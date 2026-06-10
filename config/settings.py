import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@dataclass
class BinanceConfig:
    api_key: Optional[str] = os.getenv("BINANCE_API_KEY")
    api_secret: Optional[str] = os.getenv("BINANCE_API_SECRET")


@dataclass
class MT5Config:
    login: Optional[str] = os.getenv("MT5_LOGIN")
    password: Optional[str] = os.getenv("MT5_PASSWORD")
    server: Optional[str] = os.getenv("MT5_SERVER")


@dataclass
class DatabaseConfig:
    host: str = os.getenv("DB_HOST", "localhost")
    port: str = os.getenv("DB_PORT", "5432")
    user: str = os.getenv("DB_USER", "wolf_admin")
    password: str = os.getenv("DB_PASS", "wolf_password")
    name: str = os.getenv("DB_NAME", "wolf_data")

    def connection_string(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


BINANCE = BinanceConfig()
MT5 = MT5Config()
DATABASE = DatabaseConfig()

# Compatibility constants for legacy configs and imports
BINANCE_API_KEY = BINANCE.api_key
BINANCE_API_SECRET = BINANCE.api_secret
MT5_LOGIN = MT5.login
MT5_PASSWORD = MT5.password
MT5_SERVER = MT5.server
DB_HOST = DATABASE.host
DB_PORT = DATABASE.port
DB_USER = DATABASE.user
DB_PASS = DATABASE.password
DB_NAME = DATABASE.name
