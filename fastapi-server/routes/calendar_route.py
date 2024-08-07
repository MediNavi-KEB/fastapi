from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from dto.calendar_dto import CalendarCreateModel, CalendarUpdateModel
from services import calendar_service
from db.connection import get_db
from typing import List


calendar_router = APIRouter(tags=["Calendar"])


@calendar_router.post("/register", response_model=CalendarCreateModel)
def register_calendar(calendar: CalendarCreateModel, db: Session = Depends(get_db)):
    return calendar_service.register_calendar(db, calendar)


@calendar_router.get("/read/{user_id}/{date}", response_model=List[CalendarUpdateModel])
def read_calendar_date(user_id: str, date: str, db: Session = Depends(get_db)):
    return calendar_service.read_calendar_date(db, user_id, date)


@calendar_router.delete("/delete/{calendar_id}")
def delete_calendar(calendar_id: int, db: Session = Depends(get_db)):
    return calendar_service.delete_calendar(db, calendar_id)


@calendar_router.put("/update/{calendar_id}")
def update_calendar(calendar_id: int, calendar_update: CalendarUpdateModel, db: Session = Depends(get_db)):
    return calendar_service.update_calendar(db, calendar_id, calendar_update)


@calendar_router.get("/read/year/{user_id}/{year}", response_model=List[CalendarUpdateModel])
def read_calendar_year(user_id: str, year: str, db: Session = Depends(get_db)):
    return calendar_service.read_calendar_year(db, user_id, year)


@calendar_router.get("/read/{user_id}", response_model=List[CalendarUpdateModel])
def read_calendars_by_user(user_id: str, db: Session = Depends(get_db)):
    return calendar_service.read_calendars_by_user(db, user_id)
