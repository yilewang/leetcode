### Python Leetcode Easy 14

import numpy as np
import re

def longest_prefix(str_list):
    nn = len(str_list)
    n2 = len(min(str_list, key = len))
    tmp1 = [[]] * nn
    tmp2 = ['j']*n2
    for i in range(0,nn,1):
        tmp = ['j']*len(str_list[i])
        ni = len(str_list[i])
        for n in range(0, ni, 1):
            tmp[n] = str_list[i][n:n+1]
        tmp1[i] = tmp    
    for x in range(0, n2, 1):
        tp = [[]]*nn
        for a in range(0, nn, 1):
            tp[a] = tmp1[a][x]
        tmp2[x] = ''.join(tp)
    co =0

    for x in range(0, n2, 1):
        uq = len(set(tmp2[x]))
        if uq == 1:
            co+=1
        else:
            break
    return co

s = ['flower', 'flate', 'flag', 'flame', 'florida', 'fluence', 'flight', 'flood']
longest_prefix(s)

        


