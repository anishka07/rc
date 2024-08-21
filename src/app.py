import streamlit as st
from pypdf import PdfReader

from settings import Settings, text_transform, clean_resume
from paths import Paths

vectorizer = Paths.GET_VECTORIZER_PKL
model = Paths.GET_MODEL_PKL


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
