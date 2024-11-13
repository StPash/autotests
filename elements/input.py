from elements.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def enter(self, text):
        self.find_element().send_keys(text)
