from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from framework.driver import Driver
from framework.js_action import ActionJS
from framework.logger import Logger


class BaseElement:
    def __init__(self, locator, name):
        self.__locator = locator
        self.__name = name

    def find_element(self):
        return Driver.wait().until(EC.presence_of_element_located((By.XPATH, self.__locator)))

    def find_clickable_element(self):
        return Driver.wait().until(EC.element_to_be_clickable((By.XPATH, self.__locator)))

    def click(self):
        Logger().info(f"Клик по элементу {self.__name}")
        self.find_clickable_element().click()

    def is_displayed(self):
        return self.find_element().is_displayed()

    def find_elements(self):
        return Driver.wait().until(EC.presence_of_all_elements_located((By.XPATH, self.__locator)))

    def scroll_to_element(self):
        ActionJS.scroll_to_element(self.find_element())

    def find_child_element(self, locator):
        return self.find_element().find_element(By.XPATH, '.' + locator)

    def find_child_elements(self, locator):
        return self.find_element().find_elements(By.XPATH, '.' + locator)
