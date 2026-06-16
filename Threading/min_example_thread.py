import threading
import time


def worker(name, delay):
    print(f"{name} started")
    time.sleep(delay)  # I/O-ожидание (отпускает GIL)
    print(f"{name} finished")


def main_thread():
    t1 = threading.Thread(target=worker, args=("A", 2))
    t2 = threading.Thread(target=worker, args=("B", 1))

    t1.start()
    t2.start()

    t1.join()  # ждём завершения A
    t2.join()  # ждём завершения B
    print("All done")

main_thread()