from playwright.sync_api import sync_playwright, Playwright

'''
------------------ Page ------------------
Page provides methods to interact(TR- etkilesim kurmak) with a single tab in a Browser,
or an extension(TR- uzanti) background page in Chromium. One Browser instance might have 
multiple Page instance. This exapmle creates a Page, navigates to an URL, and then saves a screenshot.
'''

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.de/")
    page.screenshot(path="screenshot.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)