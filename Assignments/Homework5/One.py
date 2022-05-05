import re

def NewTable(Text):
    print(f"|{Text}|    |")
    print(f"|---|---|")

def RSA(p,q,e,M):
    N = p*q
    phi = (p-1) * (q-1)
    d = e**(-1) % phi
    C = M**e % N
    NewTable("Key Generation by Alice")
    print(f"| Select p, q | {p=} & {q=}")
    print(f"| Calculat n | n = {N} |")
    print(f"| Calculate $\phi$(n) | {phi} |")
    print(f"| Select Integer e | gcd$(\phi(n), {e}) = 1; 1<{e}<\phi(n)$")
    print(f"| Calculate d | {d}")
    print(f"| Public Key | PU = ({e},{N}) |")
    print(f"| Private Key | PR = ({d},{N}) |")
    print()
    NewTable("Encryption by Bob with Alice's Public Key")
    print(f"| Plaintext | {M=} < n={N} |")
    print(f"| Ciphertext | {C=}; $C = M^e \mod n$ |")
    print()
    NewTable("Decryption By Alice with Alice's Public Key")
    print(f"| Ciphertext: | {C=} |")
    print(f"| Plaintext: | {M=}; $M = C^d \mod n$|")
    print()

    
if __name__ == "__main__":
    with open("RSAprob1.txt") as f:
        for line in f:
            p,q,e,M = list(map(int, re.findall(r'\d+',line)))
            RSA(p,q,e,M)
    