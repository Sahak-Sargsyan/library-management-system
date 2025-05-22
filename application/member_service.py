from infrastructure.library_repository import LibraryRepository
from uuid import UUID
from infrastructure.models import Member
from shared.schemas import MemberCreate, MemberUpdate
import uuid
from shared.exceptions import NotFoundException, DuplicateEmailException

class MemberService:
    repository: LibraryRepository

    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def get_members(self):
        return self.repository.get_all_members()
    
    def create_member(self, new_member: MemberCreate):
        try:
            member_to_add = Member(name = new_member.name, email = new_member.email)
            member_to_add.member_id = uuid.uuid4()
            return self.repository.create_member(member_to_add)
        except DuplicateEmailException:
            raise
    
    def get_member_by_id(self, member_id: UUID):
        try:
            member = self.repository.get_member_by_id(member_id)
            return member
        except NotFoundException:
            raise
        
    
    def update_member(self, member_id: UUID, updated_member: MemberUpdate):
        try:
            member_to_update = Member(
                name = updated_member.name,
                email = updated_member.email,
                member_id = member_id
            )
            return self.repository.update_member(member_id, member_to_update)
        except NotFoundException:
            raise

    def delete_member(self, member_id: UUID):
        self.repository.delete_member_by_id(member_id)