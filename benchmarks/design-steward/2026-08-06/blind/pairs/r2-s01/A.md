# Enrollment concept: guided, reversible, reassuring

Because the product context is undefined, treat this as a polished **prototype hypothesis**, not production-ready design. I’m assuming one individual is enrolling themselves in a single program, the flow can save progress, and payment or regulated identity checks happen elsewhere. Validate those assumptions before shipping.

## Screen 1 — Choose your enrollment

```text
Logo                         Help
Enrollment                         1 of 3
Let’s get you started
Choose the option that fits you.

┌ Program A ─ Recommended ─────────────┐
│ Short outcome statement     Details ›│
│ ○ Select                              │
└───────────────────────────────────────┘
┌ Program B ────────────────────────────┐
│ Short outcome statement     Details ›│
│ ○ Select                              │
└───────────────────────────────────────┘

                         [Continue →]
```

“Recommended” must have an explainable basis; omit it until one exists. Keep Continue disabled until selection, but explain why inline. Details open without losing state.

## Screen 2 — Tell us about you

```text
← Back    Your details                  2 of 3
We’ll use this to create your enrollment.

Full name        [                         ]
Email            [                         ]
Date of birth    [ DD ] [ MM ] [ YYYY ]
                 Why we ask
☐ I agree to the Terms and Privacy Notice

Saved automatically                     [Continue →]
```

Ask only what is necessary at this point. Use persistent labels, appropriate input types/autofill, field-level help, and validate on blur or submit—not while typing. Errors state the problem and remedy. Legal consent is never preselected.

## Screen 3 — Review and submit

```text
← Back    Review                         3 of 3
Check everything before enrolling.

Program A                              Edit
Name / email / date of birth           Edit

What happens next
• Confirmation sent by email
• You can update details later

[Confirm enrollment]
Nothing is submitted until you confirm.
```

After confirmation, replace the button with an unmistakable success state, enrollment reference, next action, and recovery path if email does not arrive. Prevent duplicate submission.

### Responsive and quality bar

On mobile, use one column and a sticky bottom action above the safe area; on desktop, constrain content to about 640px and keep the same reading order. Target 44px controls, visible keyboard focus, 4.5:1 text contrast, semantic headings, announced errors, and no color-only status. Preserve entered data across navigation and interruption.

Before release, define success as a measurable funnel: completion rate, time to complete, field-error rate, abandonment by step, and support contacts. Test the prototype with representative users, including keyboard and screen-reader users; the most important unknown is whether these are the right choices and fields—not the visual polish.
