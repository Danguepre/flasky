from app import db


class PlantingCalendar(db.Model):

    id_calendar = db.Column(db.Integer, primary_key=True)
    planting_date_start = db.Column(db.Date, nullable=False)
    planting_date_end = db.Column(db.Date, nullable=True)
    transplant_date_start = db.Column(db.Date, nullable=True)
    transplant_date_end = db.Column(db.Date, nullable=True)
    estimated_harvest_start_date = db.Column(db.Date, nullable=True)
    estimated_harvest_end_date = db.Column(db.Date, nullable=True)

    # Relación con Crop
    id_crop = db.Column(db.Integer, db.ForeignKey("crop.id"), nullable=False)
    crop = db.relationship("Crop", back_populates="planting_calendars")

    def __repr__(self):
        return f"<PlantingCalendar Crop: {self.id_crop}, Planting Start: {self.planting_date_start}>"

    def to_dict(self):
        return {
            "id_calendar": self.id_calendar,
            "planting_date_start": self.planting_date_start,
            "planting_date_end": self.planting_date_end,
            "transplant_date_start": self.transplant_date_start,
            "transplant_date_end": self.transplant_date_end,
            "estimated_harvest_start_date": self.estimated_harvest_start_date,
            "estimated_harvest_end_date": self.estimated_harvest_end_date,
            "id_crop": self.id_crop
        }
