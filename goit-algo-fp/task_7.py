import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from collections import defaultdict

def simulate_dice_rolls(num_simulations):
    """Моделює кидання двох кубиків та обчислює ймовірності сум чисел."""
    counts = defaultdict(int)

    for _ in range(num_simulations):
        dice = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        counts[dice + dice_two] += 1

    probabilities = {key: count / num_simulations for key, count in counts.items()}
    return probabilities

def display_results(probabilities):
    """Виводить результати у вигляді таблиці та графіка."""
    table = PrettyTable(["Сума", "Ймовірність"])

    for dice, prob in probabilities.items():
        table.add_row([dice, f"{prob * 100:.2f}%"])

    table.sortby = "Сума"
    print(table)

    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Імовірність сум при киданні двох кубиків')
    plt.show()

def main():
    num_simulations = 100000
    probabilities = simulate_dice_rolls(num_simulations)
    display_results(probabilities)

if __name__ == "__main__":
    main()
