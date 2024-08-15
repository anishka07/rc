import re
from nltk.tokenize import word_tokenize

category_mapping = {
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "Project Management Officer",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate",
}

def clean_resume(text):
    url_pattern = re.compile(r'http\S+')
    rt_cc_pattern = re.compile(r'\bRT\b|\bcc\b', re.IGNORECASE)
    hashtag_pattern = re.compile(r'#\S+')
    mention_pattern = re.compile(r'@\S+')
    special_char_pattern = re.compile(r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]')
    non_ascii_pattern = re.compile(r'[^\x00-\x7f]')
    extra_spaces_pattern = re.compile(r'\s+')

    text = url_pattern.sub(' ', text)
    text = rt_cc_pattern.sub(' ', text)
    text = hashtag_pattern.sub(' ', text)
    text = mention_pattern.sub(' ', text)
    text = special_char_pattern.sub(' ', text)
    text = non_ascii_pattern.sub(' ', text)
    text = extra_spaces_pattern.sub(' ', text)
    
    text = text.lower().strip()
    
    return text

def text_transform(text: str):
    text = text.lower()
    text = word_tokenize(text)
    y = []
    for words in text:
        if words.isalnum():
            y.append(words)
    return " ".join(y)

class Settings:
    CATEGORY = category_mapping
