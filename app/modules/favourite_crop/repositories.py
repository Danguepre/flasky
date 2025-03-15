from app.modules.favourite_crop.models import FavouriteCrop
from core.repositories.BaseRepository import BaseRepository


class FavouriteCropRepository(BaseRepository):
    def __init__(self):
        super().__init__(FavouriteCrop)
