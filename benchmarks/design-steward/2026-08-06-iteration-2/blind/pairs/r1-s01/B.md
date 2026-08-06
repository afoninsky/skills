# Enrollment concept: “A clear path in, with no surprises”

Because the brief lacks users, evidence, ownership, constraints, and success criteria, this is a reversible concept—not a validated final design. I’m assuming a general consumer enrollment flow, mobile-first, with account creation and a small amount of profile data. Before implementation, assign a product owner and validate the assumptions with representative users.

## Screen 1 — Welcome and expectations

**Header:** Brand mark · “Sign in”

**Progress:** Step 1 of 3 · About 2 minutes

**Title:** Let’s get you enrolled

**Body:** Create your account, tell us the essentials, then review everything before submitting.

**What you’ll need:** Email address · Mobile number · Basic personal details

**Primary action:** Get started

**Secondary action:** I already have an account

**Trust note:** “Your information is encrypted and used only to manage your enrollment.” Link to privacy details without interrupting the flow.

## Screen 2 — Your details

**Progress:** Step 2 of 3

**Title:** Tell us about you

Fields appear in one readable column: legal name, date of birth, email, and mobile number. Labels remain visible above inputs; examples clarify formatting. Required fields are explicitly marked.

Validate after the user leaves a field, preserve every valid entry, and place a specific correction beside the problem: “Enter a date in DD/MM/YYYY format.” Do not rely on color alone. Offer **Save and continue later** if account persistence is supported.

**Primary action:** Continue to review

**Secondary action:** Back

## Screen 3 — Review and submit

**Progress:** Step 3 of 3

**Title:** Check your enrollment

Group answers into scannable cards—Account and Personal details—with an **Edit** action beside each group. Show any consent as plain-language, unticked choices; separate required consent from optional communications.

**Primary action:** Submit enrollment

**Secondary action:** Back

After submission, replace the button with a clear confirmation, reference number, expected next step, timing, and support route. Prevent duplicate submissions.

## Responsive and quality bar

On mobile, use a single column, 44px minimum touch targets, sticky bottom actions, and an on-screen step label. On larger screens, keep the form narrow (about 640px); use spare space for reassurance, not extra fields. Preserve data across navigation, support keyboard and screen-reader use, and announce errors and progress.

Measure completion rate, abandonment by step, validation-error rate, time to complete, support contacts, and successful return after interruption. Test the riskiest assumptions with 5–8 target users before committing visual polish or engineering scope.
