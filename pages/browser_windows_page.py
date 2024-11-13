from pages.base_page import BasePage
from elements.button import Button


class BrowserWindowsPage(BasePage):
    __LOCATOR_NEW_TAB_BUTTON = "//*[@id='tabButton']"

    new_tab_btn = Button(__LOCATOR_NEW_TAB_BUTTON, "NewTabButton")

    def __init__(self):
        super().__init__("//*[@id='browserWindows']", "BrowserWindowsPage")

    def click_new_tab(self):
        self.new_tab_btn.click()
