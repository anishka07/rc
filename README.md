# Resume Classifier w/ FastAPI

A machine learning project that takes a resume in pdf format as an input and predicts the class of that resume using machine learning.
The categories it can predict are listed below:
- Java Developer
- Testing
- DevOps Engineer
- Python Developer
- Web Designing
- HR
- Hadoop
- Blockchain
- ETL Developer
- Operations Manager
- Data Science
- Sales
- Mechanical Engineer
- Arts
- Database
- Electrical Engineering
- Health and fitness
- Project Management Officer
- Business Analyst 
- DotNet Developer 
- Automation Testing
- Network Security Engineer 
- SAP Developer
- Civil Engineer 
- Advocate 

## Project Structure

```plaintext
├── README.md
├── app
│   ├── __init__.py
│   ├── main.py # contains main fast api application
│   ├── models
│   │   ├── __init__.py
│   │   └── schemas.py # contains http response schema
│   └── routers
│       ├── __init__.py
│       └── api.py # contains api routing
├── data
│   ├── processed
│   │   └── processed_resume.csv
│   └── raw
│       └── resume.csv
├── models
│   ├── model.pkl # ml model in pickle form
│   └── vectorizer.pkl # feature extractor in pickle form
├── notebooks
│   ├── eda_raw_resume_data.ipynb
│   └── ml_model_building.ipynb
├── requirements.txt
├── src
│   ├── __init__.py
│   └── app.py # streamlit application for ui 
└── utils # contains all the redundant helper functions
    ├── __init__.py
    ├── paths.py
    └── settings.py
```