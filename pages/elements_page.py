from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from elements.table import Table
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from framework.driver import Driver


class ElementsPage(BasePage):
    def __init__(self):
        super().__init__("//*[contains(@class, 'web-tables')]", "ElementsPage")

    __LOCATOR_ADD_BUTTON = "//*[@id='addNewRecordButton']"

    __LOCATOR_REGISTRATION_FORM_HEADER = "//*[@id='registration-form-modal']"
    __LOCATOR_FIRST_NAME_INPUT = "//*[@id='firstName']"
    __LOCATOR_LAST_NAME_INPUT = "//*[@id='lastName']"
    __LOCATOR_EMAIL_INPUT = "//*[@id='userEmail']"
    __LOCATOR_AGE_INPUT = "//*[@id='age']"
    __LOCATOR_SALARY_INPUT = "//*[@id='salary']"
    __LOCATOR_DEPARTMENT_INPUT = "//*[@id='department']"
    __LOCATOR_SUBMIT = "//*[@id='submit']"

    __LOCATOR_TABLE = "//*[contains(@class, 'ReactTable')]"
    __CHILD_LOCATOR_DEL_ROW_BTN = "//*[contains(@id, 'delete')]"

    add_button = Button(__LOCATOR_ADD_BUTTON, "AddButton")
    form_header = Button(__LOCATOR_REGISTRATION_FORM_HEADER, "HeaderRegistrationForm")
    name_input = Input(__LOCATOR_FIRST_NAME_INPUT, "FirstNameInput")
    last_name_input = Input(__LOCATOR_LAST_NAME_INPUT, "LastNameInput")
    email_input = Input(__LOCATOR_EMAIL_INPUT, "EmailInput")
    age_input = Input(__LOCATOR_AGE_INPUT, "AgeInput")
    salary_input = Input(__LOCATOR_SALARY_INPUT, "SalaryInput")
    department_input = Input(__LOCATOR_DEPARTMENT_INPUT, "DepartmentInput")
    submit_button = Button(__LOCATOR_SUBMIT, "SubmitButton")
    users_table = Table(__LOCATOR_TABLE, "UsersTable")

    def click_add(self):
        self.add_button.click()

    def is_displayed_registration_form(self):
        try:
            self.form_header.is_displayed()
            return True
        except TimeoutException:
            return False

    def is_closed_registration_form(self):
        try:
            Driver.wait().until(EC.element_to_be_clickable((By.XPATH, self.__LOCATOR_ADD_BUTTON)))
            return True
        except TimeoutException:
            return False

    def enter_user(self, user):
        self.name_input.enter(user.first_name)
        self.last_name_input.enter(user.last_name)
        self.email_input.enter(user.email)
        self.age_input.enter(user.age)
        self.salary_input.enter(user.salary)
        self.department_input.enter(user.department)

    def click_submit(self):
        self.submit_button.click()

    def is_userdata_in_table(self, user):
        self.users_table.refresh_data()
        return self.users_table.is_user_in_table(user)

    def clik_delete_user_data(self, user):
        i = self.users_table.get_user_record_number(user)
        self.users_table.table_body.find_child_element(f'/*[{i}]' + self.__CHILD_LOCATOR_DEL_ROW_BTN).click()
        self.users_table.refresh_data()

    def get_records_number(self):
        return self.users_table.get_records_number()
