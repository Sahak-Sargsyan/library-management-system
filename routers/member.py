from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from application.member_service import MemberService
from infrastructure.library_repository import LibraryRepository
from shared.schemas import MemberCreate, MemberUpdate, MemberBase
from uuid import UUID
from shared.exceptions import NotFoundException, DuplicateEmailException
from fastapi_pagination import Page, paginate

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)

@router.get("/", response_model=Page[MemberBase])
def get_members(db: Session = Depends(get_db)):
    service = MemberService(LibraryRepository(db))
    members = service.get_members()
    return paginate(members)

@router.get("/{member_id}", response_model=MemberBase)
def get_member_by_id(member_id: UUID, db: Session = Depends(get_db)):
    try: 
        service = MemberService(LibraryRepository(db))
        member = service.get_member_by_id(member_id)
        return member
    except NotFoundException as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))
    
@router.post("/", response_model=MemberBase)
def create_member(new_member: MemberCreate, db: Session = Depends(get_db)):
    try:
        service = MemberService(LibraryRepository(db))
        new_member = service.create_member(new_member)
        return new_member
    except DuplicateEmailException as ex:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(ex))

@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: UUID, db: Session = Depends(get_db)):
    try:
        service = MemberService(LibraryRepository(db))
        service.delete_member(member_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except NotFoundException as ex:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(ex))

@router.put("/{member_id}", response_model=MemberBase)
def update_member(member_id: UUID, updated_member: MemberUpdate, db: Session = Depends(get_db)):
    try:
        service = MemberService(LibraryRepository(db))
        upd_member = service.update_member(member_id, updated_member)
        return upd_member
    except NotFoundException as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))