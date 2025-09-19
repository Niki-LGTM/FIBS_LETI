import datetime

student_id = 458617
last_two_digits = student_id % 100
group_number = (student_id // 100) % 10000
faculty_code = (student_id // 10000) % 10

year_of_admission_digit = student_id // 100000  
year_of_admission = 2020 + year_of_admission_digit  

now = datetime.datetime.now().year
course_number = now - year_of_admission + 1

surname = "Ротчев"
name = "Никита"
patronymic = "К"

print("╔" + "═" * 39 + "╗")
print("║" + " СТУДЕНЧЕСКИЙ БИЛЕТ ".center(39, ' ') + "║")
print("╠" + "═" * 39 + "╣")
print("║" + f"{surname} {name[0]}.{patronymic[0]}.".center(39) + "║")
print("╠" + "═" * 39 + "╣")

data = [
    ("Курс", f"{course_number}"),
    ("Факультет", f"{faculty_code}"),
    ("Группа", f"{group_number}"),
    ("Подгруппа", f"{group_number % 100}"),
    ("Номер в ведомости", f"{last_two_digits}"),
    ("Номер зачетки", f"{student_id}"),
]

for label, value in data:
    print(f"║ {label:<17} : {value:>17} ║")

print("╚" + "═" * 39 + "╝")
