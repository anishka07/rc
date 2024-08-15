import streamlit as st
from pypdf import PdfReader
import pickle

from settings import Settings, text_transform, clean_resume

model = pickle.load(open("/Users/anishkamukherjee/Documents/resume_classifier/models/model.pkl", "rb"))
vectorizer = pickle.load(open("/Users/anishkamukherjee/Documents/resume_classifier/models/vectorizer.pkl", "rb"))

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
