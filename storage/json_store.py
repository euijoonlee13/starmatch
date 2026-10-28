# storage/json_store.py
import json
import os
import uuid
from typing import List, Optional
from .base import Storage, User

class JSONStorage(Storage):
    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def _read_all(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            return []

    def _write_all(self, users: List[User]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def add_user(self, name: str, birth: str, zodiac: str) -> User:
        users = self._read_all()
        user = {"id": uuid.uuid4().hex, "name": name, "birth": birth, "zodiac": zodiac}
        users.append(user)
        self._write_all(users)
        return user

    def list_users(self) -> List[User]:
        return self._read_all()

    def get_user(self, user_id: str) -> Optional[User]:
        for u in self._read_all():
            if u["id"] == user_id:
                return u
        return None