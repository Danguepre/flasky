from app.modules.crop.models import Crop
from core.repositories.BaseRepository import BaseRepository


class CropRepository(BaseRepository):
    def __init__(self):
        super().__init__(Crop)
