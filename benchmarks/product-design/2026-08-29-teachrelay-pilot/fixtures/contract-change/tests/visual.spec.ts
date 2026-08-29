import { expect, test } from "@playwright/test";

test("home default", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveScreenshot("home-default.png");
});
