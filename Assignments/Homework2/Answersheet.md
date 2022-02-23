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

Rolling two dice and only monitoring the sum means that the numbers I use will be a little different from a single die. The numbers I will be monitoring is 2-12 (it starts at 2 because you cannot roll a 1 on two dice), because the 11 possible numbers can be made from multiple combinations of dice the probability is actually over 36 possibilities instead of 11. For each die roll if you add up each combination from Die A and Die B, the number of possibilities should be 36 where there are 6 possible combinations for a sum of 7. This makes these fractions for calculating Entropy = `[1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36,1/36]`. 
Calculating the Entropy from this I get $3.2744$

## Problem 2. Balls in a Bin

### A

In this problem there are 9 balls total, 2 are yellow, 3 are red, and 4 are green. So the set to calculate should be `[2/9,3/9,4/9]` the calculated entropy for a single event is $1.5726$

### B
Not figured out yet
$\begin{aligned}
Bias(\hat{\theta})  &= E(\hat{\theta}) - \theta \\
                    &= E(2 \bar{X} -1) - \theta \\
                    &= \frac{2}{n}\sum_{i=1}^n E(X_i) -1 -\theta \\
                    &= 2E(X) - 1 - \theta \\
                    &= 2 \cdot \frac{\theta+1}{2} - 1 - \theta \\
                    &= 0 \\
\end{aligned}$


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

The best way to create the highest entropy value is to ensure that the probability of pulling any ball is as even as possible. So to take the ball set `[4/11, 3/11, 4/11]` where there are 4 red balls, 3 yellow balls, and four green balls respectively. In maximize entropy by adding or removing a single ball of any color, a yellow ball must be added such that the set would equal `[4/12, 4/12, 4/12]`. This makes an entropy value of $1.585$


### E



### F

## Problem 3. Proving Modular Arithmetic

### A

This proof is relatively simple, plugging in the value for b into the a equation and foiling the answer. The basis of this is that if you take $\mod n$ of $\mod n$ then you will always get the exact same result. Such that $ X \mod n == X \mod n \mod n $

$\begin{aligned}
a = b (\mod n) and \; b = c (\mod n)  \therefore \;\; & a = c (\mod n) \\
& if \; \; b = c (\mod n) then  \\
& a = c (\mod n) (\mod n) \\
& a = c (\mod n) (\mod n) \equiv c (\mod n) \\
\end{aligned}$

### B

To prove this I used the quotient remainder theorem to redefine a and b in terms of remainders. Below I set showed that $a = cq_1 + r_1$ and $b = cq_2 + r_2$ therefore $a \mod n = r_1$ and $b \mod n = r_2$. By setting and b to this I can prove the theorem using simple substitution once the equations are foiled. The $ (n(q_1-q_2) + r_1 - r_2)$ step is completed by removing the n due to the fact that n mod n is 0. That step leaves the remainders which as noted above should be a mod n and b mod n therein proving the Modular Subtraction Rule. 

$\begin{aligned}
& a = nq_1 + r_1 where 0 \le r_1 < n \therefore \; a \mod n = r_1 \\
& b = nq_2 + r_2 where 0 \le r_2 < n \therefore \; b \mod n = r_2 \\
& (a-b)\mod n = (nq_1 + r_1 - nq_2 - r_2) \mod n \\
& (a-b)\mod n = (n(q_1-q_2) + r_1 - r_2) \mod n \\
& (a-b)\mod n = ( r_1 - r_2) \mod n \\ 
& (a \mod n - b \mod n) \mod n = (r_1 - r_2) \mod n
\end{aligned}$

### C

## Problem 4 Euclidean Algorithm

programmed using Problem4.py

### A

$\begin{aligned}

\end{aligned}$

### B

GCD(1105, 425) = 85

### C

GCD(2078, 9602) = 2

### D

GCD(22142, 16762) = 2

## Problem 5 Extended Euclidean Algorithm

### A

### B

### C

### D

## Problem 6 Ideal Block Cipher

### A

The number of reversible mappings for the ideal block cipher for a block of n bits is $ 2^n! $. For a mapping to be reversible, each block must be able to map into a unique ciphertext block. In order to enumerate all possible mappings, the block equivalent to 0 can map into any of the $2^n$ possibile blocks. The block with value 1 can map into any of the $ 2^n-1 $ possible blocks. Thus the total number of reversible mappings of an ideal block is $ 2^n! $. 

### B

