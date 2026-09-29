from playwright.sync_api import sync_playwright


def test_open_orangehrm():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/")
        
        print("Page Title:", page.title())

        browser.close()