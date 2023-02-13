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
    BASE_URL: str = '{}:{}'.format(HOST, str(PORT))
    AWS_DEFAULT_REGION: str = Field(..., env="AWS_DEFAULT_REGION")
    DYNAMODB_TABLE_NAME: str = Field(..., env="DYNAMODB_TABLE_NAME")

    class Config:
        env_file = ENV_FILE
        env_file_encoding = 'utf-8'
        case_sensitive: bool = True


@lru_cache()
def get_settings():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path + "/" + ENV_FILE)
    settings = Settings(
        _env_file=f'{dir_path}/{ENV_FILE}',
        _env_file_encoding='utf-8',
    )
    return settings
