from app.modules.crop.repositories import CropRepository
from core.services.BaseService import BaseService


class CropService(BaseService):
    def __init__(self):
        super().__init__(CropRepository())
