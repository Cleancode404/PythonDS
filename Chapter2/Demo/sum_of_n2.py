#test how long to compute sum from 0 to 10,000
import time

def sum_of_n_2(n):
    start = time.time()
    sum = 0

    for i in range(1, n+1):
        sum = sum + i
    end = time.time()
    return(sum, end-start)

print(sum_of_n_2(10000))