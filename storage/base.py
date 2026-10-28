# storage/base.py
from abc import ABC, abstractmethod
from typing import Optional, List, Dict

User = Dict[str, str]  # {"id": "...", "name": "...", "birth": "YYYY-MM-DD", "zodiac": "..."}

class Storage(ABC):
    @abstractmethod
    def add_user(self, name: str, birth: str, zodiac: str) -> User:
        ...

    @abstractmethod
    def list_users(self) -> List[User]:
        ...

    @abstractmethod
    def get_user(self, user_id: str) -> Optional[User]:
        ...