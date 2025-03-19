from app.modules.crop.models import Crop
from core.seeders.BaseSeeder import BaseSeeder
from app import db

from app.modules.env_requirement.models import EnvRequirement, SunExposure


class EnvRequirementsSeeder(BaseSeeder):

    priority = 4

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

        env_requirements = [
            EnvRequirement(
                id_crop=corn.id,
                sun_exposure=SunExposure.Full_sun,
                min_temp=10.0,
                max_temp=35.0,
                frost_tolerance=False
            ),
            EnvRequirement(
                id_crop=soybean.id,
                sun_exposure=SunExposure.Full_sun,
                min_temp=12.0,
                max_temp=30.0,
                frost_tolerance=False
            ),
            EnvRequirement(
                id_crop=sunflower.id,
                sun_exposure=SunExposure.Full_sun,
                min_temp=15.0,
                max_temp=32.0,
                frost_tolerance=False
            ),
            EnvRequirement(
                id_crop=tomato.id,
                sun_exposure=SunExposure.Partial_shade,
                min_temp=10.0,
                max_temp=30.0,
                frost_tolerance=False
            ),
            EnvRequirement(
                id_crop=apple.id,
                sun_exposure=SunExposure.Full_sun,
                min_temp=-5.0,
                max_temp=25.0,
                frost_tolerance=True
            ),
            EnvRequirement(
                id_crop=rose.id,
                sun_exposure=SunExposure.Partial_shade,
                min_temp=5.0,
                max_temp=30.0,
                frost_tolerance=True
            ),
            EnvRequirement(
                id_crop=potato.id,
                sun_exposure=SunExposure.Full_sun,
                min_temp=5.0,
                max_temp=25.0,
                frost_tolerance=True
            ),
            EnvRequirement(
                id_crop=bermuda_grass.id,
                sun_exposure=SunExposure.Full_sun,
                min_temp=15.0,
                max_temp=40.0,
                frost_tolerance=False
            ),
        ]

        try:
            db.session.add_all(env_requirements)
            db.session.commit()
            print("Seed: Environmental Requirements added successfully")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding environmental requirements: {e}")
