#!/usr/bin/env python3
"""Generate a self-contained owner roadmap from Design Steward state."""

from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


REQUIRED_TOP_LEVEL = {
    "schema_version",
    "record_type",
    "engagement",
    "dependency_preflight",
    "resume",
    "authority",
    "constraints",
    "decisions",
    "working_assumptions",
    "blocking_unknowns",
    "research_and_materials",
    "funnel",
    "artifacts",
    "coverage",
    "implementation",
    "checks",
    "risks",
    "roadmap",
}


def esc(value: Any) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def validate_state(data: Any) -> list[str]:
    if not isinstance(data, dict):
        return ["state root must be a JSON object"]

    errors = [
        f"missing required field: {field}"
        for field in sorted(REQUIRED_TOP_LEVEL - data.keys())
    ]
    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be '1.0.0'")
    if data.get("record_type") != "design-steward-state":
        errors.append("record_type must be 'design-steward-state'")

    for field in (
        "decisions",
        "research_and_materials",
        "artifacts",
        "coverage",
        "working_assumptions",
        "blocking_unknowns",
        "risks",
        "roadmap",
    ):
        if field in data and not isinstance(data[field], list):
            errors.append(f"{field} must be an array")

    for field in (
        "engagement",
        "dependency_preflight",
        "resume",
        "authority",
        "constraints",
        "funnel",
        "implementation",
        "checks",
    ):
        if field in data and not isinstance(data[field], dict):
            errors.append(f"{field} must be an object")

    return errors


def href(value: Any, label: Any | None = None) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    text = esc(label if label is not None else raw)
    scheme = urlsplit(raw).scheme.lower()
    if scheme and scheme not in {"http", "https", "file", "mailto"}:
        return text
    return f'<a href="{esc(raw)}">{text}</a>'


def links(values: Any) -> str:
    rendered: list[str] = []
    for item in as_list(values):
        if isinstance(item, dict):
            target = item.get("url") or item.get("path") or item.get("path_or_url")
            label = item.get("label") or item.get("title") or target
            if target:
                rendered.append(href(target, label))
        elif item:
            rendered.append(href(item))
    return " · ".join(rendered)


def status_tone(status: Any) -> str:
    normalized = str(status or "").lower().replace(" ", "-").replace("_", "-")
    if any(word in normalized for word in ("not-selected", "pending", "not-started", "not-yet", "not-done")):
        return "pending"
    if any(word in normalized for word in ("fail", "blocked", "unavailable", "stop", "rejected", "gap", "material-delta")):
        return "negative"
    if any(word in normalized for word in ("progress", "review", "promising", "iterate", "iterating", "active")):
        return "active"
    if any(word in normalized for word in ("complete", "accepted", "pass", "selected", "represented", "promoted", "frozen")):
        return "positive"
    return "neutral"


def badge(status: Any) -> str:
    value = str(status or "Unknown")
    return f'<span class="badge {status_tone(value)}">{esc(value)}</span>'


def gate_state(status: Any) -> tuple[str, str, str]:
    tone = status_tone(status)
    if tone == "positive":
        return tone, "Completed", "✓"
    if tone == "active":
        return tone, "In progress", "→"
    if tone == "negative":
        return tone, "Blocked", "!"
    return "pending", "Not done", "○"


def token_list(values: Any, empty: str) -> str:
    items = [str(item) for item in as_list(values) if str(item).strip()]
    if not items:
        return f'<span class="gate-empty">{esc(empty)}</span>'
    return "".join(f'<span class="ref-token">{esc(item)}</span>' for item in items)


def text_list(values: Any, empty: str = "None recorded") -> str:
    items = as_list(values)
    if not items:
        return f'<p class="muted">{esc(empty)}</p>'
    rows = []
    for item in items:
        if isinstance(item, dict):
            title = item.get("title") or item.get("id") or item.get("statement") or item.get("question")
            detail = item.get("summary") or item.get("rationale") or item.get("risk") or item.get("status")
            body = f"<strong>{esc(title)}</strong>" if title else ""
            if detail:
                body += f'<span class="list-detail">{esc(detail)}</span>'
            rows.append(f"<li>{body}</li>")
        else:
            rows.append(f"<li>{esc(item)}</li>")
    return f'<ul class="plain-list">{"".join(rows)}</ul>'


def render_roadmap(data: dict[str, Any]) -> str:
    rows = []
    ordered = sorted(as_list(data.get("roadmap")), key=lambda item: as_dict(item).get("order", 999))
    for index, raw in enumerate(ordered):
        item = as_dict(raw)
        gate = item.get("gate") or f"G{index}"
        tone, label, symbol = gate_state(item.get("status"))
        open_items = as_list(item.get("open_items"))
        open_copy = " · ".join(str(value) for value in open_items if str(value).strip())
        if not open_copy:
            open_copy = "Gate closed" if tone == "positive" else "No next condition recorded"
        rows.append(
            f'<article class="gate-step {tone}">'
            '<div class="gate-station">'
            f'<span class="gate-code">{esc(gate)}</span><span class="gate-symbol">{esc(symbol)}</span>'
            '</div>'
            '<div class="gate-panel">'
            '<header class="gate-heading">'
            f'<div><div class="gate-sequence">Stage {index + 1} of {len(ordered)}</div><h3>{esc(item.get("stage", "Unnamed stage"))}</h3></div>'
            f'<span class="gate-status {tone}">{esc(label)}</span>'
            '</header>'
            f'<p class="gate-result">{esc(item.get("decision_or_result") or "No decision recorded yet.")}</p>'
            '<div class="gate-facts">'
            f'<div><span>Evidence</span><div class="token-row">{token_list(item.get("evidence_ids"), "None linked")}</div></div>'
            f'<div><span>Outputs</span><div class="token-row">{token_list(item.get("artifact_ids"), "None linked")}</div></div>'
            f'<div><span>{"Remaining" if tone != "positive" else "Closure"}</span><p>{esc(open_copy)}</p></div>'
            '</div>'
            f'<div class="gate-links">{links(item.get("links"))}</div>'
            '</div></article>'
        )
    return '<div class="gate-timeline">' + ("".join(rows) or '<p class="muted">No roadmap gates recorded.</p>') + '</div>'


def render_decisions(data: dict[str, Any]) -> str:
    rows = []
    for raw in as_list(data.get("decisions")):
        item = as_dict(raw)
        evidence = ", ".join(str(x) for x in as_list(item.get("evidence_ids"))) or "None"
        supersession = item.get("supersedes") or item.get("superseded_by") or "—"
        rows.append(
            '<article class="decision-card">'
            f'<div class="card-kicker">{esc(item.get("id", "Decision"))} · {esc(item.get("decided_at", "time unrecorded"))}</div>'
            f'<div class="card-title-row"><h3>{esc(item.get("question") or item.get("title") or "Untitled decision")}</h3>{badge(item.get("status"))}</div>'
            f'<p><strong>Owner input</strong><br>{esc(item.get("owner_original_input") or "None")}</p>'
            f'<p><strong>Steward recommendation</strong><br>{esc(item.get("steward_recommendation") or "None")}</p>'
            f'<p><strong>Resolution</strong><br>{esc(item.get("resolution") or "Unresolved")}</p>'
            f'<div class="meta-grid"><span>Owner: {esc(item.get("decision_owner") or "Unassigned")}</span><span>Evidence: {esc(evidence)}</span><span>Supersession: {esc(supersession)}</span></div>'
            f'<div class="links">{links(item.get("links"))}</div>'
            '</article>'
        )
    return "".join(rows) or '<p class="muted">No material decisions recorded.</p>'


def render_research(data: dict[str, Any]) -> str:
    rows = []
    for raw in as_list(data.get("research_and_materials")):
        item = as_dict(raw)
        source = item.get("url_or_path") or item.get("source")
        title = item.get("title") or item.get("question") or item.get("id") or "Research item"
        rows.append(
            '<article class="research-card">'
            f'<div class="card-kicker">{esc(item.get("id", "Source"))} · {esc(item.get("evidence_level", "Unclassified"))}</div>'
            f'<h3>{href(source, title) if source else esc(title)}</h3>'
            f'<p><strong>Material used</strong><br>{esc(item.get("material_used") or "Not recorded")}</p>'
            f'<p><strong>Design implication</strong><br>{esc(item.get("design_implication") or "None recorded")}</p>'
            f'<p class="muted">Limitations: {esc(item.get("limitations") or "None recorded")}</p>'
            '</article>'
        )
    return "".join(rows) or '<p class="muted">No decision-relevant research recorded.</p>'


def funnel_group(title: str, values: Any, selected_id: str) -> str:
    rows = []
    for raw in as_list(values):
        item = as_dict(raw)
        item_id = str(item.get("id") or "")
        active = " selected" if item_id and item_id == selected_id else ""
        name = item.get("title") or item.get("name") or item.get("thesis") or item_id or "Untitled"
        summary = (
            item.get("promise")
            or item.get("thesis")
            or item.get("summary")
            or item.get("disposition_reason")
            or ""
        )
        rows.append(
            f'<li class="funnel-item{active}"><div><strong>{esc(name)}</strong><span>{esc(summary)}</span></div>{badge(item.get("status") or item.get("disposition"))}</li>'
        )
    content = "".join(rows) or '<li class="muted">None recorded</li>'
    return f'<div class="funnel-column"><h3>{esc(title)}</h3><ul>{content}</ul></div>'


def render_funnel(data: dict[str, Any]) -> str:
    funnel = as_dict(data.get("funnel"))
    selected = as_dict(funnel.get("selected_backbone"))
    selected_id = str(selected.get("direction_id") or "")
    summary = (
        '<article class="selected-backbone">'
        '<div><div class="card-kicker">Selected backbone</div>'
        f'<h3>{esc(selected.get("title") or "Not selected")}</h3>'
        f'<p>{esc(selected.get("summary") or "No selected direction yet.")}</p></div>'
        f'{badge(selected.get("status"))}</article>'
    )
    columns = "".join(
        (
            funnel_group("Raw concepts", funnel.get("raw_concepts"), selected_id),
            funnel_group("Territories", funnel.get("territories"), selected_id),
            funnel_group("Developed directions", funnel.get("developed_directions"), selected_id),
        )
    )
    return summary + f'<div class="funnel-grid">{columns}</div>'


def render_artifacts(data: dict[str, Any]) -> str:
    rows = []
    for raw in as_list(data.get("artifacts")):
        item = as_dict(raw)
        target = item.get("path_or_url")
        title = item.get("title") or item.get("id") or "Artifact"
        state_text = ", ".join(str(x) for x in as_list(item.get("states"))) or "States not recorded"
        viewport_text = ", ".join(str(x) for x in as_list(item.get("viewports"))) or "Viewports not recorded"
        rows.append(
            '<article class="artifact-card">'
            f'<div class="card-title-row"><h3>{href(target, title) if target else esc(title)}</h3>{badge(item.get("status"))}</div>'
            f'<p>{esc(item.get("kind") or "Artifact")} · {esc(item.get("direction_id") or "No direction")}</p>'
            f'<p class="muted">States: {esc(state_text)}<br>Viewports: {esc(viewport_text)}</p>'
            f'<p>{esc(item.get("limitations") or "")}</p>'
            '</article>'
        )
    return "".join(rows) or '<p class="muted">No generated artifacts recorded.</p>'


def render_coverage(data: dict[str, Any]) -> str:
    rows = []
    for raw in as_list(data.get("coverage")):
        item = as_dict(raw)
        artifact = item.get("artifact") or item.get("artifact_id") or item.get("explicit_exclusion") or "—"
        rows.append(
            "<tr>"
            f'<td>{esc(item.get("id") or "")}</td>'
            f'<td>{esc(item.get("journey_or_state") or item.get("scope") or "")}</td>'
            f'<td>{esc(item.get("role_domain_or_destination") or item.get("context") or "")}</td>'
            f'<td>{badge(item.get("status"))}</td>'
            f'<td>{esc(artifact)}</td>'
            "</tr>"
        )
    body = "".join(rows) or '<tr><td colspan="5" class="muted">No coverage rows recorded.</td></tr>'
    return (
        '<div class="table-wrap"><table><thead><tr><th>ID</th><th>Journey/state</th><th>Role/domain/destination</th><th>Status</th><th>Artifact or exclusion</th></tr></thead>'
        f'<tbody>{body}</tbody></table></div>'
    )


def render_implementation(data: dict[str, Any]) -> str:
    implementation = as_dict(data.get("implementation"))
    statuses = "".join(
        (
            f'<article><span>Engineering source acceptance</span>{badge(implementation.get("engineering_source_acceptance"))}</article>',
            f'<article><span>Design-integration acceptance</span>{badge(implementation.get("design_integration_acceptance"))}</article>',
            f'<article><span>Preview/deployed fidelity</span>{badge(implementation.get("preview_or_deployed_fidelity"))}</article>',
        )
    )
    pairs = []
    for raw in as_list(implementation.get("fidelity_pairs")):
        item = as_dict(raw)
        pairs.append(
            "<tr>"
            f'<td>{esc(item.get("state") or item.get("id") or "")}</td>'
            f'<td>{href(item.get("reference_capture"), "Reference")}</td>'
            f'<td>{href(item.get("implementation_capture"), "Implementation")}</td>'
            f'<td>{esc(item.get("composition_constraints") or "")}</td>'
            f'<td>{badge(item.get("status"))}</td>'
            "</tr>"
        )
    pair_body = "".join(pairs) or '<tr><td colspan="5" class="muted">No matched fidelity pairs recorded.</td></tr>'
    reviewer = as_dict(implementation.get("fidelity_reviewer"))
    reviewer_text = reviewer.get("name_and_role") or "Unassigned"
    independent = "independent" if reviewer.get("independent_of_implementation") is True else "independence not established"
    return (
        f'<div class="acceptance-grid">{statuses}</div>'
        f'<p class="muted">Fidelity reviewer: {esc(reviewer_text)} · {esc(independent)}</p>'
        '<div class="table-wrap"><table><thead><tr><th>State</th><th>Frozen reference</th><th>Implementation</th><th>Composition contract</th><th>Status</th></tr></thead>'
        f'<tbody>{pair_body}</tbody></table></div>'
        '<div class="two-column">'
        f'<div><h3>Implementation deltas</h3>{text_list(implementation.get("deltas"))}</div>'
        f'<div><h3>Residual risks</h3>{text_list(data.get("risks"))}</div>'
        '</div>'
    )


def render_page(data: dict[str, Any], source_path: Path) -> str:
    engagement = as_dict(data.get("engagement"))
    resume = as_dict(data.get("resume"))
    authority = as_dict(data.get("authority"))
    dependency = as_dict(data.get("dependency_preflight"))
    checks = as_dict(data.get("checks"))
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    roadmap_items = sorted(
        as_list(data.get("roadmap")), key=lambda item: as_dict(item).get("order", 999)
    )
    completed_gates = sum(
        status_tone(as_dict(item).get("status")) == "positive"
        for item in roadmap_items
    )
    progress_segments = "".join(
        f'<span class="progress-segment {gate_state(as_dict(item).get("status"))[0]}" '
        f'title="{esc(as_dict(item).get("gate") or f"G{index}")} — '
        f'{esc(gate_state(as_dict(item).get("status"))[1])}"></span>'
        for index, item in enumerate(roadmap_items)
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(engagement.get("title") or "Design Steward roadmap")}</title>
<style>
:root{{--ink:#10243f;--muted:#60758a;--canvas:#eaf1f7;--paper:#ffffff;--line:#c7d5e2;--blue:#2458e6;--sky:#d9edff;--cyan:#56c5d0;--green:#147b65;--amber:#d98714;--coral:#cf4b43;--shadow:0 16px 42px rgba(26,61,97,.10)}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;background-color:var(--canvas);background-image:linear-gradient(rgba(36,88,230,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(36,88,230,.045) 1px,transparent 1px);background-size:28px 28px;color:var(--ink);font:16px/1.52 "Avenir Next",Avenir,"Trebuchet MS",system-ui,sans-serif}}
a{{color:#1749c6;text-underline-offset:3px}} a:focus-visible{{outline:3px solid var(--amber);outline-offset:3px;border-radius:3px}} .page{{max-width:1220px;margin:0 auto;padding:28px 24px 80px}}
.hero{{background:var(--paper);border:1px solid var(--line);border-top:10px solid var(--blue);border-radius:0 0 26px 26px;padding:34px 38px 28px;box-shadow:var(--shadow);position:relative;overflow:hidden}} .hero:after{{content:"";position:absolute;width:340px;height:340px;right:-180px;top:-190px;border:52px solid var(--sky);border-radius:50%;opacity:.75}}
.hero-lead{{display:grid;grid-template-columns:minmax(0,1fr) 210px;gap:38px;align-items:end;position:relative;z-index:1}} .eyebrow,.card-kicker,.gate-sequence{{font:800 .72rem/1.2 "Arial Narrow","Avenir Next",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--blue)}}
h1{{font-size:clamp(2.45rem,6vw,5.2rem);line-height:.92;letter-spacing:-.06em;max-width:840px;margin:.22em 0 .18em}} h2{{font-size:clamp(1.8rem,3.4vw,3rem);line-height:1;letter-spacing:-.045em;margin:0 0 16px}} h3{{margin:0;font-size:1.08rem;line-height:1.22}} .hero-summary{{font-size:1.08rem;max-width:760px;color:var(--muted);margin:0}}
.journey-score{{background:var(--blue);color:#fff;padding:22px;clip-path:polygon(0 0,100% 0,100% 82%,84% 100%,0 100%)}} .journey-score strong{{display:block;font-size:3.4rem;line-height:.9;letter-spacing:-.06em}} .journey-score span{{display:block;margin-top:9px;font:800 .72rem/1.3 "Arial Narrow",sans-serif;letter-spacing:.12em;text-transform:uppercase}}
.progress-wrap{{position:relative;z-index:1;margin-top:26px}} .progress-labels{{display:flex;justify-content:space-between;gap:12px;color:var(--muted);font-size:.8rem;margin-bottom:7px}} .progress-track{{display:grid;grid-template-columns:repeat({max(len(roadmap_items), 1)},1fr);gap:5px;height:12px}} .progress-segment{{background:#c6d3df}} .progress-segment:first-child{{border-radius:9px 0 0 9px}} .progress-segment:last-child{{border-radius:0 9px 9px 0}} .progress-segment.positive{{background:var(--green)}} .progress-segment.active{{background:var(--amber)}} .progress-segment.negative{{background:var(--coral)}}
.hero-grid,.meta-grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:22px;position:relative;z-index:1}} .hero-grid>div{{padding:12px 0;border-top:1px solid var(--line)}} .hero-grid span,.acceptance-grid article>span:first-child{{display:block;font:800 .7rem/1.2 "Arial Narrow",sans-serif;text-transform:uppercase;letter-spacing:.11em;color:var(--muted);margin-bottom:5px}} .hero-grid .next-action{{grid-column:span 2;color:var(--blue);font-weight:700}}
nav{{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0 0}} nav a{{color:var(--ink);background:rgba(255,255,255,.8);border-bottom:3px solid var(--line);padding:8px 11px;text-decoration:none;font:750 .8rem/1.2 "Avenir Next",sans-serif}} nav a:hover{{border-color:var(--blue);color:var(--blue)}}
section{{padding:58px 0;border-top:1px solid var(--line)}} .section-intro{{max-width:720px;color:var(--muted);margin-top:-8px}} #roadmap{{border-top:0;padding-top:46px}}
.gate-timeline{{position:relative;margin-top:34px}} .gate-timeline:before{{content:"";position:absolute;left:69px;top:42px;bottom:42px;width:7px;background:#c8d7e4;border-radius:9px}}
.gate-step{{--gate:#8ba0b2;display:grid;grid-template-columns:140px minmax(0,1fr);gap:26px;position:relative;margin:0 0 26px}} .gate-step.positive{{--gate:var(--green)}} .gate-step.active{{--gate:var(--amber)}} .gate-step.negative{{--gate:var(--coral)}} .gate-step.pending{{--gate:#8ba0b2}}
.gate-station{{position:relative;min-height:92px;display:grid;place-items:start center;z-index:1}} .gate-code{{width:92px;height:92px;border-radius:50%;display:grid;place-items:center;background:var(--paper);border:9px solid var(--gate);color:var(--ink);font:900 1.7rem/1 "Arial Narrow",sans-serif;letter-spacing:-.03em;box-shadow:0 0 0 7px var(--canvas)}} .gate-symbol{{position:absolute;right:12px;bottom:1px;width:31px;height:31px;border-radius:50%;display:grid;place-items:center;background:var(--gate);border:4px solid var(--canvas);color:white;font-weight:900}}
.gate-panel{{position:relative;background:var(--paper);border:1px solid var(--line);border-left:9px solid var(--gate);padding:22px 24px;box-shadow:var(--shadow)}} .gate-panel:before{{content:"";position:absolute;left:-24px;top:35px;border-width:12px 15px 12px 0;border-style:solid;border-color:transparent var(--gate) transparent transparent}} .gate-heading,.card-title-row{{display:flex;justify-content:space-between;gap:18px;align-items:flex-start}} .gate-heading h3{{font-size:1.35rem;margin-top:4px}} .gate-status{{display:inline-flex;padding:6px 9px;color:#fff;background:var(--gate);font:850 .72rem/1 "Arial Narrow",sans-serif;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}} .gate-result{{font-size:1.05rem;margin:13px 0 18px;max-width:850px}}
.gate-facts{{display:grid;grid-template-columns:1fr 1fr 1.25fr;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}} .gate-facts>div{{padding:12px 14px 12px 0}} .gate-facts>div+div{{border-left:1px solid var(--line);padding-left:14px}} .gate-facts>div>span{{display:block;font:800 .66rem/1.2 "Arial Narrow",sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}} .gate-facts p{{margin:0;font-size:.87rem}} .token-row{{display:flex;gap:5px;flex-wrap:wrap}} .ref-token{{background:var(--sky);color:#123f91;padding:3px 6px;font:800 .72rem/1.2 "Arial Narrow",sans-serif}} .gate-empty{{color:var(--muted);font-size:.82rem}} .gate-links{{margin-top:11px;font-size:.8rem}} .gate-links:empty{{display:none}}
.badge{{display:inline-flex;align-items:center;border-radius:999px;padding:4px 9px;font-size:.72rem;font-weight:800;letter-spacing:.02em;white-space:nowrap;background:#e2e9ef;color:#4a5c6c}} .badge.positive{{background:#d9eee7;color:#0b624e}} .badge.active{{background:#fff0cf;color:#81520d}} .badge.negative{{background:#f7deda;color:#8d332d}} .badge.pending{{background:#e5ebf1;color:#526679}}
.cards,.research-grid,.artifact-grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}} .decision-card,.research-card,.artifact-card,.selected-backbone{{background:var(--paper);border:1px solid var(--line);padding:20px;box-shadow:0 8px 24px rgba(26,61,97,.06)}} .decision-card p,.research-card p,.artifact-card p{{margin:12px 0}} .meta-grid{{grid-template-columns:repeat(3,minmax(0,1fr));font-size:.8rem;color:var(--muted);margin-top:16px}} .list-detail{{display:block;color:var(--muted);font-size:.9rem}}
.selected-backbone{{display:flex;justify-content:space-between;align-items:start;border-left:9px solid var(--blue);margin-bottom:18px}} .funnel-grid{{display:grid;grid-template-columns:1.25fr .9fr .65fr;gap:12px;align-items:start}} .funnel-column{{background:rgba(255,255,255,.72);border:1px solid var(--line);padding:16px}} .funnel-column:nth-child(2){{margin-top:18px}} .funnel-column:nth-child(3){{margin-top:36px;border-top:7px solid var(--blue)}} .funnel-column ul{{list-style:none;margin:14px 0 0;padding:0}} .funnel-item{{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;padding:12px 0;border-top:1px solid var(--line)}} .funnel-item span:not(.badge){{display:block;color:var(--muted);font-size:.86rem;margin-top:3px}} .funnel-item.selected{{margin:0 -8px;padding:12px 8px;background:var(--sky)}}
.table-wrap{{overflow:auto;border:1px solid var(--line);background:var(--paper)}} table{{width:100%;border-collapse:collapse;min-width:760px}} th,td{{padding:12px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}} th{{font:800 .7rem/1.2 "Arial Narrow",sans-serif;text-transform:uppercase;letter-spacing:.09em;background:#dfe9f2}} .acceptance-grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:18px 0}} .acceptance-grid article{{background:var(--ink);color:white;padding:16px;border-top:7px solid var(--blue)}} .acceptance-grid article:nth-child(2){{border-color:var(--amber)}} .acceptance-grid article:nth-child(3){{border-color:var(--coral)}} .two-column{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:24px}} .plain-list{{padding-left:20px}} .plain-list li{{margin:8px 0}} .muted{{color:var(--muted)}} .links:empty{{display:none}} .footer{{font-size:.8rem;color:var(--muted);padding-top:24px}}
@media(max-width:800px){{.page{{padding:12px 12px 48px}}.hero{{padding:26px 20px 22px}}.hero-lead{{grid-template-columns:1fr}}.journey-score{{max-width:190px}}.hero-grid,.meta-grid,.cards,.research-grid,.artifact-grid,.funnel-grid,.acceptance-grid,.two-column,.gate-facts{{grid-template-columns:1fr}}.hero-grid .next-action{{grid-column:auto}}.gate-timeline:before{{left:31px}}.gate-step{{grid-template-columns:64px minmax(0,1fr);gap:14px}}.gate-code{{width:62px;height:62px;border-width:6px;font-size:1.2rem;box-shadow:0 0 0 4px var(--canvas)}}.gate-symbol{{right:-2px;bottom:18px;width:26px;height:26px;border-width:3px}}.gate-panel{{padding:18px 16px;border-left-width:7px}}.gate-panel:before{{left:-19px;top:22px;border-width:9px 12px 9px 0}}.gate-heading{{display:block}}.gate-status{{margin-top:10px}}.gate-facts>div+div{{border-left:0;border-top:1px solid var(--line);padding-left:0}}.funnel-column:nth-child(2),.funnel-column:nth-child(3){{margin-top:0}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}} @media print{{body{{background:white}}.page{{max-width:none}}.hero,.decision-card,.research-card,.artifact-card,.gate-panel{{box-shadow:none}}nav{{display:none}}}}
</style>
</head>
<body><main class="page">
<header class="hero">
  <div class="hero-lead">
    <div>
      <div class="eyebrow">Design Steward · The route to this design</div>
      <h1>{esc(engagement.get("title") or "Untitled design engagement")}</h1>
      <p class="hero-summary">{esc(resume.get("latest_summary") or "No current summary recorded.")}</p>
    </div>
    <div class="journey-score"><strong>{completed_gates}/{len(roadmap_items)}</strong><span>gates completed</span></div>
  </div>
  <div class="progress-wrap">
    <div class="progress-labels"><span>Commission</span><span>Live learning</span></div>
    <div class="progress-track" aria-label="{completed_gates} of {len(roadmap_items)} gates completed">{progress_segments}</div>
  </div>
  <div class="hero-grid">
    <div><span>Owner</span>{esc(engagement.get("system_owner") or "Unassigned")}</div>
    <div><span>Now</span>{esc(resume.get("current_gate"))} · {esc(resume.get("current_stage"))}</div>
    <div><span>Required dependency</span>{esc(dependency.get("resolved_skill") or dependency.get("required_skill"))} · {esc(dependency.get("status"))}</div>
    <div class="next-action"><span>Next move</span>{esc(resume.get("exact_next_action") or "Unrecorded")}</div>
    <div><span>Authority</span>{esc(authority.get("authorization_boundary") or "Unrecorded")}</div>
  </div>
</header>
<nav aria-label="Roadmap sections"><a href="#roadmap">Gate timeline</a><a href="#decisions">Decisions</a><a href="#research">Inputs</a><a href="#funnel">Concept funnel</a><a href="#artifacts">Mocks</a><a href="#coverage">Coverage</a><a href="#implementation">Fidelity</a><a href="#open">Open work</a></nav>
<section id="roadmap"><div class="eyebrow">One route · Seven decisions</div><h2>Gates at a glance</h2><p class="section-intro">Read top to bottom. Each gate shows the decision gained, its proof, the output it produced, and what still prevents closure.</p>{render_roadmap(data)}</section>
<section id="decisions"><h2>Material decisions</h2><p class="section-intro">Owner input, Steward judgment, evidence, approvals, and supersession remain distinct.</p><div class="cards">{render_decisions(data)}</div></section>
<section id="research"><h2>Research and materials used</h2><p class="section-intro">Only sources that changed a design decision or remain an active limitation.</p><div class="research-grid">{render_research(data)}</div></section>
<section id="funnel"><h2>Concept funnel</h2><p class="section-intro">How broad ideas narrowed into territories, developed directions, and one selected backbone.</p>{render_funnel(data)}</section>
<section id="artifacts"><h2>Generated mocks and design artifacts</h2><div class="artifact-grid">{render_artifacts(data)}</div></section>
<section id="coverage"><h2>Commission coverage</h2><p class="section-intro">Every in-scope branch and destination maps to an artifact, an explicit exclusion, or a visible gap.</p>{render_coverage(data)}</section>
<section id="implementation"><h2>Implementation fidelity</h2><p class="section-intro">Engineering correctness, design integration, and deployed fidelity are separate claims.</p>{render_implementation(data)}</section>
<section id="open"><h2>Open work and recovery</h2><div class="two-column"><div><h3>Blocking unknowns</h3>{text_list(data.get("blocking_unknowns"))}<h3>Working assumptions</h3>{text_list(data.get("working_assumptions"))}</div><div><h3>Completed checks</h3>{text_list(checks.get("completed"))}<h3>Deferred checks</h3>{text_list(checks.get("deferred"))}</div></div><article class="selected-backbone"><div><div class="card-kicker">Resume from here</div><h3>{esc(resume.get("exact_next_action") or "No next action recorded")}</h3><p>Stopping point: {esc(resume.get("stopping_point") or "Unrecorded")}</p></div>{badge(resume.get("current_stage"))}</article></section>
<footer class="footer">Generated {esc(generated_at)} from {esc(source_path)}. This self-contained page is a view of <code>steward-state.json</code>, not a second source of truth.</footer>
</main></body></html>"""


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", type=Path, help="Path to steward-state.json")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output HTML path; defaults to steward-roadmap.html beside the state file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        data = json.loads(args.state.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"error: cannot read valid state JSON: {error}", file=sys.stderr)
        return 2

    errors = validate_state(data)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    output = args.output or args.state.with_name("steward-roadmap.html")
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_page(data, args.state), encoding="utf-8")
    except OSError as error:
        print(f"error: cannot write roadmap: {error}", file=sys.stderr)
        return 2

    print(json.dumps({"ok": True, "output": str(output), "source": str(args.state)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
