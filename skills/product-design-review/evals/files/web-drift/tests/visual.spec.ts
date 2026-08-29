import { expect, test } from '@playwright/test';

test('accepted home', async ({ page }) => {
  await page.goto('/home?fixture=accepted');
  await expect(page).toHaveScreenshot('home-default.png');
});

test('mobile error evidence', async ({ page }, testInfo) => {
  await page.goto('/home?fixture=error');
  const image = await page.screenshot();
  await testInfo.attach('mobile-error', { body: image, contentType: 'image/png' });
});

