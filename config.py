from pathlib import Path

ROOT_PATH = Path(__file__).parent
STUD_DATA = Path.joinpath(ROOT_PATH, "data", "students.json")
PROF_DATA = Path.joinpath(ROOT_PATH, "data", "professions.json")
