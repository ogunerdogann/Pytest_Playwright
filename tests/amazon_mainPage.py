from enum import Enum,auto


class Amazon_MainPage:

    AMAZON_LOGO = "a[aria-label='Amazon.de']"
    SEARCH_BOX = "input[id='twotabsearchtextbox']"
    SEARCH_SUBMIT_BUTTON = "input[id='nav-search-submit-button']"
    SEARCH_WORD = "div[class='sg-col-inner']>div>span[class='a-color-state a-text-bold']"
    NAVBAR = ["Amazon Basics ",
              "Neuerscheinungen ",
              "Musik",
              "Prime Video",
              "Shopping-Tipps",
              "Bücher",
              "Mode",
              "Gutscheine",
              "Lebensmittel",
              "Küche, Haushalt & Wohnen"]
    PRIME_STUDENT_TEXT = "a[aria-label='Student']"
    FOOTER_ELEMENT = "td.navFooterDescItem"     
    HALLO_ANMELDEN = "#nav-link-accountList-nav-line-1"
    ANMELDEN_BUTTON = "span[class='nav-action-inner']"

class Search_Words(Enum):
    
    '''
    A wonderful using of Enums in Python. You can just give
    the first value(int or str<letter>), auto() will assign 
    the rest values automaticly.  
    '''
    
    NUTELLA = 1
    DORITOS = auto()
    BOUNTY = auto()
    MILKA = auto()
    PEPSI = auto()
    MANGO = auto()
    MORITZ_FIEGE = auto() 
    
