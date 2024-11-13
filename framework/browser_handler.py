from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from framework.driver import Driver
from framework.logger import Logger


class BrowserHandler:
    _windows_set = set()

    @classmethod
    def is_alert(cls):
        try:
            Driver.wait().until(lambda d: d.switch_to.alert)
            Logger().info("Появление оповещения")
            return True
        except NoAlertPresentException:
            return False

    @classmethod
    def get_present_alert(cls):
        return Driver.wait().until(lambda d: d.switch_to.alert)

    @classmethod
    def alert_accept(cls):
        Logger().info('Клик по кнопке "ОК" в окне оповещения')
        BrowserHandler.get_present_alert().accept()

    @classmethod
    def switch_to_frame(cls, locator):
        iframe = Driver().find_element(By.XPATH, locator)
        Driver().switch_to.frame(iframe)

    @classmethod
    def switch_to_default_content(cls):
        Driver().switch_to.default_content()

    @classmethod
    def fix_windows_set(cls):
        cls._windows_set = set(Driver().window_handles)

    @classmethod
    def switch_next_window(cls):
        Logger().info("Переключение на новую вкладку")
        Driver.wait().until(EC.number_of_windows_to_be(len(cls._windows_set) + 1))
        new_window = set(Driver().window_handles) - cls._windows_set
        Driver().switch_to.window(new_window.pop())

    @classmethod
    def switch_previous_window(cls):
        Logger().info("Переключение на предыдущую вкладку")
        windows = Driver().window_handles
        Driver().switch_to.window(windows[cls.get_index_window() - 1])

    @classmethod
    def close_widow(cls):
        Logger().info("Закрытие вкладки")
        windows = Driver().window_handles
        index = cls.get_index_window()
        Driver().close()
        windows.pop(index)
        if windows and index:
            Driver().switch_to.window(windows[index - 1])
        elif not windows:
            Driver().quit()
        else:
            Driver().switch_to.window(windows[0])

    @classmethod
    def get_index_window(cls):
        windows = Driver().window_handles
        now_window = Driver().current_window_handle
        return windows.index(now_window)
