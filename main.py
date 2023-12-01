from config import PROF_DATA, STUD_DATA
from utils import load_students, load_professions, get_student_by_pk, get_professions_by_title, check_skills


def main():
    students = load_students(STUD_DATA)
    professions = load_professions(PROF_DATA)
    existing_prof = [prof["title"] for prof in professions]

    while True:
        user_pk_input = int(input(f"Enter student pk(from 1 to {len(students)}) or 0 to quit: "))
        if user_pk_input < 0 or user_pk_input > len(students):
            print("Wrong pk. Try again")
            continue
        if user_pk_input == 0:
            break
        else:
            student = get_student_by_pk(students, user_pk_input)
            print(f"{student['full_name']} has skills: {', '.join(student['skills'])}")
            user_prof_input = input(
                f"Selected a profession for student assessment({', '.join(existing_prof)}): "
            ).capitalize()
            if user_prof_input not in existing_prof:
                print("Wrong profession. Try again")
                continue
            profession = get_professions_by_title(professions, user_prof_input)
            matching = check_skills(student, profession)
            print(f"{matching['compliance_percent']}% of skills matched")
            if matching["compliance_percent"] == 0:
                print(f"{student['full_name']} has no required skills")
                continue
            else:
                print(f"{student['full_name']} has skills: {', '.join(matching['has'])}")
                print(f"{student['full_name']} lacks skills: {', '.join(matching['lacks'])}")
            break


if __name__ == "__main__":
    main()
