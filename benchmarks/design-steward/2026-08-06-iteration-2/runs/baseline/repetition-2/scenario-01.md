# Enrollment experience: three-screen concept

This is a directionally polished concept, not a validated solution. To move today, I’m assuming a consumer service, mobile-first use, one primary applicant, no unusual compliance requirements, and success measured by completed enrollments with low error and abandonment rates. These assumptions should be confirmed before implementation.

## 1. Welcome and eligibility

**Header:** logo, “Need help?”
**Progress:** Step 1 of 3

> **Let’s get you enrolled**
> It takes about 5 minutes. You can save and finish later.

- “Who is this enrollment for?” — Myself / Someone else
- “Where do you live?” — searchable location field
- “Date of birth” — accessible date input with example format
- Primary button: **Check eligibility**
- Secondary link: **Already started? Resume**

Design notes: one question group at a time on small screens; inline validation only after interaction; explain why sensitive information is needed. If ineligible, preserve dignity and offer a clear next step rather than a dead end.

## 2. Your details

**Progress:** Step 2 of 3 · autosaved

> **Tell us about you**
> We’ll use these details to create and protect your account.

- Legal name
- Email and mobile number
- Address, with manual-entry fallback
- Password or passkey setup
- Required consent in plain language, with links to full terms
- Buttons: **Continue** and **Back**

Design notes: group fields into “Identity,” “Contact,” and “Account security.” Keep labels persistent above inputs, support autofill, show password requirements before failure, and never rely on color alone for errors.

## 3. Review and submit

**Progress:** Step 3 of 3

> **Review your enrollment**
> Check everything before you submit.

- Summary cards for eligibility, personal details, and contact information
- **Edit** action beside each section, returning users to the relevant fields without losing progress
- Clear statement of what happens after submission
- Primary button: **Submit enrollment**
- Confirmation state: reference number, expected response time, next action, and email/SMS receipt

Design notes: disable submission only while processing, prevent duplicate submissions, and preserve entered data after recoverable failures.

Across all screens: use a single-column layout up to tablet width, a centered 640px form on desktop, 44px minimum touch targets, visible keyboard focus, semantic headings, screen-reader error summaries, and plain-language copy.

Before release, assign a decision owner and test the flow with representative users. Track start-to-completion rate, abandonment by field, validation errors, completion time, support contacts, and accessibility defects. Treat the three screens as a hypothesis to refine, not proof that onboarding is intuitive.
