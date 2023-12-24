from typing import Dict

from pydantic_settings import BaseSettings

from definitions import ROOT_DIR


class GlobalConfig(BaseSettings):
    SERVICE_NAME: str = 'My Web APP'
    DESCRIPTION: str = 'Lab1* Web App'
    VERSION: str = '0.1.0'

    ENV: str = 'dev'

    POSTGRES_DBNAME: str = ''
    POSTGRES_USER: str = ''
    POSTGRES_PASSWORD: str = ''
    POSTGRES_HOST: str = ''
    POSTGRES_PORT: int = 5432

    @property
    def database_settings(self) -> Dict[str, str]:
        """
        Get all settings for connection with database.
        """
        return {
            'database': self.POSTGRES_DBNAME,
            'user': self.POSTGRES_USER,
            'password': self.POSTGRES_PASSWORD,
            'host': self.POSTGRES_HOST,
            'port': str(self.POSTGRES_PORT),
        }

    @property
    def database_uri(self) -> str:
        """
        Get uri for connection with database.
        """
        return 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(
            **self.database_settings,
        )

    class Config:
        env_file = ROOT_DIR / '.env'
        env_file_encoding = 'utf-8'
        extra = 'allow'


config = GlobalConfig()
