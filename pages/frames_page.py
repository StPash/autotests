from elements.text import Text
from framework.browser_handler import BrowserHandler
from pages.base_page import BasePage


class FramesPage(BasePage):
    __LOCATOR_FRAME1 = "//*[@id='frame1']"
    __LOCATOR_FRAME2 = "//*[@id='frame2']"
    __LOCATOR_FRAME_TEXT = "//*[@id='sampleHeading']"

    frame_text = Text(__LOCATOR_FRAME_TEXT, "FrameText")

    def __init__(self):
        super().__init__("//*[@id='framesWrapper']//*[text()='Frames']", "FramesPage")

    def get_frame1_text(self):
        BrowserHandler.switch_to_frame(self.__LOCATOR_FRAME1)
        text = self.frame_text.text()
        BrowserHandler.switch_to_default_content()
        return text

    def get_frame2_text(self):
        BrowserHandler.switch_to_frame(self.__LOCATOR_FRAME2)
        text = self.frame_text.text()
        BrowserHandler.switch_to_default_content()
        return text
