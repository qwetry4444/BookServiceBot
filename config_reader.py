# import os
#
# from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import SecretStr
#
# ENV_FILE_DIR = os.path.abspath("..\..")
#
# class Settings(BaseSettings):
#     bot_token: SecretStr
#     postgres_user: str
#     postgres_host: str
#     postgres_db: str
#     postgres_port: int
#     postgres_password: SecretStr
#     model_config = SettingsConfigDict(env_file=f'{ENV_FILE_DIR}\.env', env_file_encoding='utf-8')
#
#
# config = Settings()
