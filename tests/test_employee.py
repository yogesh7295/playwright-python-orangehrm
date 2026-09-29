from playwright.sync_api import sync_playwright


def test_employee_list_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open OrangeHRM
        page.goto("https://opensource-demo.orangehrmlive.com/")

        # Login
        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        page.get_by_role("button", name="Login").click()

        # Navigate to PIM
        page.get_by_text("PIM", exact=True).click(no_wait_after=True)

        # Wait for PIM page
        page.wait_for_url("**/pim/viewEmployeeList", timeout=15000)

        # Verify Employee List page
        assert "viewEmployeeList" in page.url

        browser.close()