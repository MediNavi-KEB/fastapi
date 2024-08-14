from sqlalchemy.orm import Session
from crud import calendar_crud
from dto.calendar_dto import CalendarCreateModel, CalendarUpdateModel, CalendarReadModel
from fastapi import HTTPException
from typing import List, Dict
from datetime import timedelta


def register_calendar(db: Session, calendar: CalendarCreateModel):
    if not calendar.user_id:
        raise HTTPException(status_code=400, detail="로그인 후 사용해 주세요.")
    if not calendar.memo_content:
        raise HTTPException(status_code=400, detail="메모 내용을 입력해 주세요.")

    start_date = calendar.start_date
    end_date = calendar.end_date

    current_date = start_date
    while current_date <= end_date:
        single_day_calendar = CalendarCreateModel(
            user_id=calendar.user_id,
            start_date=current_date,  # 이 부분을 단일 datetime으로 설정
            end_date=current_date,  # 이 부분을 단일 datetime으로 설정
            memo_category=calendar.memo_category,
            memo_content=calendar.memo_content
        )
        calendar_crud.create_calendar(db, single_day_calendar, calendar.user_id)
        current_date += timedelta(days=1)

    return {"message": "메모가 성공적으로 저장되었습니다."}


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


def read_calendars_by_user(db: Session, user_id: str) -> List[CalendarReadModel]:
    return calendar_crud.get_calendars_by_user(db, user_id)


def get_current_month_frequencies(db: Session, user_id: str) -> Dict[str, int]:
    frequencies = calendar_crud.get_current_month_frequencies(db, user_id)

    # 기본 카테고리 빈도수를 0으로 설정
    result = {
        "통증": 0,
        "약": 0,
        "병원": 0
    }

    for frequency in frequencies:
        result[frequency.memo_category] = frequency.frequency

    return result
