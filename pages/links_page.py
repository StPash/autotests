from pages.base_page import BasePage
from elements.button import Button


class LinksPage(BasePage):
    __LOCATOR_HOME_BUTTON = "//*[@id='simpleLink']"

    home_btn = Button(__LOCATOR_HOME_BUTTON, "HomeButton")

    def __init__(self):
        super().__init__("//*[@id='linkWrapper']", "LinksPage")

    def click_home(self):
        self.home_btn.click()
