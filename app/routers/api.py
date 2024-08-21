from fastapi import APIRouter, HTTPException, UploadFile, File
from pypdf import PdfReader
import pickle

from app.helpers.tp_helpers import clean_resume, Settings, text_transform
from app.models.schemas import PredictionResponse

router = APIRouter()
vectorizer = pickle.load(open("/Users/anishkamukherjee/Documents/resume_classifier/models/vectorizer.pkl", "rb"))
model = pickle.load(open("/Users/anishkamukherjee/Documents/resume_classifier/models/model.pkl", "rb"))


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
