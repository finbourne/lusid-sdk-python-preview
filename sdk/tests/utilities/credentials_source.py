from pathlib import Path
import json


class CredentialsSource:

    @classmethod
    def secrets_path(cls) -> Path:
        return Path(__file__).parent.parent.joinpath('secrets.json')

    @classmethod
    def config_keys_path(cls) -> Path:
        return Path(__file__).parent.parent.parent.joinpath('lusid/utilities/config_keys.json')

    @classmethod
    def fetch_config_keys(cls):
        with open(cls.config_keys_path()) as config_key_file:
            config_keys = json.load(config_key_file)
        return config_keys