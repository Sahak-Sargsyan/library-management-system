from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from application.member_service import MemberService
from infrastructure.library_repository import LibraryRepository
from application.schemas import MemberCreate, MemberUpdate, MemberBase

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)

@router.get("/")
def get_members(db: Session = Depends(get_db)):
    service = MemberService(LibraryRepository(db))
    members = service.get_members()
    return {"members": members}

@router.post("/")
def create_member(new_member: MemberCreate, db: Session = Depends(get_db)):
    service = MemberService(LibraryRepository(db))
    new_member = service.create_member(new_member)
    return {"new member": new_member}