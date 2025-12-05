from dataclasses import dataclass
from typing import Set

@dataclass
class Student:
    id: int
    name: str
    group: str

@dataclass
class Discipline:
    code: str
    title: str

    def __post_init__(self):
        self.code = self.code.upper()

class Enrollment:
    def __init__(self):
        self.mapping: dict[str, Set[int]] = {}  # discipline_code → set(student_id)

    def add(self, disc_code: str, student_id: int):
        self.mapping.setdefault(disc_code, set()).add(student_id)

    def get_students(self, disc_code: str) -> Set[int]:
        return self.mapping.get(disc_code, set())