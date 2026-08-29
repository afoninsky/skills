import { expect, test } from '@playwright/test';

test('accepted goal card remains stable', async ({ page }) => {
  await page.goto('/fixtures/goal-card?state=default');
  await expect(page).toHaveScreenshot('goal-card-default.png');
});

