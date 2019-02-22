import sys
import os
ExampleArray = [2, 3, 1, 9, 7, 6, 8, 8, 6, 3, 2, 1, 4, 12]

print("Print ExampleArray am Anfang")
for i in ExampleArray:
    print(i)

for i in range(1, len(ExampleArray)):
    for j in range(0, i):
        if ExampleArray[i-j] < ExampleArray[i-j-1]:
            ExampleArray[i-j], ExampleArray[i-j-1] \
                = ExampleArray[i-j-1], ExampleArray[i-j]

print("Am Ende")
for i in ExampleArray:
    print(i)
