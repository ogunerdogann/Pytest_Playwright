from playwright.sync_api import Page,expect
import pytest
import re



@pytest.fixture(scope="function", name="go_to_amazon", autouse=True)
def go_to_amazon(page:Page):
    page.goto("https://www.amazon.de/")
    # Click the Akzeptieren(cookies) button
    page.locator("css=input[name='accept']").click(timeout=3000)
    expect(page).to_have_title(re.compile("Günstige"))

@pytest.fixture(scope="function", name="negative_login", autouse=True)
def negative_login(page:Page):
    print("second fixture")
    page.locator("css=[id='nav-link-accountList']").hover(timeout=2000)
    page.locator(page.get_by_text("Anmelden")).click(timeout=2000)
    expect(page).to_have_title("Amazon Anmelden")

    