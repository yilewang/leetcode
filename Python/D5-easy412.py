import numpy as np

def fizzBuzz(n):
    arr = ['1'] * n
    for i in range(1, n+1, 1):
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
            arr[i-1] = result
            continue
        elif i % 3 == 0:
            result = "Fizz"
            arr[i-1]= result
            continue
        elif i % 5 == 0:
            result = "Buzz"
            arr[i-1]= result
            continue
        else:
            arr[i-1] = str(i)
            continue
    return arr

print(fizzBuzz(100))