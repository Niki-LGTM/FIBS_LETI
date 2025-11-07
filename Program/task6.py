import copy

class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number
    
    def __str__(self):
        return f"{self.name} {self.surname} - №{self.number}"


class StudentGroup:
    def __init__(self, group_number, creation_year):
        self.group_number = group_number
        self.creation_year = creation_year
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student_by_number(self, number):
        for student in self.students:
            if student.number == number:
                self.students.remove(student)
                return
        print("Студент не найден")
    
    def __str__(self):
        result = f"Группа {self.group_number} ({self.creation_year}):\n"
        for student in self.students:
            result += f"  {student}\n"
        return result


group1 = StudentGroup("4586", 2024)

group1.add_student(Person("Иван", "Новицкий", 1))
group1.add_student(Person("Георгий", "Рожков", 2))
group1.add_student(Person("Никита", "Ротчев", 3))
group1.add_student(Person("Игорь", "Рубцов", 4))

group2 = copy.deepcopy(group1)
group2.group_number = "4586-копия"

group2.remove_student_by_number(2)
group2.remove_student_by_number(4)

print("ОРИГИНАЛЬНАЯ ГРУППА:")
print(group1)

print("КОПИЯ ГРУППЫ:")
print(group2)
