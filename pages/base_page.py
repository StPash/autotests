from elements.button import Button
from framework.logger import Logger


class BasePage:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def is_displayed(self):
        Logger().info(f"Открытие страницы {self.name}")
        return Button(self.locator, self.name).find_element().is_displayed()
