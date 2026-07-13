---
name: marktplaats-ad-creator
description: Create strong Marktplaats.nl sale listings from uploaded product images and seller-provided details. Use this skill whenever the user wants to sell something on Marktplaats, create a Dutch marketplace ad, price a second-hand item for negotiation leverage, analyze item photos for resale, or post an ad through the browser. The skill researches comparable listings, asks only necessary follow-up questions, drafts the listing, sets a leverage-oriented asking price without publicly inviting lower offers or trades, and uses the browser to create the ad while explicitly avoiding the Bieden/bidding/bet option.
compatibility: Requires image input support and browser control. If browser control is not already available, use tool discovery for the in-app browser or Chrome browser before falling back to manual instructions.
license: MIT
---

# Marktplaats Ad Creator

## Goal

Create a Marktplaats listing that makes money while preserving negotiation leverage. Do not optimize for the fastest possible sale. Price the item so the user can negotiate down to a good cash outcome or use the listing as private trade leverage.

Keep leverage private. The public ad should look confident and cash-oriented, not like an invitation to bargain down. Do not mention trades, negotiation flexibility, "lichte onderhandeling", or similar buyer-facing concessions unless the user explicitly asks for that exact public wording.

## Required Inputs

Use the uploaded images and any user-provided text first. Ask follow-up questions only when missing information blocks a credible listing or price.

Minimum needed before posting:

- Item identity: brand, model, size, variant, capacity, year, or compatibility when relevant
- Condition: working status, defects, cosmetic wear, missing parts
- Included items: accessories, boxes, receipts, manuals, chargers, cables, mounts
- Logistics: pickup, shipping, location/postcode, delivery constraints
- User constraints: minimum acceptable cash price, urgency, trade interests if any

If images are ambiguous, state exactly what cannot be determined and ask for the smallest useful clarification.

## Workflow

1. Inspect Images
   - Identify the item, visible brand/model markings, condition, accessories, defects, and quality signals.
   - Note uncertainty instead of inventing details.
   - Flag anything that should be disclosed to avoid disputes.

2. Research Market Price
   - Search Marktplaats and, when useful, external Dutch/EU second-hand sources for comparable active listings and recently visible sale signals.
   - Compare same model first, then close variants.
   - Account for condition, completeness, age, urgency, seasonality, pickup/shipping friction, and listing density.
   - Ignore unrealistic outliers unless they explain buyer anchoring.
   - Record comparable evidence with source, URL, title/model, listed price, condition, location if visible, observed date, and why it affects pricing.
   - Do not present a price as researched unless the comparable evidence is shown or the research limitation is explicitly stated.

3. Choose Pricing
   - Estimate three numbers:
     - `floor_price`: the lowest price the user should accept.
     - `target_cash_price`: the realistic money outcome worth negotiating toward.
     - `asking_price`: the visible Marktplaats price.
   - Select a pricing heuristic by category:
     - Electronics, consoles, audio, and cameras: use exact model, storage/version, battery or working status, accessories, and warranty/receipt signals. Price within the comparable band because buyers compare quickly.
     - Furniture and household goods: weight pickup friction, size, visible wear, brand/design signal, and local listing density more than original retail price.
     - Bikes, scooters, tools, and appliances: require working status, maintenance state, missing parts, and safety defects before pricing.
     - Clothing, shoes, and accessories: require brand, size, authenticity signals, condition, and seasonality. Treat unknown authenticity as a hard pricing discount.
     - Collectibles, musical instruments, and niche items: favor wider research, rarity, exact edition/model, and slower-sale leverage over quick turnover.
   - Set `asking_price` above `target_cash_price` enough to create negotiation room, usually 10-25%, unless the market is illiquid, commodity-like, or already over-supplied locally.
   - Prefer clean psychological anchors: EUR 45, 75, 95, 125, 175, 225, 275, 325, 450, 575, 750.
   - Do not choose the lowest comparable price unless the user explicitly prioritizes speed.
   - If the item is suitable for trades, preserve leverage through `asking_price`, `target_cash_price`, and private notes. Do not mention trades in the public text unless the user explicitly asks to advertise trades.

4. Draft Listing
   - Use Dutch for the final Marktplaats listing unless the user requests another language.
   - Write a specific title with brand/model and the strongest searchable attributes.
   - Put important facts in the first 2 lines: item, condition, included accessories, reason only if useful.
   - Use short paragraphs or bullets.
   - Include honest condition notes.
   - Include pickup/shipping terms.
   - Keep the closing factual and short. Prefer logistics over persuasion. Example:
     - "Ophalen of verzenden mogelijk. Verzendkosten voor koper."
   - Do not write weak phrases like "mag weg", "doe maar een bod", "tegen elk aannemelijk bod", or "bieden vanaf".
   - Do not write buyer-lowering phrases like "lichte onderhandeling mogelijk", "prijs bespreekbaar", "ruilvoorstel mag", "sta open voor ruil", or "verkoop heeft voorkeur" unless the user explicitly asks to show that publicly.
   - Do not add priority, urgency, emotion, or buyer-qualifying language such as "serieuze berichten krijgen voorrang", "berichten met concrete interesse krijgen voorrang", "liefst snel ophalen", or similar filler.

5. Confirm With User
   - Before opening the posting flow, show:
     - Proposed category
     - Title
     - Description
     - Asking price
     - Floor and target cash price for the user's private reference
     - Comparable evidence table
     - Photo order recommendation
     - Pickup/shipping settings
     - Shipping package recommendation, including weight tier when the form asks for it
     - Explicit statement: "Bieden/bidding remains disabled."
   - Ask for confirmation before publishing or making irreversible changes.

6. Create Ad In Browser
   - Use the browser skill/tooling to open Marktplaats.nl and start the ad placement flow.
   - If login is required, ask the user to sign in in the browser and wait.
   - Upload the best images first: overview, front, model label, condition detail, accessories, defect close-ups.
   - Choose price type `Vraagprijs`.
   - Check whether `Bieden toestaan` was automatically enabled after selecting `Vraagprijs`; if so, switch it off.
   - Do not choose `Bieden`.
   - Do not enable "koper mag bieden", "bieden toestaan", "bieden vanaf", "Doe een bod", or any equivalent bidding/offer option.
   - Do not enable `Direct Kopen` unless the user explicitly asks for it after seeing the tradeoff; it can reduce negotiation leverage.
   - If pickup and shipping are both wanted, choose the combined pickup/shipping option and then select the smallest credible shipping package tier.
   - For tablets, phones, small electronics, game controllers, cameras, keyboards, and similar compact items with normal accessories, prefer the `0-3 kg` package tier unless the item plus packaging is clearly heavier or bulkier.
   - Use `0-10 kg` only when the payload is too large/heavy for `0-3 kg`, when protective packaging makes `0-3 kg` unrealistic, or when Marktplaats does not offer a smaller applicable tier.
   - Verify selected carriers and package tier before review; do not leave an auto-selected heavier tier unchecked.
   - If the form forces an offer/bid setting or the UI is unclear, stop and ask the user before continuing.
   - Do not add paid promotion, booster, Pro CPC, automatic bidding, or paid placement unless the user explicitly requests it after seeing the cost.
   - On the final review screen, inspect the visible listing state and report the exact values shown for price type, asking price, bidding/offer setting, Direct Kopen, category, title, shipping/pickup, package tier, and paid promotion.
   - Stop at the final review screen and ask for final approval before publishing.

## Browser Safety

- Use only the user's own account and items they are authorized to sell.
- Do not bulk-post, duplicate listings, bypass CAPTCHA or access controls, evade platform limits, or continue past an anti-automation challenge. Hand those steps to the user.
- Follow current platform rules and stop when the requested action would violate them.
- Treat the user's account, contact info, postcode, and payment settings as sensitive.
- Do not expose private profile details in the chat unless needed.
- Do not change account settings.
- Do not save payment methods.
- Do not publish without explicit user confirmation in the current conversation.

## Output Format Before Posting

Use this structure:

```markdown
## Listing Draft
Category: ...
Title: ...
Price type: Vraagprijs
Asking price: EUR ...
Private target: EUR ...
Private floor: EUR ...
Bidding: disabled
Shipping package: ...

Description:
...

Photo order:
1. ...
2. ...

Research basis:
| Source | URL | Comparable | Price | Condition | Location | Observed | Pricing impact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... |

Questions before posting:
- ...
```

If no questions remain, replace `Questions before posting` with `Ready for confirmation`.

## Pricing Notes

The user's phrase "get money and have leverage for trading" means the listing should create a strong anchor. A buyer should see a credible asking price, not a desperate quick-sale signal. The private floor is never placed in the public text. Private willingness to trade is not public ad copy; public trade language gives buyers an opening to reduce the price.

When comparables are thin, widen the research set and explain uncertainty. Use a range rather than false precision.

## Hard Stops

Stop and ask the user before continuing when:

- Material identity is insufficient for credible pricing. Require exact model only when category, buyer search behavior, compatibility, or value depends on it.
- A material defect is visible but not explained.
- The browser asks for paid promotion or payment.
- Marktplaats requires a bidding/offer field and there is no clear way to disable it.
- The next click would publish the ad.
