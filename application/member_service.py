from infrastructure.library_repository import LibraryRepository
from uuid import UUID
from infrastructure.models import Member

class MemberService:
    repository: LibraryRepository

    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def get_members(self):
        return self.repository.get_all_members
    
    def get_member_by_id(self, member_id: UUID):
        return self.repository.get_member_by_id(member_id)
    
    def update_member(self, member_id: UUID, updated_member: Member):
        self.repository.update_member(member_id, updated_member)

    def delete_member(self, member_id: UUID):
        self.repository.delete_member_by_id(member_id)