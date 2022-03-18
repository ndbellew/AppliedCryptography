# Homework 3
## Bellew, Nathan D

<style type="text/css">
    ol { list-style-type: upper-alpha; align: center;}
</style>
### Problem 1

A. 

B.
C. 
D.
E.


### Problem 2

A. 

To derive $K_1$ you must first change the hex key into binary, then use the Key Parity permutation to change the key into 56 bits, then separate the into halves, circular left shift both sides and then recombine the key, after recombining the key you can use the compression permutation on the key to compress the key into 48 bits. Creating $K_1$.
First you must change the key 89ABCDEF01234567 into Binary which has been provided as 
`1000100110101011110011011110111100000001001000110100010101100111`. 
From here the key needs to be permuted following the Key Parity permutation set as described from the supplementary material as
```
[57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4 ]
```
Once permuted the key becomes:
$K_{L}$ = `0000 1111 1100 1100 1010 1010 0000`
$K_{R}$ =`1010 1010 1100 1100 0000 1111 0000`
These are written seperately because the key needs to be split in half creating a left and a right side. these sides are each shifted to the left using a circular left shift. They are shifted a single time because the normal DES has the shift occur once on the first run and then twice on the next few. Because we are only doing a single round we only need the first shift which is only a single shift. 
After shifting the values become:
$K_{Lshifted}$ = `0001 1111 1001 1001 0101 0100 0000`
$K_{Rshifted}$ = `1010 1010 1100 1100 0000 1111 0000`
Now that the two have been shifted the key sides can be recombined and permuted. The permutation will compress the now 56bit key into a 48 bit key. 
$K_{P48}$ = `0000 0100 0100 0011 0111 0110 1001 0011 1001 0101 1000 1101`
Which when converted to Hex becomes $K_{P48} =$ `84 43 76 93 95 8B`. 

B. 

In order to derive the initial Left and Right sides of the cipher the plaintext must first be permuted through the initial Permutation or IP, then the result of that initial Permutation can be split in half creating the left and right sides. 
IP = 
```
[58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7]
```
So taking the Initial Permutation of the original line (do not need to convert to binary since its the same as the key and this was done already) of 
`1000 1001 1010 1011 1100 1101 1110 1111 0000 0001 0010 0011 0100 0101 0110 0111` 
becomes:
$L_0$ = `1100 1100 0000 0000 1100 1100 1111 1111`
$R_0$ = `0000 1111 1010 1010 0000 1111 1010 1010` 

C. 

This one is easier than it sounds in order to Expand $R_0$ to get $E[R_0]$ you must use the Expansion function which is described as:
```
[32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
12, 13, 12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21, 20, 21,
22, 23, 24, 25, 24, 25, 26, 27,
28, 29, 28, 29, 30, 31, 32, 1 ]
```

After applying this function to only $R_0$ the result will modify the 32bit right side to 48 bits so it can be xored. Applying the function the result becomes:
$R_{0expanded}$ = `0000 0101 1111 1101 0101 0100 0000 0101 1111 1101 0101 0100`

D.

Calculate $A = E[R_0] \oplus K_1$. Simply take the Key that was calculated earlier and xor it with the new expanded right side:
$K_{P48}$ =       `0000 0100 0100 0011 0111 0110 1001 0011 1001 0101 1000 1101`
$R_{0expanded}$ = `0000 0101 1111 1101 0101 0100 0000 0101 1111 1101 0101 0100`
XOR Results =     `0000 0001 1011 1110 0010 0010 1001 0110 0110 1000 1101 1001`

(They lined up way better on my markdown sheet than my pdf!)

E.

I ordered the XOR results above into groupings of 4 because it was easier for me to calcuate the XOR that way. But now i have to take that and rearrange it into 6s then apply the s-box. I could include every single s-box (all 8 of them) but i think you know what they look like. The way to apply the s-box (or what i did) is to take each of the 6 bit sections and apply them to a different box. Maintaining order from left to right.

Group into 6:
`000000 011011 111000 100010 100101 100110 100011 011001`
Apply S-box, the results:
S-Box = `1110 1001 0101 0110 1100 0101 1011 0000`

F.

Take the results from above and put them into a single binary line, I will write it but it should be relatively clear how i determined the answer. 
`11101001010101101100010110110000`
G.

This permutation is the straight permutation, it is not part of the initial nor the final. it instead will permute a 32 bit result which is necessary for the final XOR of the round. 

Straight Permutation:
```
[ 16,  7, 20, 21,
29, 12, 28, 17,
1, 15, 23, 26,
5, 18, 31, 10,
2,  8, 24, 14,
32, 27,  3,  9,
19, 13, 30,  6,
22, 11,  4, 25 ]
```
The result of the permutation:
`0000 0111 1100 1101 1111 0110 0000 1001`

H.

Calculate $R_1 = P(B) \oplus L_0$
Same as last XOR but with different values:
`1100 1100 0000 0000 1100 1100 1111 1111` $L_0$
`0000 0111 1100 1101 1111 0110 0000 1001` $P(B)$
`1100 1011 1100 1101 0011 1010 1111 0110` XOR

The XOR becomes the new Right side or $R_1$ and the old right becomes the new left or $L_1$ so 
$L_1$ = `0000 1111 1010 1010 0000 1111 1010 1010`
$R_1$ = `1100 1011 1100 1101 0011 1010 1111 0110` 

This is important in the last step.

I.

Now to get the ciphertext I must first combine $L_1$ and $R_1$ and then with the new combination run that through the inverse of the initial permutation or $IP^{-1}$

$IP^{-1}$ = 
`1110 0100 1101 1111 0110 0110 1111 1101 0000 1010 0001 1011 1010 0010 1011 0011`

Which, after converting to Hex, becomes:
    `E4DF66FD0A1A2B3`


### Problem 3

A. 
Addition:
| + | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **0** | **0** | 1 | 2 | 3 | 4 |
| **1** | 1 | 2 | 3 | 4 | **0** |
| **2** | 2 | 3 | 4 | **0** | 1 |
| **3** | 3 | 4 | **0** | 1 | 2 |
| **4** | 4 | **0** | 1 | 2 | 3 |

Multiplication:
| x | **0**  | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **0** | **0**  | **0**  | **0**  | **0**  | **0**  |
| **1** | **0**  | 1 | 2 | 3 | 4 |
| **2** | **0**  | 2 | 4 | 6 | 8 |
| **3** | **0**  | 3 | 6 | 9 | 12|
| **4** | **0**  | 4 | 8 | 12| 16|

Multiplicative and additive inverses:
| $w$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
|$-w$ | 0 | 4 | 3 | 2 | 1 |
|$w^{-1}$| - | 1 | 3 | 2 | 4 |

B.
 


### Problem 4

A. 
The Field GF(4) with $m(x) = x^2 + x + 1$


|   +   |   0   |   1   |   $ x $   |   $ x+1 $   |
| ----- | ----- | ----- | --------- | ----------- |
| **0** |   0   |   1   |   $ x $   |   $ x+1 $   |
| **1** |   1   |   0   |  $ x+1 $  |    $ x $    |
| **x** |   x   |   x   |     0     |      1      |
|**x+1**|$ x+1 $|   x   |     1     |      0      |


|   x   |   0   |   1   |   $ x $   |   $ x+1 $   |
| ----- | ----- | ----- | --------- | ----------- |
|   0   |   0   |   0   |     0     |      0      |
|   1   |   0   |   1   |   $ x $   |   $ x+1 $   |
|  $x$  |   0   |  $x$  |  $ x+1 $  |      1      |
| $x+1$ |   0   |$ x+1 $|     1     |     $x$     |



B.
Generator for $GF(2^4)$ using $m(x) = x^4 + x + 1$
| Power Representation | Polynomial Representation | Binary Representation | Decimal (Hex) Representation |
| -------------------- | ------------------------- | --------------------- | ---------------------------- |
|          0           |            0              |          0000         |               00             |
|        $g^0$         |            1              |          0001         |               01             |
|        $g^1$         |           $g$             |          0010         |               02             |
|        $g^2$         |          $g^2$            |          0100         |               04             |
|        $g^3$         |          $g^3$            |          1000         |               08             |
|        $g^4$         |          $g+1$            |          0011         |               03             |
|        $g^5$         |         $g^2+g$           |          0110         |               06             |
|        $g^6$         |        $g^3+g^2$          |          1100         |               12             |
|        $g^7$         |        $g^3+g+1$          |          1011         |               11             |
|        $g^8$         |         $g^2+1$           |          0101         |               05             |
|        $g^9$         |         $g^3+g$           |          1010         |               10             |
|       $g^10$         |        $g^2+g+1$          |          0111         |               07             |
|       $g^11$         |       $g^3+g^2+g$         |          1110         |               14             |
|       $g^12$         |      $g^3+g^2+g+1$        |          1111         |               15             |
|       $g^13$         |       $g^3+g^2+1$         |          1101         |               13             |
|       $g^14$         |         $g^3+1$           |          1001         |               09             |

### Problem 5

A.

B.

