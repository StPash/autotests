import json
import os

from models.config_model import ConfigModel


class ConfigManager:
    _RESOURCES_ROOT = os.path.dirname(os.path.abspath(__file__))
    _CONFIG_FILE_PATH = os.path.join(_RESOURCES_ROOT, 'config_data.json')
    _TEST_USERS_FILE_PATH = os.path.join(_RESOURCES_ROOT, 'test_data.json')
    _EXPECTED_TEXTS_FILE_PATH = os.path.join(_RESOURCES_ROOT, 'expected_texts.json')

    _config = None

    @classmethod
    def load_json(cls, model, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if type(data) is list:
                return [model(**el) for el in data]
            else:
                return model(**data)

    @classmethod
    def get_config(cls):
        if cls._config is None:
            cls._config = cls.load_json(ConfigModel, cls._CONFIG_FILE_PATH)
        return cls._config

