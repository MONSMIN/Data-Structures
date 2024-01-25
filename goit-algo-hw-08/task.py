import heapq

cables = [4, 10, 3, 5]

heapq.heapify(cables)
print("Початкова купа:", cables)

def connect_cables(cables):
    total_sum = 0

    while len(cables) > 1:
        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)
        
        connection_cable = cable_1 + cable_2
        total_sum += connection_cable
        
        heapq.heappush(cables, connection_cable)
        print(f"Витрати на з'єднання {cable_1} та {cable_2}: {connection_cable}")
        print("Купа після з'єднання:", cables)
        

    return total_sum

result = connect_cables(cables)
print(f"Мінімальні витрати для з'єднання кабелів: {result}")
