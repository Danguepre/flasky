from app.modules.crop.models import Crop, CropType, LifeCycle
from core.seeders.BaseSeeder import BaseSeeder
from app import db


class CropSeeder(BaseSeeder):

    priority = 2  # Menor prioridad que los usuarios, si es necesario

    def run(self):
        crops = [
            Crop(name="Corn", type=CropType.Cereals.value, life_cycle=LifeCycle.Annual.value),
            Crop(name="Soybean", type=CropType.Legumes.value, life_cycle=LifeCycle.Annual.value),
            Crop(name="Sunflower", type=CropType.Oilseeds.value, life_cycle=LifeCycle.Annual.value),
            Crop(name="Tomato", type=CropType.Vegetables.value, life_cycle=LifeCycle.Annual.value),
            Crop(name="Apple", type=CropType.Fruits.value, life_cycle=LifeCycle.Perennial.value),
            Crop(name="Rose", type=CropType.Ornamentals.value, life_cycle=LifeCycle.Perennial.value),
            Crop(name="Potato", type=CropType.Roots_and_Tubers.value, life_cycle=LifeCycle.Annual.value),
            Crop(name="Bermuda Grass", type=CropType.Grasses.value, life_cycle=LifeCycle.Perennial.value),
        ]

        try:
            db.session.add_all(crops)
            db.session.commit()
            print("Seed: Crops added successfully")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding crops: {e}")