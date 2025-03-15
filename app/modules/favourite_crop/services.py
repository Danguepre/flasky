from app.modules.favourite_crop.repositories import FavouriteCropRepository
from core.services.BaseService import BaseService


class FavouriteCropService(BaseService):
    def __init__(self):
        super().__init__(FavouriteCropRepository())
