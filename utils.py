import json


def load_students(filepath: str) -> list:
    """
    Function loading data from students.json
    :return: list
    """
    with open(filepath, encoding="utf-8") as file:
        contents = json.load(file)
        return contents


def load_professions(filepath: str) -> list:
    """
    Function loading data from professions.json
    :return: list
    """
    with open(filepath, encoding="utf-8") as file:
        contents = json.load(file)
        return contents


def get_student_by_pk(students_info: list, user_pk: int) -> dict:
    """
    Function getting data by pk
    :return: dict
    """
    for student in students_info:
        if student["pk"] == user_pk:
            return student


def get_professions_by_title(professions_list: list, prof_name: str) -> dict:
    """
    Function getting data by title
    :return: dict
    """
    for profession in professions_list:
        if profession["title"] == prof_name:
            return profession


def check_skills(student, profession) -> dict:
    """
    Function checking skills
    :return:
    """
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])
    matching_skills = list(student_skills.intersection(profession_skills))
    diffident_skills = list(student_skills.difference(profession_skills))
    compliance_percentage = int(len(matching_skills) / len(profession_skills) * 100)
    matching = {
        "has": matching_skills,
        "lacks": diffident_skills,
        "compliance_percent": compliance_percentage,
    }
    return matching
