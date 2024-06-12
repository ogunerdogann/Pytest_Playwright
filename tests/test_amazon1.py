import re 
import pytest
from playwright.sync_api import Page,expect
from amazon_mainPage import Amazon_MainPage

@pytest.mark.test1
def test_get_started_link(page:Page, go_to_amazon_main_page):
     
    # Expects page to have a heading with the name of installation
    expect(page.locator(Amazon_MainPage.AMAZON_LOGO)).to_be_visible()
    expect(page.locator(Amazon_MainPage.SEARCH_BOX)).to_be_visible()
    expect(page.get_by_role("link", name="Amazon Basics ")).to_be_visible()

    for i in range(0,len(Amazon_MainPage.NAVBAR)):
        page.wait_for_timeout(3000)
        expect(page.get_by_role("link", name=Amazon_MainPage.NAVBAR[i]).first).to_be_visible()
        