from pydantic import BaseModel
from typing import Optional


class TelegramIDModel(BaseModel):
    telegram_id: int

    
class UserModel(TelegramIDModel):
    username: Optional[str] = None
    first_name: str
    last_name: Optional[str] = None
    best_score: int = 0


class SetBestScoreRequest(BaseModel):
    score: int


class SetBestScoreResponse(BaseModel):
    status: str
    best_score: int