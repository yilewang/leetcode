import numpy as np

def factorial_trail_zeros(n):
    factorial = 1
    for n in range(1, n+1):
	    factorial = factorial*n

    fact = str(factorial)
    y = np.zeros(len(fact))

    f = list(map(int, str(factorial)))
    count = 0
    for x in range(len(f)-1, 0, -1):
        if f[x] == 0:
	        count+=1
        else:
            break
    print('The factorial number is : ', factorial)
    print('The trail zeros number is : ', count)

factorial_trail_zeros()