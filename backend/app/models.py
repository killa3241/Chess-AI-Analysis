from pydantic import BaseModel
from typing import List

class AnalysisResponse(BaseModel):
    advice: List[str]