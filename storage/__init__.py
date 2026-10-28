# storage/__init__.py
import os
from .json_store import JSONStorage
from .sqlite_store import SQLiteStorage
from .base import Storage

def get_storage() -> Storage:
    # 환경변수로 쉽게 교체: STORAGE_BACKEND=json or sqlite
    backend = os.environ.get("STORAGE_BACKEND", "json").lower()

    if backend == "sqlite":
        db_path = os.environ.get("SQLITE_PATH", "data/app.db")
        return SQLiteStorage(db_path)

    # default json
    json_path = os.environ.get("JSON_PATH", "data/users.json")
    return JSONStorage(json_path)