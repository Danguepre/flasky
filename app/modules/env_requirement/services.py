from app.modules.env_requirement.repositories import EnvRequirementRepository
from core.services.BaseService import BaseService


class EnvRequirementService(BaseService):
    def __init__(self):
        super().__init__(EnvRequirementRepository())
