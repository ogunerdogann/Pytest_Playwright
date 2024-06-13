import pytest
import re
from playwright.sync_api import Page,expect


pytest_plugins = [  ]

def pytest_addoption(parser) -> None:
    parser.addoption(
        "--amazon_base_url",
        action = "store",
        default = "https://www.amazon.de/",
        help = "Amazon main page URL"
    )

@pytest.fixture(scope = "function")
def go_to_amazon_main_page(request, page:Page):
    page.goto(request.config.getoption("--amazon_base_url"))
    # Click the Akzeptieren(cookies) button
    button = page.locator("css=input[name='accept']")
    button.click()
    expect(page).to_have_title(re.compile("Günstige"))
