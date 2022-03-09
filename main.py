import csv
import math
from operator import indexOf
list = [0,0,0,0,0,0,0]
temp = 0
with open('list.csv', newline='') as f:
    read = csv.reader(f, delimiter=',')
    for row in read:
        list[temp] = row
        temp += 1
url = input()
final = ""
'''
for i in range(1, 6):
    final += list[0][indexOf(list[i], url[i - 1])]
print(final)
'''
for i in range(0, len(url)):
    final += list[0][indexOf(list[i % 6 + 1], url[i])]
print(final)