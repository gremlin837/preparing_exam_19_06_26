import threading, time
threading.Thread(target=lambda: [time.sleep(1) or print("Демон") for _ in range(10)], daemon=True).start()
time.sleep(2)
print("Основной завершён")