from playwright.sync_api import Page,Locator

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
    def __init__(self, page: Page, parent: Locator, testid: str) -> None:
        locator = parent.get_by_test_id(testid)
        super().__init__(page, locator)

    def click(self) -> None:
        """
        Clicks on the relevant button
        """
        self.root.click()

    def wait_until_visible(self,timeout: 5000) -> None:
        """
        Waits until the relevant button is visible.
        Default waiting time = 5 seconds
        """
        self.root.wait_for(timeout=timeout, state='visible')


