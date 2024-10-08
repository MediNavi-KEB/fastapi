from sqlalchemy.orm import Session
from db.models.calendar import Calendar
from dto.calendar_dto import CalendarCreateModel, CalendarUpdateModel, CalendarReadModel
from sqlalchemy import func
from datetime import datetime, timedelta


def get_calendar_by_id(db: Session, calendar_id: int):
    return db.query(Calendar).filter(Calendar.calendar_id == calendar_id).first()


def create_calendar(db: Session, calendar: CalendarCreateModel, user_id: str):
    db_calendar = Calendar(
        user_id=user_id,
        date_time=calendar.start_date,
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


def get_calendars_by_user(db: Session, user_id: str):
    db_calendar = db.query(Calendar).filter(Calendar.user_id == user_id).all()
    return [
        CalendarReadModel(
            calendar_id=calendar.calendar_id,
            user_id=calendar.user_id,
            date_time=calendar.date_time,
            memo_category=calendar.memo_category,
            memo_content=calendar.memo_content
        ) for calendar in db_calendar
    ]


def get_current_month_frequencies(db: Session, user_id: str):
    start_of_month = datetime(datetime.now().year, datetime.now().month, 1)
    end_of_month = start_of_month + timedelta(days=32)
    end_of_month = datetime(end_of_month.year, end_of_month.month, 1)

    frequencies = db.query(
        Calendar.memo_category,
        func.count(Calendar.memo_category).label("frequency")
    ).filter(
        Calendar.user_id == user_id,
        Calendar.date_time >= start_of_month,
        Calendar.date_time < end_of_month
    ).group_by(
        Calendar.memo_category
    ).all()

    return frequencies
