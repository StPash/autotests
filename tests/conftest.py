import pytest

from framework.driver import Driver
from framework.logger import Logger
from resources.config_manager import ConfigManager


@pytest.fixture(autouse=True)
def browser():
    driver = Driver()
    driver.maximize_window()
    driver.get(ConfigManager.get_config().url)

    yield

    Logger().info("Завершение тест-кейса\n")
    try:
        driver.quit()
    finally:
        Driver.del_instance()
