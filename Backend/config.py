from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_NAME_sqlite: str

    @property
    def DATABASE_URL_sqlite(self):
        return f"sqlite:///{self.DB_NAME_sqlite}"

    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()