import re 
from playwright.sync_api import Page,expect

amazon_url = "https://www.amazon.de/"
def test_has_title(page:Page):
    page.goto(amazon_url)

    # Expect a title "to contain" a substring
    expect(page).to_have_title(re.compile("Günstige"))

def test_get_started_link(page:Page):
    page.goto(amazon_url)

    # Click the Akzeptieren(cookies) button
    page.locator("css=input[name='accept']").click()
    
    # Expects page to have a heading with the name of installation
    expect(page.locator("css=#nav-logo-sprites")).to_be_visible()

    