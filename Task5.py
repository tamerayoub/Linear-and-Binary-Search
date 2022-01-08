# Tamer Ayoub

import time

import timeit


def LinearSearch(A, key):
    current = 1
    found = False

    AlistSize = len(A)

    while current <= AlistSize and found != True:
        if(A[current] == key):
            found = True
            print('Found')
        else:
            current = current + 1
            print('Not Found')

    return found


A = list(range(0, 100001))


key = 99999

""" t = timeit.default_timer()

# replace this line with appropriate function name
a = LinearSearch(A, key)

elapsed_time = timeit.default_timer() - t
print(elapsed_time) """


t = time.process_time()

# replace this line with appropriate function name
a = LinearSearch(A, key)
elapsed_time = time.process_time() - t
print(elapsed_time)


# ATTENTION READ TIME CASE RESULTS BELOW

# Best case is O(1), runs once and finds match
# Best Case Time Result: 0.00026980, 0.000542499, .00036900

# Worse case is O(n), runs all the way and doesnt find any matches
# Worse case Time Results: 2.546875, 2.640625, 2.453125
