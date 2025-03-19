from app.modules.env_requirement.models import EnvRequirement
from core.repositories.BaseRepository import BaseRepository


class EnvRequirementRepository(BaseRepository):
    def __init__(self):
        super().__init__(EnvRequirement)
