import time
import random
import numpy

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterFibo(n):
    fib = [0 for i in range(n+1)] # pre-make a size n+1 list filled with 0
    for i in range(n+1):
        if i <= 1:
            fib[i] = i
        else:
            fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def iterFibo2(n):
    number_list = []
    if n<= 1:
        number_list.append(n)
    else:
        number_list = [1,1]
        for i in range(n):
            number_list.append(number_list[i] + number_list[i+1])
    result = number_list[n-1]
    return result






while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterFibo2(nbr) #fibo(nbr)
    ts = time.time() - ts
    ts2 = time.time()
    fibnumber2 = iterFibo(nbr)
    ts2 = time.time() - ts2
    ts3 = time.time()

    print("iterFibo(%d)=%d, time %.6f\n" %(nbr, fibonumber, ts))
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibnumber2, ts2))

