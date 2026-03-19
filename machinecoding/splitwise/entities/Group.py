from typing import List
from .User import User
import uuid
class Group:
    def __init__(self, name: str, members: List[User]):
        self._id = str(uuid.uuid4())
        self._name = name
        self._members = members

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_members(self):
        return self._members