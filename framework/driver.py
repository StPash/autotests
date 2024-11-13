from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from framework.singleton import Singleton
from resources.config_manager import ConfigManager


class Driver(metaclass=Singleton):
    def __new__(cls):
        return cls.create_driver()

    @classmethod
    def wait(cls):
        return WebDriverWait(Driver(), ConfigManager.get_config().timeout)

    @classmethod
    def create_driver(cls):
        browser = ConfigManager.get_config().browser.lower()
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--lang=en')
            options.add_argument('--incognito')
            return webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("-private")
            options.set_preference("intl.accept_languages", "en")
            return webdriver.Firefox(options=options)
