import pytest
import re
from playwright.sync_api import Page,expect


pytest_plugins = [ 
     "D:\Pytest_Playwright\conftest.py"
 ]

def pytest_addoption(parser) -> None:
    parser.addoption(
        "--amazon_base_url",
        action = "store",
        default = "https://www.amazon.de/",
        help = "Amazon main page URL"
    )

@pytest.fixture()
def ui_fixture(request, page:Page):
    page.goto(request.config.getoption("--amazon_base_url"))
    # Click the Akzeptieren(cookies) button
    button = page.locator("css=input[name='accept']")
    button.click()
    expect(page).to_have_title(re.compile("Günstige"))
    

def pytest_runtest_setup(item):
    '''
    This hook checks each test before it runs.
    If the test has the UI mark, it appends the ui_fixture to the list of fixtures to be used for that test.   
    '''
    # Check if the test has the 'UI' mark
    if 'UI' in item.keywords:
        # Dynamically add the UI fixture
        item.fixturenames.append('ui_fixture')
        
