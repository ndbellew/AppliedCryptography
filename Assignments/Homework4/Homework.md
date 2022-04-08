# Homework 4

## Problem 1

a. 
Block Length: 16 bits
The state array for a simplified AES is similar to the regular version except the state array is divided into a two by two array (rather than a four by four). These state arrays are referred to as Nibbles (a nibble is also half a byte)

b.
$x^4 + x + 1$

c. 
I am doing this under the assumption that the shift rows step has already taken place. 
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
    =
  \begin{bmatrix}
  17 \\
  38
  \end{bmatrix}
  \mod{x^4+x+1} =
  \begin{bmatrix}
  2 \\
  0
  \end{bmatrix}
  =S'_{0,0 - 1,0} \\
  \begin{bmatrix}
    1 & 4 \\
    4 & 1
  \end{bmatrix}
  \times
  \begin{bmatrix}
      2  \\
      9 
    \end{bmatrix}
    =
  \begin{bmatrix}
  38 \\
  17
  \end{bmatrix}
  \mod{x^4+x+1} =
  \begin{bmatrix}
  0 \\
  2
  \end{bmatrix}
  =S'_{0,1 - 1,1}
$
The inverse then becomes:
$
\begin{bmatrix}
2 & 0 \\
0 & 2
\end{bmatrix}
$
## Problem 2

a.
Key =  0e 00 71 c9 47 d9 e8 59 1c b7 ad d6 af 7f 67 98
Key Expansion for AES 

|   Key Words  | Auxiliary Funciton       |
---------------|-------------------------
|W0 = 0e 00 71 c9<br>W1 = 47 d9 e8 59<br>W2 = 1c b7 ad d6<br>W3 = af 7f 67 98|RotWord(W3) = 7f 67 98 af<br>SubWord(X1) = d2 85 46 79<br>Rcon (1) = 01 00 00 00<br>y xor Rcon = d3 85 46 79|
|W4 = W0 $\oplus$ z = dd 85 37 b0<br>W5 = W4 $\oplus$ W1  = 9a 5c df e9<br>W6 = W5 $\oplus$ W2  = 86 eb 72 3f<br>W7 = W6 $\oplus$ W3  = 29 94 15 a7|RotWord(W7) = 94 15 a7 29<br>SubWord(X2) = 22 59 5c a5<br>Rcon (2) = 02 00 00 00<br>y xor Rcon = 20 59 5c a5|
|W8 = W4 $\oplus$ z = fd dc 6b 15<br>W9 = W8 $\oplus$ W5  = 67 80 b4 fc<br>W10 = W9 $\oplus$ W6  = e1 6b c6 c3<br>W11 = W10 $\oplus$ W7  = c8 ff d3 64|RotWord(W11) = ff d3 64 c8<br>SubWord(X3) = 16 66 43 e8<br>Rcon (3) = 04 00 00 00<br>y xor Rcon = 12 66 43 e8|
|W12 = W8 $\oplus$ z = ef ba 28 fd<br>W13 = W12 $\oplus$ W9  = 88 3a 9c 01<br>W14 = W13 $\oplus$ W10  = 69 51 5a c2<br>W15 = W14 $\oplus$ W11  = a1 ae 89 a6|RotWord(W15) = ae 89 a6 a1<br>SubWord(X4) = e4 a7 24 32<br>Rcon (4) = 08 00 00 00<br>y xor Rcon = ec a7 24 32|
|W16 = W12 $\oplus$ z = 31 d0 cc f<br>W17 = W16 $\oplus$ W13  = 8b 27 90 ce<br>W18 = W17 $\oplus$ W14  = e2 76 ca 0c<br>W19 = W18 $\oplus$ W15  = 43 d8 43 aa|RotWord(W19) = d8 43 aa 43<br>SubWord(X5) = 61 1a ac 1a<br>Rcon (5) = 10 00 00 00<br>y xor Rcon = 71 1a ac 1a|
|W20 = W16 $\oplus$ z = 72 07 a0 d5<br>W21 = W20 $\oplus$ W17  = f9 20 30 1b<br>W22 = W21 $\oplus$ W18  = 1b 56 fa 17<br>W23 = W22 $\oplus$ W19  = 58 8e b9 bd|RotWord(W23) = 8e b9 bd 58<br>SubWord(X6) = 19 56 7a 6a<br>Rcon (6) = 20 00 00 00<br>y xor Rcon = 39 56 7a 6a|
|W24 = W20 $\oplus$ z = 4b 51 da bf<br>W25 = W24 $\oplus$ W21  = b2 71 ea a4<br>W26 = W25 $\oplus$ W22  = a9 27 10 b3<br>W27 = W26 $\oplus$ W23  = f1 a9 a9 0e|RotWord(W27) = a9 a9 0e f1<br>SubWord(X7) = d3 d3 ab a1<br>Rcon (7) = 40 00 00 00<br>y xor Rcon = 93 d3 ab a1|
|W28 = W24 $\oplus$ z = d8 82 71 1e<br>W29 = W28 $\oplus$ W25  = 6a f3 9b ba<br>W30 = W29 $\oplus$ W26  = c3 d4 8b 09<br>W31 = W30 $\oplus$ W27  = 32 7d 22 07|RotWord(W31) = 7d 22 07 32<br>SubWord(X8) = ff 93 c5 23<br>Rcon (8) = 80 00 00 00<br>y xor Rcon = 7f 93 c5 23|
|W32 = W28 $\oplus$ z = a7 11 b4 3d<br>W33 = W32 $\oplus$ W29  = cd e2 2f 87<br>W34 = W33 $\oplus$ W30  = e3 6a 48 e<br>W35 = W34 $\oplus$ W31  = 3c 4b 86 89|RotWord(W35) = 4b 86 89 3c<br>SubWord(X9) = b3 44 a7 eb<br>Rcon (9) = 1B 00 00 00<br>y xor Rcon = a8 44 a7 eb|
|W36 = W32 $\oplus$ z = f5 51 3d 6<br>W37 = W36 $\oplus$ W33  = c2 b7 3c 51<br>W38 = W37 $\oplus$ W34  = cc 81 98 df<br>W39 = W38 $\oplus$ W35  = f0 ca 1e 56|RotWord(W39) = ca 1e 56 f0<br>SubWord(X10) = 74 72 b1 8c<br>Rcon (10) = 36 00 00 00<br>y xor Rcon = 42 72 b1 8c|
|W40 = W36 $\oplus$ z = 4d 27 a2 5a<br>W41 = W40 $\oplus$ W37  = 8f 90 9e 0b<br>W42 = W41 $\oplus$ W38  = 43 11 06 d4<br>W43 = W42 $\oplus$ W39  = b3 db 18 82||




## Problem 3

## Problem 4

## Problem 6