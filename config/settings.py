import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Binance settings
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

# MT5 settings
MT5_LOGIN = os.getenv("MT5_LOGIN")
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

# Database settings
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "wolf_admin")
DB_PASS = os.getenv("DB_PASS", "wolf_password")
DB_NAME = os.getenv("DB_NAME", "wolf_data")
