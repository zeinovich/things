import matplotlib.pyplot as plt
import numpy as np
import sys
import time

def timing_wrapper(func):
    def timing(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'[INFO] {func.__name__} executed in {(end - start):.3f}s')
        return result
    return timing

@timing_wrapper
def get_primes(limit):
    primes = [2]
    for number in range(3, limit+1, 2):
        div_set = []
        for prime in primes:
            div_set.extend([number % prime])

            if number%prime == 0: 
                break

        P = (0 not in div_set)

        if not P: 
            continue
        primes.extend([number])

        print(f"{number/limit*100:06.3f}%")
        sys.stdout.write("\033[F")

    return primes


primes = get_primes(100000)
primes = np.array(primes)

plt.scatter(primes * np.cos(primes), primes * np.sin(primes), s=0.1, c='b')    

plt.gcf().set_size_inches(12, 12)
plt.show()