import random
import time
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


items = [10000, 50000, 100000, 500000]
d = []
r = []
retries = 5
for i in items:
    d_time = []
    r_time = []
    for k in range(retries):
        array = [random.randint(0, i) for _ in range(i)]
        d_start = time.time()
        deterministic_quick_sort(array)
        d_end = time.time()
        d_time.append(d_end - d_start)
        r_start = time.time()
        randomized_quick_sort(array)
        r_end = time.time()
        r_time.append(r_end - r_start)
    print(f"\nРозмір масиву: {i}")
    print(f"Рандомізований QuickSort: {sum(r_time)/retries:6.4f} секунд")
    print(f"Детермінований QuickSort: {sum(d_time)/retries:6.4f} секунд")
    r.append(sum(r_time) / retries)
    d.append(sum(d_time) / retries)


# create data


# plot lines
plt.plot(items, r, label="Random", color="orange")
plt.plot(items, d, label="Deterministic", color="blue")
plt.legend()
plt.xlabel("Array size", fontsize=14, color="darkgreen")
plt.ylabel("average time", fontsize=14, color="darkgreen")
plt.xticks(rotation=45, fontsize=10, color="darkgreen")
plt.yticks(fontsize=10, color="darkgreen")
plt.show()
print("DONE")
