#!/usr/bin/python

string = "I am am a good good teacher"
lis = string.split()
seen = set()
uniq = []
for x in lis:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
res = ' '.join(uniq)
print(res)