import random
import timeit
import matplotlib.pyplot as plt


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def measure_time(func, arr, repeats=5):
    times = []
    for _ in range(repeats):
        arr_copy = arr[:]
        t = timeit.timeit(lambda: func(arr_copy), number=1)
        times.append(t)
    return sum(times) / repeats


def run_comparison():
    sizes = [10_000, 50_000, 100_000, 500_000]
    det_times = []
    rand_times = []

    for size in sizes:
        print(f"\nРозмір масиву: {size}")
        array = [random.randint(0, 1_000_000) for _ in range(size)]

        rand_time = measure_time(randomized_quick_sort, array)
        print(f"  Рандомізований QuickSort: {rand_time:.4f} секунд")

        det_time = measure_time(deterministic_quick_sort, array)
        print(f"  Детермінований QuickSort: {det_time:.4f} секунд")

        rand_times.append(rand_time)
        det_times.append(det_time)

    print("\n📊 Підсумкова таблиця:")
    print(f"{'Size':<10}{'Randomized (s)':<20}{'Deterministic (s)'}")
    for s, r, d in zip(sizes, rand_times, det_times):
        print(f"{s:<10}{r:<20.4f}{d:.4f}")

    plt.plot(sizes, rand_times, marker='o', label="Randomized QuickSort")
    plt.plot(sizes, det_times, marker='x', label="Deterministic QuickSort")
    plt.title("Порівняння часу сортування QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час (секунди)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_comparison()
