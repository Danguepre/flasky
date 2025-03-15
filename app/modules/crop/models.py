from app import db
from enum import Enum

from sqlalchemy import Enum as SQLAlchemyEnum


class CropType(Enum):
    Cereals = "Cereals"
    Legumes = "Legumes"
    Oilseeds = "Oilseeds"
    Vegetables = "Vegetables"
    Fruits = "Fruits"
    Ornamentals = "Ornamentals"
    Roots_and_Tubers = "Roots_and_Tubers"
    Grasses = "Grasses"


class LifeCycle(Enum):
    Annual = "Annual"
    Perennial = "Perennial"
    Biennial = "Biennial"


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(SQLAlchemyEnum(CropType), nullable=False)
    life_cycle = db.Column(SQLAlchemyEnum(LifeCycle), nullable=False)

    favourite_crops = db.relationship("FavouriteCrop", back_populates="crop", lazy=True, cascade="all, delete")
    planting_calendars = db.relationship("PlantingCalendar", back_populates="crop", lazy=True, cascade="all, delete")
