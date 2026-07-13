#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ALLOWED_FRONTMATTER_KEYS = {
    "allowed-tools",
    "compatibility",
    "description",
    "license",
    "metadata",
    "name",
}
FORBIDDEN_FILENAMES = {
    ".DS_Store",
    ".env",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "id_rsa",
}
FORBIDDEN_SUFFIXES = {".key", ".p12", ".pem", ".pfx"}
FRONTMATTER_KEY = re.compile(r"^([a-zA-Z][a-zA-Z0-9_-]*):(?:\s*(.*))?$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MAX_FILE_BYTES = 2 * 1024 * 1024
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SENSITIVE_PATTERNS = {
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\b(?:gh[oprsu]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "OpenAI-style token": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "email address": re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "private absolute path": re.compile(r"(?:/Users/[^/\s]+|/home/[^/\s]+|[A-Za-z]:\\Users\\[^\\\s]+)"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "secret assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|access[_-]?token|password|passwd|secret)\b\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
}


def parse_frontmatter(skill_file: Path, errors: list[str]) -> dict[str, str]:
    content = skill_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"{skill_file}: missing opening YAML frontmatter delimiter")
        return {}
    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        errors.append(f"{skill_file}: missing closing YAML frontmatter delimiter")
        return {}

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if not line or line.lstrip().startswith("#") or line[0].isspace():
            continue
        match = FRONTMATTER_KEY.fullmatch(line)
        if not match:
            errors.append(f"{skill_file}:{line_number}: unsupported frontmatter syntax")
            continue
        key, value = match.groups()
        if key not in ALLOWED_FRONTMATTER_KEYS:
            errors.append(f"{skill_file}:{line_number}: unsupported frontmatter key {key!r}")
        if key in fields:
            errors.append(f"{skill_file}:{line_number}: duplicate frontmatter key {key!r}")
        fields[key] = (value or "").strip().strip("'\"")
    return fields


def validate_frontmatter(skill_directory: Path, errors: list[str]) -> None:
    skill_file = skill_directory / "SKILL.md"
    fields = parse_frontmatter(skill_file, errors)
    name = fields.get("name", "")
    description = fields.get("description", "")
    compatibility = fields.get("compatibility", "")
    if not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_file}: name must use lowercase kebab-case")
    if name != skill_directory.name:
        errors.append(f"{skill_file}: frontmatter name must match its directory {skill_directory.name!r}")
    if not description:
        errors.append(f"{skill_file}: description is required")
    elif len(description) > 1024:
        errors.append(f"{skill_file}: description exceeds 1024 characters")
    if len(compatibility) > 500:
        errors.append(f"{skill_file}: compatibility exceeds 500 characters")


def validate_file_path(path: Path, errors: list[str]) -> None:
    if path.is_symlink():
        errors.append(f"{path}: symlink is not publishable")
        return
    if path.name in FORBIDDEN_FILENAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
        errors.append(f"{path}: sensitive filename or extension is not publishable")
    if path.stat().st_size > MAX_FILE_BYTES:
        errors.append(f"{path}: file exceeds {MAX_FILE_BYTES} bytes")


def validate_markdown_links(path: Path, content: str, skill_directory: Path, errors: list[str]) -> None:
    for raw_target in MARKDOWN_LINK.findall(content):
        target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
        if not target or target.startswith(("#", "https://", "http://", "mailto:")):
            continue
        relative_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        resolved_target = (path.parent / relative_target).resolve()
        try:
            resolved_target.relative_to(skill_directory.resolve())
        except ValueError:
            errors.append(f"{path}: relative Markdown link leaves the skill directory: {target}")
            continue
        if not resolved_target.exists():
            errors.append(f"{path}: broken relative Markdown link: {target}")


def validate_evaluations(path: Path, data: object, skill_directory: Path, errors: list[str]) -> None:
    if isinstance(data, list):
        for index, evaluation in enumerate(data):
            location = f"{path}[{index}]"
            if not isinstance(evaluation, dict):
                errors.append(f"{location}: trigger evaluation must be an object")
                continue
            if not isinstance(evaluation.get("query"), str) or not evaluation["query"].strip():
                errors.append(f"{location}: trigger evaluation query is required")
            if not isinstance(evaluation.get("should_trigger"), bool):
                errors.append(f"{location}: should_trigger must be a boolean")
        return
    if not isinstance(data, dict) or not isinstance(data.get("evals"), list):
        errors.append(f"{path}: evaluation file must be a trigger list or contain an evals array")
        return
    if data.get("skill_name") != skill_directory.name:
        errors.append(f"{path}: skill_name must match its directory {skill_directory.name!r}")

    seen_ids: set[int] = set()
    for index, evaluation in enumerate(data["evals"]):
        location = f"{path}.evals[{index}]"
        if not isinstance(evaluation, dict):
            errors.append(f"{location}: evaluation must be an object")
            continue
        evaluation_id = evaluation.get("id")
        if isinstance(evaluation_id, bool) or not isinstance(evaluation_id, int) or evaluation_id < 1:
            errors.append(f"{location}: id must be a positive integer")
        elif evaluation_id in seen_ids:
            errors.append(f"{location}: duplicate evaluation id {evaluation_id}")
        else:
            seen_ids.add(evaluation_id)
        for field in ("prompt", "expected_output"):
            if not isinstance(evaluation.get(field), str) or not evaluation[field].strip():
                errors.append(f"{location}: {field} is required")
        files = evaluation.get("files", [])
        if not isinstance(files, list):
            errors.append(f"{location}: files must be an array")
            continue
        for file_index, relative_file in enumerate(files):
            if not isinstance(relative_file, str):
                errors.append(f"{location}.files[{file_index}]: path must be a string")
                continue
            fixture = (skill_directory / relative_file).resolve()
            try:
                fixture.relative_to(skill_directory.resolve())
            except ValueError:
                errors.append(f"{location}.files[{file_index}]: evaluation fixture leaves the skill directory")
                continue
            if not fixture.is_file():
                errors.append(f"{location}.files[{file_index}]: missing evaluation fixture {relative_file!r}")


def validate_text_file(path: Path, skill_directory: Path, errors: list[str]) -> None:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{path}: non-UTF-8 or binary files are not allowed")
        return
    for label, pattern in SENSITIVE_PATTERNS.items():
        if pattern.search(content):
            errors.append(f"{path}: possible {label}")
    if path.suffix.lower() == ".md":
        validate_markdown_links(path, content, skill_directory, errors)
    if path.suffix.lower() == ".json":
        try:
            parsed_json = json.loads(content)
        except json.JSONDecodeError as error:
            errors.append(f"{path}:{error.lineno}: invalid JSON: {error.msg}")
        else:
            if path.parent.name == "evals":
                validate_evaluations(path, parsed_json, skill_directory, errors)
    if path.suffix.lower() == ".py":
        try:
            compile(content, str(path), "exec")
        except SyntaxError as error:
            errors.append(f"{path}:{error.lineno}: invalid Python: {error.msg}")


def verify_repository(repository: Path) -> tuple[list[Path], list[str]]:
    errors: list[str] = []
    skills_directory = repository / "skills"
    if not skills_directory.is_dir():
        return [], [f"{skills_directory}: skills directory is required"]
    skill_directories = sorted(path.parent for path in skills_directory.glob("*/SKILL.md"))
    if not skill_directories:
        return [], [f"{skills_directory}: no skills found"]

    for skill_directory in skill_directories:
        validate_frontmatter(skill_directory, errors)
        for path in sorted(skill_directory.rglob("*")):
            if path.is_dir() and not path.is_symlink():
                continue
            validate_file_path(path, errors)
            if path.is_file() and not path.is_symlink():
                validate_text_file(path, skill_directory, errors)
    return skill_directories, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate public agent skills before release.")
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    args = parser.parse_args()
    skill_directories, errors = verify_repository(args.repository.resolve())
    if errors:
        print("Skill verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    names = ", ".join(path.name for path in skill_directories)
    print(f"Verified {len(skill_directories)} skill(s): {names}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
