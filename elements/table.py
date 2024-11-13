from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from elements.text import Text
from models.user_model import UserModel


class Table(BaseElement):
    __LOCATOR_TABLE_FIELDS = "//*[ contains(@role, 'columnheader')]"
    __LOCATOR_TABLE_BODY = "//*[contains(@class, 'tbody')]"

    __CHILD_LOCATOR_TABLE_RECORDS = "//*[not(contains(@class, 'padRow')) and @role = 'row']"
    __CHILD_LOCATOR_ROW_COLUMNS = ".//*[contains(@class, 'rt-td')]"

    table_body = Text(__LOCATOR_TABLE_BODY, "TableBody")

    def __init__(self, locator, name):
        super().__init__(locator, name)
        self.fields = []
        self.records = []

    def get_records_number(self):
        if not self.records:
            self.get_records()
        return len(self.records)

    def is_user_in_table(self, user):
        if not self.records:
            self.get_records()
        for record in self.records:
            if record == user:
                return True

    def get_records(self):
        for record in self.table_body.find_child_elements(self.__CHILD_LOCATOR_TABLE_RECORDS):
            record_fields = [el.text for el in record.find_elements(By.XPATH, self.__CHILD_LOCATOR_ROW_COLUMNS)]
            self.records.append(UserModel(**dict(zip(self.get_fields(), record_fields))))

    def get_fields(self):
        if not self.fields:
            self.fields = [field.text.lower().strip().replace(' ', '_') for field in
                           Text(self.__LOCATOR_TABLE_FIELDS, "fields").find_elements()]
            self.fields.pop()
        return self.fields

    def refresh_data(self):
        self.records = []
        self.get_records()

    def get_user_record_number(self, user):
        for i in range(len(self.records)):
            if user == self.records[i]:
                return i + 1
