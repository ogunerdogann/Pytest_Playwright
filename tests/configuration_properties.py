from playwright.sync_api import Page,expect
import pytest
import re



@pytest.fixture(scope="function")
def go_to_amazon(page:Page):
    page.goto("https://www.amazon.de/")
    # Click the Akzeptieren(cookies) button
    button = page.locator("css=input[name='accept']")
    button.click()
    expect(page).to_have_title(re.compile("Günstige"))

@pytest.fixture(scope="function")
def negative_login(page:Page):
    print("second fixture")
    button = page.locator("css=[id='nav-link-accountList']")
    button.hover()
    button.click()
    expect(page).to_have_title("Amazon Anmelden")

    