import pickle
from typing import List, Optional
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    student_number: int

class Group(BaseModel):
    number: str
    students: List[Student] = []

class GroupManager:
    def __init__(self, filename: str = "groups.bin"):
        self.filename = filename
        self.groups: List[Group] = []
    
    def save_to_file(self):
        """Сохранить группы в бинарный файл"""
        with open(self.filename, 'wb') as f:
            pickle.dump(self.groups, f)
    
    def load_from_file(self):
        """Загрузить группы из бинарного файла"""
        try:
            with open(self.filename, 'rb') as f:
                self.groups = pickle.load(f)
        except FileNotFoundError:
            self.groups = [
                Group(number="student_group"),
                Group(number="4586")
            ]
            student1 = Student(name="Иван Иванов", student_number=1)
            student2 = Student(name="Мария Петрова", student_number=2)
            student3 = Student(name="Алексей Сидоров", student_number=3)
            
            self.groups[0].students.append(student3)  
            self.groups[1].students.append(student1)  
            self.groups[1].students.append(student2)
        
        self.save_to_file()
    
    def get_group(self, group_number: str) -> Optional[Group]:
        """Найти группу по номеру"""
        for group in self.groups:
            if group.number == group_number:
                return group
        return None
    
    def add_student_to_group(self, group_number: str, student: Student):
        """Добавить студента в группу"""
        group = self.get_group(group_number)
        if group:
            for existing_student in group.students:
                if existing_student.student_number == student.student_number:
                    raise ValueError(f"Студент с номером {student.student_number} уже существует")
            group.students.append(student)
            return True
        else:
            new_group = Group(number=group_number, students=[student])
            self.groups.append(new_group)
            return True
    
    def remove_student_from_group(self, group_number: str, student_number: int):
        """Удалить студента из группы по номеру в ведомости"""
        group = self.get_group(group_number)
        if group:
            initial_length = len(group.students)
            group.students = [s for s in group.students if s.student_number != student_number]
            return len(group.students) < initial_length
        return False


group_manager = GroupManager()