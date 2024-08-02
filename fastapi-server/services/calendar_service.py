from sqlalchemy.orm import Session
from crud import calendar_crud
from dto.calendar_dto import CalendarCreateModel, CalendarUpdateModel
from fastapi import HTTPException
from typing import List


def register_calendar(db: Session, calendar: CalendarCreateModel):
    if not calendar.user_id:
        raise HTTPException(status_code=400, detail="로그인 후 사용해 주세요.")
    if not calendar.memo_content:
        raise HTTPException(status_code=400, detail="메모 내용을 입력해 주세요.")
    return calendar_crud.create_calendar(db, calendar, calendar.user_id)


def read_calendar_date(db: Session, user_id: str, date: str) -> List[CalendarUpdateModel]:
    db_calendar = calendar_crud.get_calendar_by_id_and_date(db, user_id, date)
    if not db_calendar:
        raise HTTPException(status_code=404, detail="등록된 메모가 없습니다.")
    return db_calendar


def delete_calendar(db: Session, calendar_id: int):
    db_calendar = calendar_crud.delete_calendar(db, calendar_id)
    if not db_calendar:
        raise HTTPException(status_code=400, detail="삭제할 메모가 없습니다.")
    return db_calendar


def update_calendar(db: Session, calendar_id: int, calendar_update: CalendarUpdateModel):
    db_calendar = calendar_crud.get_calendar_by_id(db, calendar_id)
    if db_calendar is None:
        raise HTTPException(status_code=400, detail="수정할 메모가 없습니다.")
    return calendar_crud.update_calendar_db(db, db_calendar, calendar_update)


def read_calendar_year(db: Session, user_id: str, year: str) -> List[CalendarUpdateModel]:
    db_calendar = calendar_crud.get_calendar_by_id_and_year(db, user_id, year)
    if not db_calendar:
        raise HTTPException(status_code=404, detail="등록된 메모가 없습니다.")
    return db_calendar
