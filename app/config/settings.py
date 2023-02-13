import os
from functools import lru_cache
from pydantic import BaseSettings, Field

ENV_FILE = '.env'


class Settings(BaseSettings):
    DEBUG: bool = Field(..., env="DEBUG")
    APP_NAME: str = "SimpleFormProcessorAPI"
    API_PREFIX: str = '/api'
    HOST: str = Field(..., env="HOST")
    PORT: int = Field(..., env="PORT")
    BASE_URL = '{}:{}'.format(HOST, str(PORT))

    class Config:
        env_file = ENV_FILE
        env_file_encoding = 'utf-8'
        case_sensitive: bool = True

        @classmethod
        def parse_env_var(cls, field_name: str, env_var: str) -> str:
            print(field_name)
            print(env_var)
            return ""


@lru_cache()
def get_settings():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path + "/" + ENV_FILE)
    settings = Settings(
        _env_file=f'{dir_path}/{ENV_FILE}',
        _env_file_encoding='utf-8',
    )
    return settings
