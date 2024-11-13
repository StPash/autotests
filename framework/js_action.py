import os

from framework.driver import Driver


class ActionJS:
    @classmethod
    def execute_script_from_file(cls, script_path, *args):
        with open(script_path, 'r') as file:
            script = file.read()
        Driver().execute_script(script, *args)

    @classmethod
    def scroll_to_element(cls, element):
        _PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        script_path = os.path.join(_PROJECT_ROOT, 'scripts/scrollToElement.js')
        cls.execute_script_from_file(script_path, element)
