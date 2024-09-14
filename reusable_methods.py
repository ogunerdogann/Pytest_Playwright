from playwright.sync_api import Page,Locator


def go_to_main_page():
    """"""

class _RootComponent:
    """
    Root Component Class
    """
    def __init__(self, page: Page, locator: Locator) -> None:
        
        self.root = locator
        self.page = page

    def is_visible(self, timeout: float = 5000) ->bool:
        """
        Returns True if root Component is visible, False otherwise 
        """
        return self.root.is_visible(timeout=timeout)
    
    def is_hidden(self) ->bool:
        """
        Returns True if root Component is hidden, False otherwise
        """
        return self.root.is_hidden()
    
class UnitActionButton(_RootComponent):
    """
    This class decribes the behavior of a button
    """
    
    def __init__(self, page: Page, parent: Locator, test_id: str) -> None:
        locator = parent.get_by_test_id(test_id)
        super().__init__(page=page, locator=locator)

    def click(self) -> None:
        """
        Clicks on the relevant button
        """
        self.root.click()

    def get_title(self) -> str:
        """Returns the title of a button"""
        title = self.root.text_content()
        return title if title is not None else ""

    def wait_until_visible(self,timeout: 5000) -> None:
        """
        Waits until the relevant button is visible.
        Default waiting time = 5 seconds
        """
        self.root.wait_for(timeout=timeout, state='visible')


