class Item:
    def __init__(self, cost, calories):
        self.cost = cost
        self.calories = calories
        self.calories_per_cost = calories / cost
        
def greedy_algorithm(items: dict[str, dict[str, int]], budget: int) -> tuple[int, list[str]]:
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []
    for item, data in sorted_items:
        if budget >= data['cost']:
            budget -= data['cost']
            total_calories += data['calories']
            selected_items.append(item)
    return total_calories, selected_items
    

def dynamic_programming(items, budget):
    # Ініціалізація матриці для збереження найкращої калорійності для кожного бюджету
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    # Заповнюємо матрицю залежно від бюджету та кількості доступних страв
    for i, (item, data) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if data['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], data['calories'] + dp[i - 1][j - data['cost']])
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлення оптимального набору страв
    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]['cost']
        i -= 1

    return selected_items, dp[len(items)][budget]

    
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}




if __name__ == "__main__":

    budget = 100
    total_calories, selected_items = greedy_algorithm(items, budget)
    print("-" * 50)
    print("\033[92mРезультат роботи жадібного алгоритму\033[0m")
    print(f"Сума калорій: {total_calories}")
    print(f"Набір страв: {', '.join(selected_items)}")
    print("-" * 50)
    print("\033[92mРезультат роботи алгоритму динамічного програмування\033[0m")
    result_dynamic = dynamic_programming(items, budget)
    print(f"Сума калорій: {result_dynamic[1]}")
    print(f"Набір страв: {result_dynamic[0]}")
    print("-" * 50)
