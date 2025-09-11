""" Module test program for lr1. """



NAME = 'Ротчев Н.К.'
GROUP = '4586'
STRING = "Тестовая программа " + NAME + " группа " + GROUP
with open("test.txt", 'ta', encoding="utf-8") as f:
    print(STRING, sep="\n", file=f)
    f.close()
print(STRING)
print ("тестовый", "вывод", "на экран")
N = 25
X = 2.5
A = 11.1 + N
print(N * 2 + X)    # проверить значение X в отладчике
print(N - X)        # проверить значение A в отладчике
print(N * X)        # проверить значение N в отладчике
print(N / X)        # проверить значение N / X в отладчике
print(N ** X)
A += X
print(A)            # проверить значение переменной A в отладчике
ARGUMENT_1 = 45
ARGUMENT_2 = 45
print(f"Ответ:{ARGUMENT_1 + ARGUMENT_2}")
