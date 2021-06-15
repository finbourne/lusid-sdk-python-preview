import json
import os
from pathlib import Path


class PersonalAccessTokenLoader:

    def __init__(self, config_keys_path=Path(__file__).parent.joinpath('config_keys.json')):
        self.__config_keys_path = config_keys_path
        self.__pat = self.__load_pat_from_env_var(self.__config_keys_path)

    def __load_pat_from_env_var(self, config_keys_path):

        with open(config_keys_path) as json_file:
            pat_env = json.load(json_file)["personal_access_token"]["env"]
        return os.getenv(pat_env)

    @property
    def pat(self):
        return self.__pat

    @pat.setter
    def pat(self, value):
        self.__pat = value
