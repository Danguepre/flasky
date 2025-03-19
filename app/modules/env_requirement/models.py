from app import db
from enum import Enum

from sqlalchemy import Enum as SQLAlchemyEnum


class SunExposure(Enum):
    Full_sun = "Full Sun"
    Partial_shade = "Partial Shade"
    Full_shade = "Full Shade"


class EnvRequirement(db.Model):

    id_requirement = db.Column(db.Integer, primary_key=True)
    sun_exposure = db.Column(SQLAlchemyEnum(SunExposure), nullable=False)
    min_temp = db.Column(db.Float, nullable=False)
    max_temp = db.Column(db.Float, nullable=False)
    frost_tolerance = db.Column(db.Boolean, nullable=False)
    id_crop = db.Column(db.Integer, db.ForeignKey('crop.id'), nullable=False)
    crop = db.relationship("Crop", back_populates="env_requirements")
