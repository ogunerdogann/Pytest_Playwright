import pytest
from playwright.sync_api import Page,expect

@pytest.fixture(scope = "function", autouse=True)
def before_each_after_each(page:Page):

    print("before the test runs")

    # Go to the starting URL before each test
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")

def test_main_navigation(page:Page):
    # Assertions use the expect API
    expect(page).to_have_url("https://playwright.dev/")

'''
You can use various fixtures to execute code before or after your tests and to share objects between them.
A function scoped fixture e.g. with autouse behaves like a beforeEach/afterEach.
And a module scoped fixture with autouse behaves like a beforeAll/afterAll which runs before all and after all the tests.
'''
#deneme 