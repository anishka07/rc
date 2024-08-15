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
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate",
}

sample_resume_text = """I am a data scientist specializing in machine
learning, deep learning, and computer vision. With
a strong background in mathematics, statistics,
and programming, I am passionate about
uncovering hidden patterns and insights in data.
I have extensive experience in developing
predictive models, implementing deep learning
algorithms, and designing computer vision
systems. My technical skills include proficiency in
Python, Sklearn, TensorFlow, and PyTorch.
What sets me apart is my ability to effectively
communicate complex concepts to diverse
audiences. I excel in translating technical insights
into actionable recommendations that drive
informed decision-making.
If you're looking for a dedicated and versatile data
scientist to collaborate on impactful projects, I am
eager to contribute my expertise. Let's harness the
power of data together to unlock new possibilities
and shape a better future.
Contact & Sources
Email: 611noorsaeed@gmail.com
Phone: 03442826192
Github: https://github.com/611noorsaeed
Linkdin: https://www.linkedin.com/in/noor-saeed654a23263/
Blogs: https://medium.com/@611noorsaeed
Youtube: Artificial Intelligence
ABOUT ME
WORK EXPERIENCE
SKILLES
NOOR SAEED
LANGUAGES
English
Urdu
Hindi
I am a versatile data scientist with expertise in a wide
range of projects, including machine learning,
recommendation systems, deep learning, and computer
vision. Throughout my career, I have successfully
developed and deployed various machine learning models
to solve complex problems and drive data-driven
decision-making
Machine Learnine
Deep Learning
Computer Vision
Recommendation Systems
Data Visualization
Programming Languages (Python, SQL)
Data Preprocessing and Feature Engineering
Model Evaluation and Deployment
Statistical Analysis
Communication and Collaboration
"""

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
    SAMPLE_TEXT = sample_resume_text
