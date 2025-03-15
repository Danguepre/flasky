from app.modules.crop.models import Crop
from app.modules.planting_calendar.models import PlantingCalendar
from core.seeders.BaseSeeder import BaseSeeder
from app import db
from datetime import date


class PlantingCalendarSeeder(BaseSeeder):

    priority = 4  # Menor prioridad que los usuarios, si es necesario

    def run(self):
        # Asegúrate de que los cultivos existen en la base de datos
        corn = Crop.query.filter_by(name="Corn").first()
        soybean = Crop.query.filter_by(name="Soybean").first()
        sunflower = Crop.query.filter_by(name="Sunflower").first()
        tomato = Crop.query.filter_by(name="Tomato").first()
        apple = Crop.query.filter_by(name="Apple").first()
        rose = Crop.query.filter_by(name="Rose").first()
        potato = Crop.query.filter_by(name="Potato").first()
        bermuda_grass = Crop.query.filter_by(name="Bermuda Grass").first()

        # Datos del calendario de siembra
        planting_calendars = [
            PlantingCalendar(
                planting_date_start=date(2025, 3, 15),
                planting_date_end=date(2025, 3, 30),
                transplant_date_start=date(2025, 5, 15),
                transplant_date_end=date(2025, 5, 30),
                estimated_harvest_start_date=date(2025, 8, 1),
                estimated_harvest_end_date=date(2025, 8, 15),
                id_crop=corn.id
            ),
            PlantingCalendar(
                planting_date_start=date(2025, 5, 1),
                planting_date_end=date(2025, 5, 15),
                transplant_date_start=date(2025, 6, 15),
                transplant_date_end=date(2025, 6, 30),
                estimated_harvest_start_date=date(2025, 9, 1),
                estimated_harvest_end_date=date(2025, 9, 15),
                id_crop=soybean.id
            ),
            PlantingCalendar(
                planting_date_start=date(2025, 4, 1),
                planting_date_end=date(2025, 4, 15),
                transplant_date_start=date(2025, 5, 1),
                transplant_date_end=date(2025, 5, 15),
                estimated_harvest_start_date=date(2025, 7, 15),
                estimated_harvest_end_date=date(2025, 7, 30),
                id_crop=sunflower.id
            ),
            PlantingCalendar(
                planting_date_start=date(2025, 3, 1),
                planting_date_end=date(2025, 3, 15),
                transplant_date_start=date(2025, 4, 15),
                transplant_date_end=date(2025, 4, 30),
                estimated_harvest_start_date=date(2025, 7, 1),
                estimated_harvest_end_date=date(2025, 7, 15),
                id_crop=tomato.id
            ),
            PlantingCalendar(
                planting_date_start=date(2025, 2, 1),
                planting_date_end=date(2025, 2, 15),
                transplant_date_start=date(2025, 3, 1),
                transplant_date_end=date(2025, 3, 15),
                estimated_harvest_start_date=date(2025, 8, 15),
                estimated_harvest_end_date=date(2025, 8, 30),
                id_crop=apple.id
            ),
            PlantingCalendar(
                planting_date_start=date(2025, 4, 1),
                planting_date_end=date(2025, 4, 15),
                transplant_date_start=date(2025, 5, 1),
                transplant_date_end=date(2025, 5, 15),
                estimated_harvest_start_date=date(2025, 9, 1),
                estimated_harvest_end_date=date(2025, 9, 15),
                id_crop=rose.id
            ),
            PlantingCalendar(
                planting_date_start=date(2025, 4, 15),
                planting_date_end=date(2025, 4, 30),
                transplant_date_start=date(2025, 5, 15),
                transplant_date_end=date(2025, 5, 30),
                estimated_harvest_start_date=date(2025, 7, 1),
                estimated_harvest_end_date=date(2025, 7, 15),
                id_crop=potato.id
            ),
            PlantingCalendar(
                planting_date_start=date(2025, 3, 1),
                planting_date_end=date(2025, 3, 15),
                transplant_date_start=date(2025, 4, 1),
                transplant_date_end=date(2025, 4, 15),
                estimated_harvest_start_date=date(2025, 7, 15),
                estimated_harvest_end_date=date(2025, 7, 30),
                id_crop=bermuda_grass.id
            ),
        ]

        try:
            db.session.add_all(planting_calendars)
            db.session.commit()
            print("Seed: Planting calendars added successfully")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding planting calendars: {e}")
