from elements.button import Button
from pages.base_page import BasePage


class MainPage(BasePage):
    __LOCATOR_ALERTS_BUTTON = "(//*[contains(text(),'Alerts')]//ancestor::*)/*[contains(@class, 'card-up')]"
    __LOCATOR_ELEMENTS_BUTTON = "(//*[@id='app']//*[contains(text(), 'Elements')]//ancestor::*)/*[contains(@class, 'card-up')]"

    alerts_button = Button(__LOCATOR_ALERTS_BUTTON, "AlertsFrameWindowsButton")
    elements_button = Button(__LOCATOR_ELEMENTS_BUTTON, "ElementsButton")

    def __init__(self):
        super().__init__("//*[@class='home-content']", "MainPage")

    def click_alerts(self):
        self.alerts_button.scroll_to_element()
        self.alerts_button.click()

    def click_elements(self):
        self.elements_button.scroll_to_element()
        self.elements_button.click()
