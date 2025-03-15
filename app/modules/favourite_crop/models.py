from app import db


class FavouriteCrop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    crop_id = db.Column(db.Integer, db.ForeignKey("crop.id"), nullable=False)

    # Relación con el modelo User
    user = db.relationship("User", back_populates="favourite_crops")

    # Relación con el modelo Crop
    crop = db.relationship("Crop", back_populates="favourite_crops")

    def __repr__(self):
        return f"<FavouriteCrop User: {self.user_id}, Crop: {self.crop_id}>"
