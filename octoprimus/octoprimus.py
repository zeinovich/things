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

        print(f"{number / limit * 100:06.3f}%")
        sys.stdout.write("\033[F")

    return primes


primes = get_primes(200000)

primes = np.array(primes)
primes_5000 = primes[primes < 5000]
primes_20000 = primes[primes < 20000]
primes_50000 = primes[primes < 50000]

figure, axis = plt.subplots(2, 2, figsize=(12, 12))

axis[0, 0].scatter(primes_5000 * np.cos(primes_5000), primes_5000 * np.sin(primes_5000), s=0.1, c='b')  
axis[0, 1].scatter(primes_20000 * np.cos(primes_20000), primes_20000 * np.sin(primes_20000), s=0.1, c='m')    
axis[1, 0].scatter(primes_50000 * np.cos(primes_50000), primes_50000 * np.sin(primes_50000), s=0.1, c='g')    
axis[1, 1].scatter(primes * np.cos(primes), primes * np.sin(primes), s=0.03, c='r')    

axis[0, 0].locator_params(nbins=3)
axis[0, 1].locator_params(nbins=3)
axis[1, 0].locator_params(nbins=3)
axis[1, 1].locator_params(nbins=3)

plt.show()