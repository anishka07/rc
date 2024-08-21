from pydantic import BaseModel


class PredictionResponse(BaseModel):
    category: str

    class Config:
        schema_extra = {
            "example": {
                "category": "Data Science"
            }
        }
