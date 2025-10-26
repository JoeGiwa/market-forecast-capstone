""" 
env_loader.py
----------------
Utility for safely loading and validating environment variables (.env) 
in the Market Forecast Capstone project.

Usage:
    from src.utils.env_loader import load_env, check_env

    load_env()          # Loads .env variables
    check_env()         # Prints status of all keys
"""

from dotenv import load_dotenv
import os


def load_env():
    """Loads environment variables from .env file."""
    load_dotenv()
    print("✅ Environment variables loaded.")


def check_env():
    """Verifies that required environment variables exist and aren't placeholders."""
    keys = [
        "ALPHA_VANTAGE_API_KEY",
        "FRED_API_KEY",
        "GUARDIAN_API_KEY",
        "TIMEZONE",
        "DATA_START_YEAR",
        "TICKER",
    ]

    print("🔍 Checking environment variables...\n")
    missing = False

    for key in keys:
        value = os.getenv(key)
        if value and "your_" not in value:
            print(f"✅ {key} loaded successfully.")
        elif value:
            print(f"⚠️  {key} exists but has a placeholder value.")
        else:
            print(f"❌ {key} not found.")
            missing = True

    if missing:
        print("\n⚠️  Some keys are missing or invalid — please update your .env file.")
    else:
        print("\n✅ All required environment variables are correctly configured.")


if __name__ == "__main__":
    load_env()
    check_env()
