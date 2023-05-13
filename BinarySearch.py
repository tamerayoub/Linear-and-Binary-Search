import time

# A is ordered list, key is what the function searches for, and returns true if found.


def BinarySearch(A, key):
    start = 1
    end = len(A) - 1
    found = False

    midpoint = (start + end) // 2

    while start <= end and found != True:

        print(midpoint, ":midpoint")
        print(start, ":start]", end, ":end]", "\n")

        if A[midpoint] == key:
            found = True
            print("Found")
        else:
            if key < A[midpoint]:
                midpoint = midpoint - 1
                print('Not Found. Decrement Midpoint')
            else:
                midpoint = midpoint + 1
                print('Not Found. Increment Midpoint')
    return found


key = 1

A = list(range(0, 100001))

t = time.process_time()
a = (BinarySearch(A, key))
elapsed_time = time.process_time() - t
print(elapsed_time)  # Note down this time in the table
