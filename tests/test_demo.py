import pytest

from framework.browser_handler import BrowserHandler
from framework.logger import Logger
from models.expected_texts import ExpectedTexts
from models.user_model import UserModel
from pages.alerts_page import AlertsPage
from pages.browser_windows_page import BrowserWindowsPage
from pages.elements_page import ElementsPage
from pages.frames_page import FramesPage
from pages.links_page import LinksPage
from pages.main_page import MainPage
from pages.navigation_menu_page import NavigationMenuPage
from pages.nested_frames_page import NestedFramesPage
from resources.config_manager import ConfigManager
from pages.simple_page import SamplePage
from utils.generate_string import generate_string


class TestCaseAlerts:
    def test_simple_confirm_prompt_alerts(self):
        Logger().info("Тест-кейс по работе с алертами")
        expected_texts = ConfigManager.load_json(ExpectedTexts, ConfigManager._EXPECTED_TEXTS_FILE_PATH)
        main_page = MainPage()
        assert main_page.is_displayed(), f'страница {main_page.name} не отображена'

        main_page.click_alerts()
        nav_menu = NavigationMenuPage()
        nav_menu.click_alerts()
        alerts_page = AlertsPage()
        assert alerts_page.is_displayed(), 'форма Alerts не отображена'

        alerts_page.click_see_alert()
        assert BrowserHandler.is_alert(), 'оповещение не открыто'
        assert expected_texts.simple_alert in BrowserHandler.get_present_alert().text, \
            f'Не отображен текст {expected_texts.simple_alert}'

        BrowserHandler.alert_accept()
        assert not BrowserHandler.is_alert(), 'оповещение не закрыто'

        alerts_page.click_confirm_box()
        assert BrowserHandler.is_alert(), 'оповещение не открыто'
        assert expected_texts.confirm_alert in BrowserHandler.get_present_alert().text, \
            f'Не отображен текст {expected_texts.confirm_alert}'

        BrowserHandler.alert_accept()
        assert not BrowserHandler.is_alert(), 'оповещение не закрыто'
        assert alerts_page.is_displayed_confirm_result(), 'не отображена надпись результата работы в оповещении подтверждения'
        assert expected_texts.confirm_result_ok in alerts_page.get_confirm_result_text(), \
            f'надпись не соответствует ожидаемой "{expected_texts.confirm_result}"'

        alerts_page.click_prompt_box()
        assert BrowserHandler.is_alert(), 'оповещение не открыто'
        alert = BrowserHandler.get_present_alert()
        assert expected_texts.prompt_alert in alert.text, f'Не отображен текст {expected_texts.prompt_alert}'

        input_text = generate_string()
        Logger().info(f'Ввод текста "{input_text}" в окне оповещения')
        alert.send_keys(input_text)
        BrowserHandler.alert_accept()
        assert not BrowserHandler.is_alert(), 'оповещение не закрыто'
        assert alerts_page.is_displayed_prompt_result(), 'не отображена надпись результата работы в оповещении запроса'
        assert input_text in alerts_page.get_prompt_result_text(), f'надпись не соответствует ожидаемой "{input_text}"'


class TestCaseIframe:
    def test_switching_between_frames(self):
        Logger().info("Тест-кейс по работе с фреймами")
        main_page = MainPage()
        assert main_page.is_displayed(), f'страница {main_page.name} не отображена'

        main_page.click_alerts()
        nav_menu = NavigationMenuPage()
        nav_menu.click_nested_frames()
        nested_frames_page = NestedFramesPage()
        nested_frames_page.is_displayed(), 'форма Nested Frames не отображена'
        assert nested_frames_page.have_parent_child_frame_text(), 'Отсутствуют надписи "Parent frame" и "Child Iframe"'

        nav_menu.click_frames()
        frames_page = FramesPage()
        assert frames_page.is_displayed(), 'форма Frames не отображена'
        assert frames_page.get_frame1_text() == frames_page.get_frame2_text(), 'Надписи из фреймов не соответствуют друг другу'


@pytest.mark.parametrize("user", ConfigManager.load_json(UserModel, ConfigManager._TEST_USERS_FILE_PATH))
class TestCaseTables:
    def test_work_with_tables(self, user):
        Logger().info("Тест-кейс по работе с веб-таблицей")
        main_page = MainPage()
        assert main_page.is_displayed(), f'страница {main_page.name} не отображена'

        main_page.click_elements()
        nav_menu = NavigationMenuPage()

        nav_menu.click_web_tables()
        elements_page = ElementsPage()
        assert elements_page.is_displayed(), 'форма Web Tables не отображена'
        elements_page.is_displayed_registration_form()

        elements_page.click_add()
        assert elements_page.is_displayed_registration_form(), 'форма Registration Form не отображена'

        Logger().info("Ввод данных пользователя")
        elements_page.enter_user(user)
        elements_page.click_submit()
        assert elements_page.is_closed_registration_form(), 'форма Registration Form не закрыта'
        assert elements_page.is_userdata_in_table(user), "В таблице отсутствуют введенные данные пользователя"

        table_rows_number = elements_page.get_records_number()
        elements_page.clik_delete_user_data(user)
        assert table_rows_number != elements_page.get_records_number(), "В таблице не изменилось количество пользователей"
        assert not elements_page.is_userdata_in_table(user), "Введенные данные пользователя не удалены"


class TestCaseHandles:
    def test_simple_confirm_prompt_alerts(self):
        Logger().info("Тест-кейс по работе с вкладками")
        main_page = MainPage()
        assert main_page.is_displayed(), f'страница {main_page.name} не отображена'

        main_page.click_alerts()
        nav_menu = NavigationMenuPage()
        nav_menu.click_browser_windows()
        browser_windows_page = BrowserWindowsPage()
        assert browser_windows_page.is_displayed(), 'форма Browser Windows не отображена'

        BrowserHandler.fix_windows_set()
        browser_windows_page.click_new_tab()
        BrowserHandler.switch_next_window()
        sample_page = SamplePage()
        assert sample_page.is_displayed(), f'страница {sample_page.name} не отображена'

        BrowserHandler.close_widow()
        assert browser_windows_page.is_displayed(), 'форма Browser Windows не отображена'

        nav_menu.click_elements()
        nav_menu.click_links()
        links_page = LinksPage()
        assert links_page.is_displayed(), 'форма Links не отображена'

        BrowserHandler.fix_windows_set()
        links_page.click_home()
        BrowserHandler.switch_next_window()
        assert main_page.is_displayed(), f'страница {main_page.name} не отображена'

        BrowserHandler.switch_previous_window()
        assert links_page.is_displayed(), 'форма Links не отображена'

