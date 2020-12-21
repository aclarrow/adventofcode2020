import numpy
from itertools import combinations


with open("Day1Input.txt") as f:
    numbers = f.read().splitlines()
    numbers = [int(i) for i in numbers] 
#print(numbers)

target = 2020

def findTrio(pool, key): 
    def hitstarget(val): 
        return sum(val) == key  
    return list(filter(hitstarget, list(combinations(pool, 3)))) 

print(findTrio(numbers, 2020)) 
print(numpy.prod(findTrio(numbers, 2020)))