
GROUP = []

class Person:

    COLUMN_WIDTHS = {
        'name': 15,
        'surname': 15, 
        'number': 10
    }
    SEPARATOR_CHAR = '='

    def __init__(self,name,surname,number):
        self.name = name
        self.surname = surname
        self.number = number
    
    def __str__(self):
        return f"Студент: {self.name} {self.surname} (№{self.number})"
    
    def __repr__(self):
        return f"Person(name='{self.name}', surname='{self.surname}', number={self.number})"
    
    @staticmethod
    def print_separator(char=None):
        if char is None:
            char = Person.SEPARATOR_CHAR
        total_width = (Person.COLUMN_WIDTHS['name'] + 
                      Person.COLUMN_WIDTHS['surname'] + 
                      Person.COLUMN_WIDTHS['number'] + 2)
        print(char * total_width)

    @classmethod
    def print_header(cls):
        print(f"{'Имя':<{cls.COLUMN_WIDTHS['name']}} "
              f"{'Фамилия':<{cls.COLUMN_WIDTHS['surname']}} "
              f"{'Номер':>{cls.COLUMN_WIDTHS['number']}}")
        cls.print_separator()

    #--------------гетеры-----------------#
    @property
    def getName(self):
        print(f"Name: {self.name}")
    @property
    def getSurname(self):
        print(f"Surname: {self.surname}")
    @property
    def getNumber(self):
        print(f"Number: {self.number}")
    #--------------сетеры-----------------#
    def setName(self,name):
        self.name = name
    def setSurname(self,surname):
        self.surname = surname
    def setNumber(self,number):
        self.number = number

def invate_group():
    GROUP.append(Person("Иван","Новицкий",15))
    GROUP.append(Person("Георгий","Рожков",16))
    GROUP.append(Person("Никита","Ротчев",17))
    GROUP.append(Person("Игорь","Рубцов",18))
    GROUP.append(Person("Григорий","Ручьев",19))
    GROUP.append(Person("Анастасия","Тимофеева",20))

invate_group()

for person in GROUP:
    print(f"Name: {person.name}, Surname: {person.surname}, Number: {person.number}")

print("=== Таблица с настройками по умолчанию ===")
Person.print_header()
for person in GROUP:
    print(person)
Person.print_separator()
