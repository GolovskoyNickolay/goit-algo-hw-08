import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з кабелів
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Дістаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх і обчислюємо вартість
        combined = first + second
        total_cost += combined

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, combined)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальна вартість з'єднання:", min_cost_to_connect_cables(cables))
