import threading
import time

# Общий ресурс
counter = 0
lock = threading.Lock()


def worker(name, delay, is_daemon=False):
    global counter
    print(f"{name}: начал")
    for i in range(2):
        time.sleep(delay)
        # Критическая секция с состоянием гонки
        # lock.acquire()  # раскомментировать для защиты
        global counter
        temp = counter
        time.sleep(0.001)  # имитация прерывания
        counter = temp + 1
        # lock.release()
        print(f"{name}: counter = {counter}")
    print(f"{name}: завершил")


def main():
    # Демон-поток завершится при выходе из main
    t1 = threading.Thread(target=worker, args=("A", 0.5), daemon=False)
    t2 = threading.Thread(target=worker, args=("B", 0.3), daemon=True)

    t1.start()
    t2.start()

    # join - ждём завершения t1, но не t2 (демон завершится сам)
    t1.join()
    print("Main: t1 завершён, программа закончена (демон t2 прерван)")


if __name__ == "__main__":
    main()