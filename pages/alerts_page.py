from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class AlertsPage(BasePage):
    __LOCATOR_ALERTS_FORM = "//*[@id='javascriptAlertsWrapper']"

    __LOCATOR_SEE_ALERT_BUTTON = "//*[@id='alertButton']"
    __LOCATOR_CONFIRM_BOX_BUTTON = "//*[@id='confirmButton']"
    __LOCATOR_PROMPT_BOX_BUTTON = "//*[@id='promtButton']"

    __LOCATOR_CONFIRM_BOX_RESULT = "//*[@id='confirmResult']"
    __LOCATOR_PROMPT_BOX_RESULT = "//*[@id='promptResult']"

    alerts_see_button = Button(__LOCATOR_SEE_ALERT_BUTTON, "AlertsSeeButton")
    confirm_box_button = Button(__LOCATOR_CONFIRM_BOX_BUTTON, "ConfirmBoxButton")
    prompt_box_button = Button(__LOCATOR_PROMPT_BOX_BUTTON, "PromptBoxButton")

    result_confirm_box = Text(__LOCATOR_CONFIRM_BOX_RESULT, "ResultConfirmBox")
    result_prompt_box = Text(__LOCATOR_PROMPT_BOX_RESULT, "ResultPromptBox")

    def __init__(self):
        super().__init__(self.__LOCATOR_ALERTS_FORM, "AlertPage")

    def click_see_alert(self):
        self.alerts_see_button.click()

    def click_confirm_box(self):
        self.confirm_box_button.click()

    def click_prompt_box(self):
        self.prompt_box_button.click()

    def is_displayed_confirm_result(self):
        return self.result_confirm_box.is_displayed()

    def get_confirm_result_text(self):
        return self.result_confirm_box.text()

    def is_displayed_prompt_result(self):
        return self.result_prompt_box.is_displayed()

    def get_prompt_result_text(self):
        return self.result_prompt_box.text()
