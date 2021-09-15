
## climbing stairs
import numpy as np
import math

def climbing(n):
    C = 0
    if n/2 % 1 == 0:
        for s in range(0, n+1, 2):
            m = (n - s*1)/2
            if m >= s:
                re = math.factorial(np.sum(m+s))/(math.factorial(s)*math.factorial(np.sum(m+s)-s))
            else:
                re = math.factorial(np.sum(m+s))/(math.factorial(m)*math.factorial(np.sum(m+s)-m))
            C +=re
            

    else:
        for m in range(0, int(n/2)+1, 1):
            s = n - m*2
            if s >= m:
                re = math.factorial(np.sum(m+s))/(math.factorial(m)*math.factorial(np.sum(m+s)-m))
            else:
                re = math.factorial(np.sum(m+s))/(math.factorial(s)*math.factorial(np.sum(m+s)-s))
            C +=re
    return int(C)



for i in range (1, 45, 1):
    result = climbing(i)
    print("The number of distinct climbing stairs methods is :" , result)
        
    



