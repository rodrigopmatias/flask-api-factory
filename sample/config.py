from pydantic import BaseSettings


class __Settings(BaseSettings):
    APP_ID: str = "sample-v1.0.0"

    DB_URI: str = "sqlite://"
    DB_ECHO: bool = True

    class Config:
        env_file = (".env", ".prod.env", ".dev.env")


settings = __Settings()
