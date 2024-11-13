from elements.base_element import BaseElement


class Text(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def text(self):
        return self.find_element().text
