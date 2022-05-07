a. 

|Key Generation by Alice|    |
|---|---|
| Select p, q | p=3 & q=11
| Calculat n | n = 33 |
| Calculate $\phi$(n) | 20 |
| Select Integer e | gcd$(\phi(n), 7) = 1; 1<7<\phi(n)$
| Calculate d | 0.14285714285714285
| Public Key | PU = (7,33) |
| Private Key | PR = (0.14285714285714285,33) |

|Encryption by Bob with Alice's Public Key|    |
|---|---|
| Plaintext | M=5 < n=33 |
| Ciphertext | C=14; $C = M^e \mod n$ |

|Decryption By Alice with Alice's Public Key|    |
|---|---|
| Ciphertext: | C=14 |
| Plaintext: | M=5; $M = C^d \mod n$|
b.

|Key Generation by Alice|    |
|---|---|
| Select p, q | p=7 & q=11
| Calculat n | n = 77 |
| Calculate $\phi$(n) | 60 |
| Select Integer e | gcd$(\phi(n), 17) = 1; 1<17<\phi(n)$
| Calculate d | 0.058823529411764705
| Public Key | PU = (17,77) |
| Private Key | PR = (0.058823529411764705,77) |

|Encryption by Bob with Alice's Public Key|    |
|---|---|
| Plaintext | M=8 < n=77 |
| Ciphertext | C=57; $C = M^e \mod n$ |

|Decryption By Alice with Alice's Public Key|    |
|---|---|
| Ciphertext: | C=57 |
| Plaintext: | M=8; $M = C^d \mod n$|
c.

|Key Generation by Alice|    |
|---|---|
| Select p, q | p=11 & q=13
| Calculat n | n = 143 |
| Calculate $\phi$(n) | 120 |
| Select Integer e | gcd$(\phi(n), 9) = 1; 1<9<\phi(n)$
| Calculate d | 0.1111111111111111
| Public Key | PU = (9,143) |
| Private Key | PR = (0.1111111111111111,143) |

|Encryption by Bob with Alice's Public Key|    |
|---|---|
| Plaintext | M=7 < n=143 |
| Ciphertext | C=8; $C = M^e \mod n$ |

|Decryption By Alice with Alice's Public Key|    |
|---|---|
| Ciphertext: | C=8 |
| Plaintext: | M=7; $M = C^d \mod n$|
d.

|Key Generation by Alice|    |
|---|---|
| Select p, q | p=17 & q=31
| Calculat n | n = 527 |
| Calculate $\phi$(n) | 480 |
| Select Integer e | gcd$(\phi(n), 7) = 1; 1<7<\phi(n)$
| Calculate d | 0.14285714285714285
| Public Key | PU = (7,527) |
| Private Key | PR = (0.14285714285714285,527) |

|Encryption by Bob with Alice's Public Key|    |
|---|---|
| Plaintext | M=2 < n=527 |
| Ciphertext | C=128; $C = M^e \mod n$ |

|Decryption By Alice with Alice's Public Key|    |
|---|---|
| Ciphertext: | C=128 |
| Plaintext: | M=2; $M = C^d \mod n$|