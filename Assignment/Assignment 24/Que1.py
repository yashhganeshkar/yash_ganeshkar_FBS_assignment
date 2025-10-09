
import threading

partial_sums = [0, 0, 0, 0]

def sum_squares(start, end, index):
    total = 0
    for num in range(start, end + 1):
        total += num * num
    partial_sums[index] = total

threads = []
range_size = 100 // 4

for i in range(4):
    start = i * range_size + 1
    end = (i + 1) * range_size if i < 3 else 100
    thread = threading.Thread(target=sum_squares, args=(start, end, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_sum = sum(partial_sums)
print(f"Sum of squares from 1 to 100 is: {total_sum}")
