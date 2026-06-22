import time
import matplotlib.pyplot as plt

# Interpolation Search Function
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and key >= arr[low] and key <= arr[high]:

        comparisons += 1

        # Avoid division by zero
        if arr[high] == arr[low]:
            if arr[low] == key:
                return low, comparisons
            return -1, comparisons

        # Interpolation formula
        pos = low + ((high - low) * (key - arr[low])) // (arr[high] - arr[low])

        if arr[pos] == key:
            return pos, comparisons

        elif arr[pos] < key:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


# MAIN PROGRAM

n = int(input("Enter number of elements: "))

# Generate uniformly distributed sorted array
arr = list(range(1, n + 1))

print("\nGenerated Array:")
print(arr)

key = int(input("\nEnter search key: "))

# Measure execution time
start_time = time.perf_counter()

position, comparisons = interpolation_search(arr, key)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Display results
print("\n----- RESULTS -----")

if position != -1:
    print(f"Element {key} found at position {position}")
else:
    print(f"Element {key} not found")

print(f"Number of Comparisons: {comparisons}")
print(f"Execution Time: {execution_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(log log n)")
print("Worst Case   : O(n)")

print("\nSpace Complexity: O(1)")

# PERFORMANCE ANALYSIS GRAPH

sizes = [100, 500, 1000, 5000, 10000, 20000]
times = []

for size in sizes:
    test_arr = list(range(1, size + 1))
    test_key = size // 2

    start = time.perf_counter()
    interpolation_search(test_arr, test_key)
    end = time.perf_counter()

    times.append(end - start)

# Plot graph
plt.plot(sizes, times, marker='o')
plt.title("Interpolation Search Performance Analysis")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.show()
