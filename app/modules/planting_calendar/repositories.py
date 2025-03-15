from app.modules.planting_calendar.models import PlantingCalendar
from core.repositories.BaseRepository import BaseRepository


class PlantingCalendarRepository(BaseRepository):
    def __init__(self):
        super().__init__(PlantingCalendar)
