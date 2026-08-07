---
name: marktplaats-ad-creator
description: Create accurate, effective Marktplaats.nl listings from item photos and seller-provided details. Use this skill whenever the user wants to sell, value, draft, improve, or post an item on Marktplaats. Adapt pricing, negotiation, delivery, and browser settings to the seller's stated goal instead of imposing one sales strategy. Research current comparable listings when pricing is needed, disclose uncertainty and defects, and require confirmation before publishing or enabling consequential options.
compatibility: Requires image input support for photo analysis and browser control for posting. Without those capabilities, research and draft the listing from seller-provided details and provide manual posting instructions.
license: MIT
---

# Marktplaats Ad Creator

## Goal

Create a truthful, searchable Marktplaats listing aligned with the seller's objective. Do not assume that every seller wants the fastest sale, the highest possible price, negotiation room, bidding, shipping, or Direct Kopen.

Separate public listing content from private seller guidance. Never expose a private minimum price, address, contact detail, trade preference, or negotiation limit unless the user explicitly wants it in the advertisement.

## Required Inputs

Use uploaded images and user-provided text before asking questions. Ask only for information that materially affects accuracy, price, or posting.

Collect as relevant:

- Item identity: category, brand, model, size, variant, capacity, year, edition, or compatibility
- Condition: working status, defects, repairs, cosmetic wear, authenticity, and safety issues
- Included items: accessories, original packaging, receipts, manuals, chargers, cables, or missing parts
- Seller objective: quick sale, balanced outcome, maximum value, fixed price, or another stated priority
- Timing: desired sale window or deadline
- Price preferences: fixed price, price advice, willingness to negotiate, optional private minimum
- Transaction settings: asking price, bidding, Direct Kopen, trade language, or other options currently offered by Marktplaats
- Logistics: pickup, shipping, delivery area, package constraints, and location or postcode when the form requires it

State exactly what an image does and does not establish. Never infer hidden damage, working status, authenticity, ownership, included accessories, or exact model details from ambiguous evidence.

## Workflow

### 1. Inspect the item

- Identify visible markings, condition, accessories, defects, and useful photo evidence.
- Distinguish observation from seller-provided fact and inference.
- Flag facts that require disclosure to prevent a misleading listing or later dispute.
- Recommend additional photos when identification, condition, scale, or completeness is unclear.

### 2. Establish the seller's strategy

Determine the user's priority before recommending a price or transaction mode:

- **Quick sale:** prioritize a competitive price and low-friction pickup or shipping.
- **Balanced:** target a realistic market price with a reasonable expected sale time.
- **Maximum value:** tolerate a longer listing period and support the price with condition, completeness, rarity, or proof of value.
- **Seller-defined:** follow a fixed price, deadline, negotiation rule, or other explicit constraint.

If no strategy is given, present a balanced recommendation as a proposal, not as a hidden assumption. Confirm the strategy before filling the browser form.

### 3. Research current comparables

Research when the user requests price advice or has not supplied a fixed price:

- Search current Marktplaats listings first and use other relevant Dutch or EU resale sources when they improve coverage.
- Prefer the same model, version, size, condition, and included items; use close substitutes only when exact matches are scarce.
- Account for condition, completeness, age, warranty or receipt, local supply, seasonality, pickup friction, and shipping cost.
- Separate asking prices from verified sale prices. Active asking prices do not prove what buyers paid.
- Exclude obvious outliers unless they explain the market range.
- Record source, URL, comparable, price, condition, location when relevant, observation date, and pricing impact.

Do not call a price researched unless the supporting comparables are shown. When evidence is thin or contradictory, provide a range and explain the uncertainty.

### 4. Recommend pricing and transaction settings

Provide the recommendation that matches the chosen strategy:

- Estimate a defensible market range from the comparable evidence.
- Recommend a visible price or price mode and explain its expected tradeoff between value, speed, and buyer friction.
- Provide a private minimum or negotiation plan only when the user requests one or indicates willingness to negotiate.
- Treat bidding, Direct Kopen, trade language, and fixed-price sales as separate choices. Do not enable or disable them based on a prior seller's preference.
- Verify current Marktplaats behavior and costs before recommending platform-dependent options. Direct Kopen, buyer protection, payment, shipping, and bidding combinations can change.
- Select shipping only from the packed item's measured or credible dimensions and weight plus the options currently shown. Do not assume a package tier from the product category.

### 5. Draft the listing

- Use Dutch unless the user requests another language.
- Write a specific, searchable title using the strongest verified identity and attributes.
- Put the item, condition, important included parts, and material defect disclosures early.
- Use concise paragraphs or bullets appropriate to the item.
- Include only verified claims about working condition, age, authenticity, ownership, retail price, or warranty.
- State pickup, shipping, delivery, and payment expectations accurately.
- Match the tone to the seller's objective without inventing urgency, scarcity, buyer competition, or negotiation flexibility.
- Do not add trades, bidding invitations, a minimum price, or off-platform contact details unless explicitly requested.

### 6. Confirm the complete draft

Before opening or editing the posting form, show:

- Seller objective
- Proposed category
- Title and description
- Price mode and visible price or range
- Private pricing guidance, only when applicable
- Comparable evidence
- Photo order and missing-photo recommendations
- Pickup, shipping, or delivery settings
- Bidding, Direct Kopen, trade, and paid-promotion choices
- Remaining uncertainties and assumptions

Ask the user to confirm the draft and settings before changing the browser form.

### 7. Prepare the advertisement in the browser

- Use the available browser tooling to open Marktplaats and start the placement flow.
- Ask the user to handle login, CAPTCHA, identity checks, payment verification, and other account-security steps.
- Upload photos in an informative order: overview, key angles, model or authenticity markings, included items, condition details, and defects.
- Select only the category, price mode, bidding, Direct Kopen, logistics, and promotion settings the user approved.
- Re-check fields that Marktplaats enables automatically or changes after another selection.
- If an option has payment, buyer-protection, shipping, tax, legal, or irreversible consequences that were not confirmed, stop and explain the current tradeoff.
- Do not add paid promotion, Pro CPC, boosters, automatic bidding, or other charges without explicit authorization after the cost is visible.
- On the final review screen, report the exact visible category, title, price, transaction settings, delivery settings, fees, and promotion state.
- Stop before the action that publishes the advertisement and request final approval in the current conversation.

## Browser and Transaction Safety

- Use only the user's own account and items they are authorized to sell.
- Do not list prohibited, recalled, counterfeit, unsafe, or regulated goods without resolving the applicable platform and legal requirements.
- Do not bulk-post, duplicate listings, bypass CAPTCHA or access controls, evade platform limits, or continue past an anti-automation challenge.
- Keep account data, contact details, addresses, payment settings, and identity information out of chat unless strictly necessary.
- Do not change account settings, save payment methods, or connect a bank account.
- Prefer Marktplaats Berichten and official payment or shipping flows. Flag requests to move communication or payment off-platform as a safety risk.
- Do not publish without explicit final approval.

## Output Format Before Posting

```markdown
## Listing Draft
Seller objective: ...
Category: ...
Title: ...
Price mode: ...
Visible price or range: EUR ...
Private pricing guidance: ... / Not requested
Bidding: enabled / disabled / undecided
Direct Kopen: enabled / disabled / not available / undecided
Delivery: ...

Description:
...

Photo order:
1. ...
2. ...

Research basis:
| Source | URL | Comparable | Price | Condition | Location | Observed | Pricing impact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... |

Open questions or uncertainties:
- ...
```

Omit `Research basis` when the user supplied a fixed price and did not request market research. Replace `Open questions or uncertainties` with `Ready for confirmation` when nothing material remains.

## Hard Stops

Stop and ask the user when:

- Item identity or ownership is insufficient for a credible or permitted listing.
- A material defect, authenticity concern, recall, or safety issue is unresolved.
- The requested public claim is not supported by images, seller information, or authoritative evidence.
- Current platform behavior differs from the approved settings or an important option is unclear.
- Marktplaats requests payment, paid promotion, identity verification, bank details, or an irreversible account change.
- The next action would publish the advertisement.
