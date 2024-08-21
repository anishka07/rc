import os


def get_src_path():
    return os.path.abspath(os.getcwd())


def get_project_dir():
    src_path = get_src_path()
    return os.path.dirname(src_path)


class Paths:
    GET_PROJECT_DIR = get_project_dir()
    GET_MODEL_PKL = os.path.join(GET_PROJECT_DIR, "ml_models/model.pkl")
    GET_VECTORIZER_PKL = os.path.join(GET_PROJECT_DIR, "ml_models/vectorizer.pkl")
