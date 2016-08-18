#!/usr/bin/env python3
lines = ''
with open("log1.txt") as fobj1:
    line1 = fobj1.read() 
with open("log2.txt") as fobj2:
    line2 = fobj2.read()
lines = line1 + line2
result = {}
for line in lines.splitlines():
    if line[11] == '<':
        i = line[12:].split('>')[0]
        result[i] = result.get(i, 0) + 1
       
for i in result.keys():
    j = i + '\t' + str(result[i])
    print(j)
