import math
from multiprocessing import Pool
def fact(x):
    return math.factorial(x)
if __name__ == "__main__":
    # Пул из 5 процессов
    with Pool(processes=5) as pool:
        results = pool.map(fact, range(1, 11))
        print(results)