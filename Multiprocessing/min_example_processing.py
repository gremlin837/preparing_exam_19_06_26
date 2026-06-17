import multiprocessing as mp

def cpu_heavy(n):
    return sum(i * i for i in range(n))

def main_mp():
    with mp.Pool(processes=2) as pool:
        results = pool.map(cpu_heavy, [5_000_000, 5_000_000])
    print(results)

if __name__ == '__main__':
    main_mp()