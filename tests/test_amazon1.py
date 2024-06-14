from playwright.sync_api import Page,expect
from amazon_mainPage import Amazon_MainPage, Search_Words
import pytest

class Amazon_MainPageTests:

  "If I delete this line then an error appear on line 9. IDK why for now"
   
@pytest.mark.UI
@pytest.mark.test1
def test_get_started_link(page:Page):
   
    #deneme = "css=[type='submit']"
    
    # Expects page to have a heading with the name of installation
    page.wait_for_timeout(1000)
    expect(page.locator(Amazon_MainPage.AMAZON_LOGO)).to_be_visible()
    expect(page.locator(Amazon_MainPage.SEARCH_BOX)).to_be_visible()
    expect(page.get_by_role("link", name="Amazon Basics ")).to_be_visible()

    for i in range(0,len(Amazon_MainPage.NAVBAR)):
        expect(page.get_by_role("link", name=Amazon_MainPage.NAVBAR[i]).first).to_be_visible()

@pytest.mark.UI
@pytest.mark.test2       
def test_nutella(page:Page):
    search_word = ""
    for i in range(1,len(list(Search_Words))+1):
        search_word = Search_Words(i).name
        #page.pause()
        page.locator(Amazon_MainPage.SEARCH_BOX).fill(search_word)
        page.locator(Amazon_MainPage.SEARCH_SUBMIT_BUTTON).click()
        page.wait_for_timeout(5000)
        expect(page.locator(Amazon_MainPage.SEARCH_WORD)).to_contain_text(search_word)
    
@pytest.mark.UI
@pytest.mark.test3
def test_footer(page:Page):
    
    page.mouse.wheel(0,13188)      
    # x,y (horizontal-vertical) coordinats of an element.
    # You can get this values under Inspect->Styles
    page.wait_for_timeout(5000)
    for i in range(0,12):
        expect(page.locator(Amazon_MainPage.FOOTER_ELEMENT).nth(i)).to_be_visible()
        # if there are too many elements with same class, id etc.
        # you can locate just one of them and nth(<index>) will get the rest. 

        