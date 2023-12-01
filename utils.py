import json
from config import PROF_DATA, STUD_DATA


def load_students(filepath: str) -> list:
    """
    Function loading data from students.json
    :return: list
    """
    with open(filepath, encoding="utf-8") as file:
        contents = json.load(file)
        return contents


students = load_students(STUD_DATA)


def load_professions(filepath: str) -> list:
    """
    Function loading data from professions.json
    :return: list
    """
    with open(filepath, encoding="utf-8") as file:
        contents = json.load(file)
        return contents


professions = load_professions(PROF_DATA)


def get_student_by_pk(students_info) -> dict:
    """
    Function getting data by pk
    :return: dict
    """
    for student in students_info:
        if student["pk"] == 1:
            return student


def get_professions_by_title(professions_info) -> dict:
    """
    Function getting data by title
    :return: dict
    """
    for profession in professions_info:
        if profession["title"] == "Backend":
            return profession


print(get_student_by_pk(students))
print(get_professions_by_title(professions))
