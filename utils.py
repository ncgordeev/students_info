import json
from config import PROF_DATA, STUD_DATA


def load_students(filepath):
    """
    Function loading data from students.json
    :return:
    """
    with open(filepath) as file:
        contents = json.load(file)
        return contents


def load_professions(filepath):
    """
    Function loading data from professions.json
    :return:
    """
    with open(filepath) as file:
        contents = json.load(file)
        return contents


print(load_students(STUD_DATA))
print(load_professions(PROF_DATA))
