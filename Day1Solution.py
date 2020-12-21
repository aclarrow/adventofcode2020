with open("Day1Input.txt") as f:
    numbers = f.read().splitlines()
    numbers = [int(i) for i in numbers] 
#print(numbers)

target = 2020

for i in numbers:
    if i < target:
        pair = target - i
        if pair in numbers:
            print("{} X {}".format(i,pair))
            print(i*pair)
            break
