# Homework 4

## Problem 1

a. 
Block Length: 16 bits
The state array for a simplified AES is similar to the regular version except the state array is divided into a two by two array (rather than a four by four). These state arrays are referred to as Nibbles (a nibble is also half a byte)

b.
$x^4 + x + 1$

c. 

$
  S_{0,0} = x^3+1 = 1001 = 9 \\
  S_{1,0} = x = 0010 = 2 \\
  S_{0,1} = x = 0010 = 2 \\
  S_{1,1} = x^3+1 \\
  S = 
    \begin{bmatrix}
      9 & 2 \\
      2 & 9
    \end{bmatrix} \\
   \begin{bmatrix}
    1 & 4 \\
    4 & 1
  \end{bmatrix}
  \times
  \begin{bmatrix}
      9  \\
      2 
    \end{bmatrix}
    = =S'_{0,0 - 1,0}
$

## Problem 2

## Problem 3

## Problem 4

## Problem 6