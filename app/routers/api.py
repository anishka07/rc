from fastapi import APIRouter, HTTPException, UploadFile, File
from pypdf import PdfReader
import pickle

from app.models.schemas import PredictionResponse
from utils.paths import Paths
from utils.settings import *

router = APIRouter()
vectorizer = pickle.load(open(Paths.GET_VECTORIZER_PKL, "rb"))
model = pickle.load(open(Paths.GET_MODEL_PKL, "rb"))


@router.get("/hello")
async def hello():
    return {"msg": "hello world"}


@router.post("/classify_resume", response_model=PredictionResponse)
async def classify_resume_image(file: UploadFile = File(...)):
    try:
        reader = PdfReader(file.file)
        all_text = ""
        for page in reader.pages:
            all_text += page.extract_text()

        clean_resume_text = clean_resume(all_text)
        transformed_text = text_transform(clean_resume_text)

        input_features = vectorizer.transform([transformed_text])
        prediction_id = model.predict(input_features)[0]

        category = Settings.CATEGORY.get(prediction_id, "Unknown")
        return PredictionResponse(
            category=category
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to process the resume file: {str(e)}")
