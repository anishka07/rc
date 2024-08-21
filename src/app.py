from pypdf import PdfReader
import streamlit as st
import pickle
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.settings import clean_resume, text_transform, Settings
from utils.paths import Paths

vectorizer = pickle.load(open(Paths.GET_VECTORIZER_PKL, "rb"))
model = pickle.load(open(Paths.GET_MODEL_PKL, "rb"))


def main():
    st.title("Resume Classifier")

    uploaded_file = st.file_uploader("Upload your resume", type=["txt", "pdf"])

    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)
        all_text = ""
        for page in reader.pages:
            all_text += page.extract_text()
        clean_resume_text = clean_resume(all_text)
        transformed_text = text_transform(clean_resume_text)

        input_features = vectorizer.transform([transformed_text])

        prediction_id = model.predict(input_features)[0]
        st.write(f"Predicted Category ID: {prediction_id}")

        category_name = Settings.CATEGORY.get(prediction_id, "Unknown")
        st.write("Predicted Category: ", category_name)


if __name__ == "__main__":
    main()
