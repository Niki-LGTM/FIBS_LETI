import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import matplotlib as mpl

# Увеличим шрифты для лучшей читаемости
mpl.rcParams['font.size'] = 12
mpl.rcParams['figure.figsize'] = (14, 8)

# Параметры цепи
L1 = 0.889
C1 = 0.5  
C2 = 0.9

# Матрицы системы
A = np.array([
    [0, 1/L1, 0],
    [-1/C1, -1/C1, -1/C1],
    [0, -1/C2, -2/C2]
])

B = np.array([
    [0],
    [1/C1],
    [1/C2]
])

# Параметры расчета
dt = 0.06
t_end = 8  # Уменьшим время для лучшего обзора
steps = int(t_end / dt)

# Начальные условия
x = np.array([[0], [0], [0]])  # [i_L1, u_C1, u_C2]
u = 1  # Ступенчатое воздействие

# Массивы для хранения результатов
time = np.zeros(steps)
h1_numeric = np.zeros(steps)  

# Численное интегрирование методом Эйлера
for i in range(steps):
    time[i] = i * dt
    h1_numeric[i] = x[2, 0]  # u_C2
    x = x + dt * (A @ x + B * u)

# Аналитическое решение
def h1_analytic(t):
    return 0.5 - 0.464 * np.exp(-3.33 * t) + 0.391 * np.exp(-0.445 * t) * np.cos(1.14 * t + 1.658)


t_dense = np.linspace(0, t_end, 1000)
h1_analytic_dense = h1_analytic(t_dense)
plt.figure(figsize=(16, 10))

# График 1: Совмещенные графики
plt.subplot(2, 2, 1)
plt.plot(t_dense, h1_analytic_dense, 'r-', linewidth=3, label='Аналитическое решение', alpha=0.8)
plt.plot(time, h1_numeric, 'bo-', markersize=4, linewidth=1.5, label='Численное решение (Эйлер)', alpha=0.7)
plt.axhline(y=0.5, color='green', linestyle='--', alpha=0.7, label='Установившееся значение = 0.5')
plt.xlabel('Время t, с')
plt.ylabel('$h_1(t)$')
plt.title('Сравнение аналитического и численного решений', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(0, t_end)
plt.ylim(-0.1, 0.7)

# График 2: Крупный план начального участка
plt.subplot(2, 2, 2)
t_initial = 2  # Первые 2 секунды
mask = time <= t_initial
mask_dense = t_dense <= t_initial

plt.plot(t_dense[mask_dense], h1_analytic_dense[mask_dense], 'r-', linewidth=3, label='Аналитическое')
plt.plot(time[mask], h1_numeric[mask], 'bo-', markersize=5, linewidth=2, label='Численное')
plt.xlabel('Время t, с')
plt.ylabel('$h_1(t)$')
plt.title('Начальный участок (0-2 с)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# График 3: Разность между решениями
plt.subplot(2, 2, 3)
h1_analytic_at_points = h1_analytic(time)
difference = h1_numeric - h1_analytic_at_points

plt.plot(time, difference, 'g-', linewidth=2, label='Разность (числ. - аналит.)')
plt.axhline(y=0, color='red', linestyle='--', alpha=0.5)
plt.xlabel('Время t, с')
plt.ylabel('Разность')
plt.title('Погрешность численного решения', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# График 4: Крупный план установившегося режима
plt.subplot(2, 2, 4)
t_steady = 4  # С 4 секунд
mask_steady = time >= t_steady
mask_dense_steady = t_dense >= t_steady

plt.plot(t_dense[mask_dense_steady], h1_analytic_dense[mask_dense_steady], 'r-', linewidth=3, label='Аналитическое')
plt.plot(time[mask_steady], h1_numeric[mask_steady], 'bo-', markersize=4, linewidth=1.5, label='Численное')
plt.axhline(y=0.5, color='green', linestyle='--', alpha=0.7, label='0.5')
plt.xlabel('Время t, с')
plt.ylabel('$h_1(t)$')
plt.title('Установившийся режим (4-8 с)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(0.49, 0.51)  # Узкий диапазон для точного сравнения

plt.tight_layout()
plt.show()

# Вывод количественных характеристик
print("="*60)
print("СРАВНЕНИЕ АНАЛИТИЧЕСКОГО И ЧИСЛЕННОГО РЕШЕНИЙ")
print("="*60)

# Ключевые точки для сравнения
key_times = [0.1, 0.5, 1.0, 2.0, 5.0]
print(f"{'Время':<8} {'Аналит.':<10} {'Числен.':<10} {'Разность':<10} {'Отн. погр., %':<15}")
print("-" * 60)

for t in key_times:
    idx = int(t / dt)
    if idx < len(time):
        analytic_val = h1_analytic(time[idx])
        numeric_val = h1_numeric[idx]
        diff = numeric_val - analytic_val
        rel_error = abs(diff / analytic_val) * 100 if analytic_val != 0 else 0
        
        print(f"{t:<8.1f} {analytic_val:<10.4f} {numeric_val:<10.4f} {diff:<10.4f} {rel_error:<15.2f}")

print(f"\nМаксимальная погрешность: {np.max(np.abs(difference)):.6f}")
print(f"Средняя погрешность: {np.mean(np.abs(difference)):.6f}")
print(f"Установившееся значение (числ.): {h1_numeric[-1]:.6f}")
print(f"Установившееся значение (аналит.): {h1_analytic(t_end):.6f}")