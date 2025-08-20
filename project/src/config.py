import sys, os

try:
    import numpy as np
    from dotenv import load_dotenv
    print("Imports OK")
except Exception as e:
    print("Import error:", e)
    raise

from pathlib import Path

from typing import Optional





print("Python version:", sys.version)
print("Interpreter path:", sys.executable)

load_dotenv()  # looks for a .env file in the current and parent directories
print(".env loaded (if present)")



def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)

api_key_present = get_key("API_KEY") is not None
data_dir_env = get_key("DATA_DIR", str(DATA_DIR))
print("API_KEY present:", api_key_present)
print("DATA_DIR from env:", data_dir_env)

# Ensure data directory exists (non-destructive)
Path(data_dir_env).mkdir(parents=True, exist_ok=True)
print("Ensured data directory exists.")