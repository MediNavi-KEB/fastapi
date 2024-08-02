from sqlalchemy.orm import Session
from db.models.calendar import Calendar
from dto.calendar_dto import CalendarCreateModel, CalendarUpdateModel
from datetime import datetime
from sqlalchemy import cast, Date, extract


def get_calendar_by_id(db: Session, calendar_id: int):
    return db.query(Calendar).filter(Calendar.calendar_id == calendar_id).first()


def get_calendar_by_id_and_date(db: Session, user_id: str, date_str: str):
    specific_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    db_calendar = db.query(Calendar).filter(
        Calendar.user_id == user_id,
        cast(Calendar.date_time, Date) == specific_date
    ).all()

    return [
        CalendarUpdateModel(
            date_time=calendar.date_time,
            memo_category=calendar.memo_category,
            memo_content=calendar.memo_content
        ) for calendar in db_calendar
    ]


def get_calendar_by_id_and_year(db: Session, user_id: str, year_str: str):
    specific_year = datetime.strptime(year_str, "%Y").year
    db_calendar = db.query(Calendar).filter(
        Calendar.user_id == user_id,
        extract("year", Calendar.date_time) == specific_year
    ).all()

    return [
        CalendarUpdateModel(
            date_time=calendar.date_time,
            memo_category=calendar.memo_category,
            memo_content=calendar.memo_content
        ) for calendar in db_calendar
    ]



def create_calendar(db: Session, calendar: CalendarCreateModel, user_id: str):
    db_calendar = Calendar(
        user_id=user_id,
        date_time=calendar.date_time,
        memo_category=calendar.memo_category,
        memo_content=calendar.memo_content
    )
    db.add(db_calendar)
    db.commit()
    db.refresh(db_calendar)
    return db_calendar


def delete_calendar(db: Session, calendar_id: int):
    db_calendar = get_calendar_by_id(db, calendar_id)
    if db_calendar:
        db.delete(db_calendar)
        db.commit()
    return db_calendar


def update_calendar_db(db: Session, db_calendar: Calendar, calendar_update: CalendarUpdateModel):
    if calendar_update.date_time is not None:
        db_calendar.date_time = calendar_update.date_time
    if calendar_update.memo_category is not None:
        db_calendar.memo_category = calendar_update.memo_category
    if calendar_update.memo_content is not None:
        db_calendar.memo_content = calendar_update.memo_content

    db.commit()
    db.refresh(db_calendar)
    return db_calendar
