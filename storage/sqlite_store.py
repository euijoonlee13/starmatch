# storage/sqlite_store.py
# now I will use json but if I have to handle more data in the future , can use sqlite - code structure will be almost same
import sqlite3
from typing import List, Optional
from .base import Storage, User

class SQLiteStorage(Storage):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init(self):
        with self._connect() as con:
            con.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                birth TEXT NOT NULL,
                zodiac TEXT NOT NULL
            )
            """)

    def add_user(self, name: str, birth: str, zodiac: str) -> User:
        raise NotImplementedError("later change to SQLite")

    def list_users(self) -> List[User]:
        raise NotImplementedError("later change to SQLite")

    def get_user(self, user_id: str) -> Optional[User]:
        raise NotImplementedError("later change to SQLite")