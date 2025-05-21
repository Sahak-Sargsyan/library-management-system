from typing import Optional
import uuid

class Member:
    member_id: Optional[uuid.UUID] = None
    name: str
    email: str

    def __init__(self, name, email, id:Optional[uuid.UUID] = None):
        self.member_id = id
        self.name = name
        self.email = email