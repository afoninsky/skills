# Enrollment concept: three screens

Because the brief is underspecified, this is a **same-day, testable hypothesis**, not a validated final design. Assumptions: individual adults, mobile-first web, one offering, email enrollment, no payment or regulated data, and completion in under two minutes.

## 1. Choose your path

```text
┌──────────────────────────────────────┐
│ Acme                         Help    │
│                                      │
│ Join the program                     │
│ A few details and you're enrolled.   │
│                                      │
│ [ Individual                         │
│   I'm enrolling myself             ✓ ]
│ [ Organization                       │
│   I'm enrolling through my employer  ]
│                                      │
│                         [Continue →] │
│ Step 1 of 3                          │
└──────────────────────────────────────┘
```

Use plain-language cards with a large hit area. Continue stays disabled until a choice is made. On desktop, cards sit side by side in a centered 720px panel; on mobile, they stack and the primary action is full width. Preserve the selection on Back.

## 2. Tell us about you

```text
┌──────────────────────────────────────┐
│ ← Back       Your details   Step 2/3 │
│                                      │
│ First name                           │
│ [Jordan____________________________] │
│ Last name                            │
│ [Lee_______________________________] │
│ Email                                │
│ [jordan@example.com________________] │
│ We'll send confirmation here.        │
│                                      │
│                         [Review →]   │
└──────────────────────────────────────┘
```

Use persistent labels, appropriate autocomplete/input modes, and inline validation after blur—not while typing. Explain errors beside the field (“Enter an email like name@example.com”), move focus to the first error on submit, and never discard entered data. One column at all breakpoints keeps the reading order predictable.

## 3. Review and enroll

```text
┌──────────────────────────────────────┐
│ ← Back      Review details  Step 3/3 │
│                                      │
│ Enrollment type          Individual  │
│ Name                      Jordan Lee │
│ Email        jordan@example.com Edit │
│                                      │
│ □ I agree to the Terms and Privacy   │
│                                      │
│                    [Complete enroll] │
└──────────────────────────────────────┘
```

Make terms links independently focusable. On submit, show progress in the button, prevent duplicates, then replace the card with a clear success state, confirmation number, “Check your email,” and a single next action. If submission fails, retain everything and offer Retry.

Visual direction: warm white background, ink text, one high-contrast brand accent, 16px minimum body text, 8px spacing grid, 44px controls, visible keyboard focus, and reduced-motion support.

Before calling this “intuitive,” test with five representative users. Initial pass criteria: at least 4/5 complete unaided, median completion under two minutes, no repeated field errors, and every participant can state what happens next.
