import math
from multiprocessing import Process, Queue
def fact(x, q):
    q.put(math.factorial(x))
if __name__ == "__main__":
    q = Queue()
    ps = [Process(target=fact, args=(i, q)) for i in range(1, 11)]
    for p in ps: p.start()
    for p in ps: p.join()
    print([q.get() for _ in range(10)])