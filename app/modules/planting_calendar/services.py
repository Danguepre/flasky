from app.modules.planting_calendar.repositories import PlantingCalendarRepository
from core.services.BaseService import BaseService


class PlantingCalendarService(BaseService):
    def __init__(self):
        super().__init__(PlantingCalendarRepository())
