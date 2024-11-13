from pages.base_page import BasePage
from elements.button import Button


class NavigationMenuPage(BasePage):
    def __init__(self):
        super().__init__("//*[contains(@class, 'accordion')]", "NavigationMenuPage")

    __LOCATOR_ALERTS_BUTTON = "//*[contains(@class, 'element-list')]//*[contains(text(),'Alerts')]"
    __LOCATOR_NESTED_BUTTON = "//*[contains(text(),'Nested')]"
    __LOCATOR_FRAMES_BUTTON = "//*[text()='Frames']"
    __LOCATOR_BROWSER_BUTTON = "//*[contains(text(), 'Browser')]"
    __LOCATOR_ELEMENTS_BUTTON = "//*[contains(@class, 'element-group')]//*[contains(text(), 'Elements')]"
    __LOCATOR_LINKS_BUTTON = "//*[contains(@class, 'element-group')]//*[text()='Links']"
    __LOCATOR_WEB_TABLES_BUTTON = "//*[contains(text(), 'Tables')]"

    alerts_button = Button(__LOCATOR_ALERTS_BUTTON, "AlertsButton")
    nested_button = Button(__LOCATOR_NESTED_BUTTON, "NestedFramesButton")
    frames_button = Button(__LOCATOR_FRAMES_BUTTON, "FramesButton")
    browser_windows_btn = Button(__LOCATOR_BROWSER_BUTTON, "BrowserWindowsButton")
    elements_btn = Button(__LOCATOR_ELEMENTS_BUTTON, "ElementsButton")
    links_btn = Button(__LOCATOR_LINKS_BUTTON, "LinksButton")
    web_tables_button = Button(__LOCATOR_WEB_TABLES_BUTTON, "WebTablesButton")

    def click_alerts(self):
        self.alerts_button.click()

    def click_nested_frames(self):
        self.nested_button.scroll_to_element()
        self.nested_button.click()

    def click_frames(self):
        self.frames_button.click()

    def click_browser_windows(self):
        self.browser_windows_btn.click()

    def click_elements(self):
        self.elements_btn.click()

    def click_links(self):
        self.links_btn.click()

    def click_web_tables(self):
        self.web_tables_button.click()
