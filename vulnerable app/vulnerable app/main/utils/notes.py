from typing import List
from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from main.models import Session, Note


def user_notes(user_id: int) -> List[Note]:
    with Session(expire_on_commit=False) as session:
        return session.query(Note).filter(
            or_(Note.user_id == user_id,
                Note.private == False)).options(joinedload(Note.user)).all()
