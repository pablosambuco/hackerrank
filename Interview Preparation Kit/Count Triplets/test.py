#!/bin/python3

# Complete the countTriplets function below.
def countTriplets(arr, r):
    q = 0
    arr_q = {}
    for i in reversed(arr):
        arr_q[i] = arr_q.get(i, 0) + 1
        q += arr_q.get(i * r, 0) * arr_q.get(i * r * r, 0)
    return q

if __name__ == "__main__":

    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    print(ans)
