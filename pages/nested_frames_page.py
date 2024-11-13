from selenium.common import TimeoutException

from elements.text import Text
from framework.browser_handler import BrowserHandler
from pages.base_page import BasePage


class NestedFramesPage(BasePage):

    __LOCATOR_PARENT_FRAME = "//*[@id='frame1']"
    __LOCATOR_PARENT_TEXT = "//*[contains(text(),'Parent frame')]"
    __LOCATOR_CHILD_FRAME = "//iframe"
    __LOCATOR_CHILD_TEXT = "//*[contains(text(),'Child Iframe')]"

    parent_text = Text(__LOCATOR_PARENT_TEXT, "ParentFrameText")
    child_text = Text(__LOCATOR_CHILD_TEXT, "ChildFrameText")

    def __init__(self):
        super().__init__("//*[@id='framesWrapper']//*[text()='Nested Frames']", "NestedFramesPage")

    def have_parent_child_frame_text(self):
        BrowserHandler.switch_to_frame(self.__LOCATOR_PARENT_FRAME)
        try:
            self.parent_text.find_element()
            BrowserHandler.switch_to_frame(self.__LOCATOR_CHILD_FRAME)
            try:
                self.child_text.find_element()
                BrowserHandler.switch_to_default_content()
                return True
            except TimeoutException:
                return False
        except TimeoutException:
            return False

    def get_child_frame_text(self):
        BrowserHandler.switch_to_frame(self.__LOCATOR_CHILD_FRAME)
        text = self.child_text.text()
        BrowserHandler.switch_to_default_content()
        return text
