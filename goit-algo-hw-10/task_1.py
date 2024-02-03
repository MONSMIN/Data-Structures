import pulp

# Створюємо модель оптимізації
model = pulp.LpProblem(name="optimal_production", sense=pulp.LpMaximize)

# Визначаємо змінні рішення - кількість "Лимонаду" та "Фруктового соку" для виробництва
x1 = pulp.LpVariable(name="lemonade_units", lowBound=0, cat="Intenger")
x2 = pulp.LpVariable(name="fruit_juice_units", lowBound=0, cat="Integer")

# Визначаємо функцію максимізації
model += x1 + x2, "Total_products"

# Додаємо обмеження на ресурси
model += 2 * x1 + x2 <= 100, "water_constraint"
model += x1 <= 50, "sugar_constraint"
model += x1 <= 30, "lemon_juice_constraint"
model += 2 * x2 + x1 <= 40, "fruit_puree_constraint"

# Розв'язуємо модель
model.solve()

# Результати
print("-" * 40)
print("| Оптимальний план виробництва          |")
print("-" * 40)
print(f"| Одиниці Лимонаду: {int(x1.varValue):<19} |")
print(f"| Одиниці Фруктового соку: {int(x2.varValue):<12} |")
print(f"| Максимальна кількість продуктів: {int(model.objective.value()):<4} |")
print("-" * 40)
