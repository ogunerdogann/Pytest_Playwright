from playwright.sync_api import Page,expect, Locator
from amazon_mainPage import Amazon_MainPage, Search_Words
import pytest

class Amazon_MainPageTests:

   button = 'hello'
   
@pytest.mark.test1
def test_get_started_link(page:Page, go_to_amazon_main_page):
   
    #deneme = "css=[type='submit']"
    # Expects page to have a heading with the name of installation
    expect(page.locator(Amazon_MainPage.AMAZON_LOGO)).to_be_visible()
    expect(page.locator(Amazon_MainPage.SEARCH_BOX)).to_be_visible()
    expect(page.get_by_role("link", name="Amazon Basics ")).to_be_visible()

    for i in range(0,len(Amazon_MainPage.NAVBAR)):
        expect(page.get_by_role("link", name=Amazon_MainPage.NAVBAR[i]).first).to_be_visible()

@pytest.mark.test2       
def test_nutella(page:Page, go_to_amazon_main_page):
    search_word = ""
    for i in range(1,len(list(Search_Words))+1):
        search_word = Search_Words(i).name
        page.locator(Amazon_MainPage.SEARCH_BOX).fill(search_word)
        page.locator(Amazon_MainPage.SEARCH_SUBMIT_BUTTON).click()
        page.wait_for_timeout(5000)
        expect(page.locator(Amazon_MainPage.SEARCH_WORD)).to_contain_text(search_word)
    
@pytest.mark.test3
def test_footer(page:Page, go_to_amazon_main_page):
    
    page.mouse.wheel(0,13188)
    page.wait_for_timeout(5000)
    for i in range(0,12):
        expect(page.locator(Amazon_MainPage.FOOTER_ELEMENT).nth(i)).to_be_visible()

        