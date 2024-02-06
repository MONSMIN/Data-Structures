import random
import matplotlib.pyplot as plt

from prettytable import PrettyTable
from collections import defaultdict

nums = 100000

counts = defaultdict(int)

for _ in range(nums):
    dice = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    counts[dice + dice_two] += 1

probabilities = {key: count / nums for key, count in counts.items()}

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
