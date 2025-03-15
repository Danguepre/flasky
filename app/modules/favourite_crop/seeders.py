from app.modules.auth.models import User
from app.modules.crop.models import Crop
from app.modules.favourite_crop.models import FavouriteCrop
from core.seeders.BaseSeeder import BaseSeeder
from app import db
import random


class FavouriteCropSeeder(BaseSeeder):

    priority = 3  # Se ejecuta después de los usuarios y cultivos

    def run(self):
        users = User.query.all()
        crops = Crop.query.all()

        if not users or not crops:
            print("No users or crops found. Skipping FavouriteCrop seeding.")
            return

        favourite_crops = []

        for user in users:
            # Cada usuario tendrá de 1 a 3 cultivos favoritos aleatorios
            fav_crops = random.sample(crops, k=min(3, len(crops)))
            for crop in fav_crops:
                # Evitamos duplicados
                if not FavouriteCrop.query.filter_by(user_id=user.id, crop_id=crop.id).first():
                    favourite_crops.append(FavouriteCrop(user_id=user.id, crop_id=crop.id))

        try:
            db.session.add_all(favourite_crops)
            db.session.commit()
            print(f"Seed: {len(favourite_crops)} FavouriteCrops added successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding FavouriteCrops: {e}")
