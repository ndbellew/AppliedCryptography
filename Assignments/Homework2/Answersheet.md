# Homework 2
## Problem 1 Dice

### A

Entropy information is calculated by finding the entropy for each event and adding all of those numbers up. This was calculated by finding the Entropy of one die and then adding that 4 times for 4 events. 

- For One event: $2.585$

- For Four Events: $10.340$

### B

Following the logic in Part A, I created a list of four values, three of which are $1/6$ and the last value is $3/6$. This is because 3 of the 6 sides are now 5s meaning there is a 50% chance or $3/6$ chance of rolling a five. 

- For One Event: $1.792$

- For 5 Events: $ 8.962 $

### C

The best way to maximize entropy for a die is to leave it as it is, having an equal chance to roll any of the 6 numbers will give the die the highest entropy value. 
The Dice should be marked `[1, 2, 3, 4, 5, 6]` to achieve a maximum entropy of $2.585$

### D


### E

## Problem 2. Balls in a Bin

### A

### B

### C

The total number of balls is increased from nine to eleven. The number of red balls is increased from three to four and yellow is increased from two to three. the way to calculate this event is to modify the list of values:
```py
import math
listOfValues = [3/9,2/9,4/9] #initial set of values is 9 the lists sets red, yellow and green respectively.
newListOfValues = [4/11, 3/11, 4/11] # set the same as the above list respectively.\
EntropyValue = 0
for value in List:
    EntropyValue += Value * math.log2(1/Value)
print(EntropyValue)
```
The first value will equal **1.792** the new list of values will instead make **1.573**
### D

### E

### F

## Problem 3. Proving stuff

### A

### B

### C

## Problem 4 Euclidean Algorithm

### A

### B

### C

### D

## Problem 5 More Euclidean Algorithm

### A

### B

### C

### D

## Problem 6 [No Title]

### A

### B
