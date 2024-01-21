import time
from queue import Queue

# Створити чергу заявок
queue = Queue()

# Максимальна кількість запитів у черзі
MAX_QUEUE_SIZE = 5

def generate_request():
    num_request = 1
    for _ in range(MAX_QUEUE_SIZE):
        if queue.qsize() < MAX_QUEUE_SIZE:
            queue.put(num_request)
            print(f"Сформовано новий запит: Номер запиту {num_request}")
            num_request += 1
            time.sleep(2)

def process_request():
    while True:
        if not queue.empty():
            request = queue.get()
            print(f"Запит {request} обробляється ............. ")
            time.sleep(1)
        else:
            print("Черга порожня")
            time.sleep(1)
            break

if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
        user_input = input("Натисніть Enter, щоб продовжити, або введіть exit, щоб вийти: ")
        if user_input.lower() == 'exit':
            print("Бувай!")
            break
