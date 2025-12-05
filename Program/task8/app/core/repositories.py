import pickle
from app.config import DATA_DIR
from app.core.models import Discipline, Enrollment, Student
from typing import Dict, List

groups: Dict[str, list[Student]] = {}
students: Dict[int, Student] = {}
disciplines: Dict[str, Discipline] = {}
enrollment = Enrollment()

def _save(filename: str, obj):
    with open(DATA_DIR / filename, "wb") as f:
        pickle.dump(obj, f)

def save_groups():      _save("groups.pkl", groups)
def save_students():    _save("students.pkl", students)
def save_disciplines(): _save("disciplines.pkl", disciplines)
def save_enrollments(): _save("enrollments.pkl", enrollment)

def load_all_data():
    global groups, students, disciplines, enrollment
    files = [
        ("groups.pkl", groups, {}),
        ("students.pkl", students, {}),
        ("disciplines.pkl", disciplines, {}),
        ("enrollments.pkl", enrollment, Enrollment()),
    ]
    for filename, target, default in files:
        path = DATA_DIR / filename
        if path.exists():
            with open(path, "rb") as f:
                loaded = pickle.load(f)
                if filename == "enrollments.pkl":
                    enrollment = loaded
                else:
                    target.clear()
                    target.update(loaded)

    for group_students in groups.values():
        for s in group_students:
            students[s.id] = s