from TWO import factors


def PubKey(a, q, X):
    return a**X % q

def SharedSecretKey(Yb, Xa, q):
    return Yb**Xa % q

def DerivePrivateKey(q, a, Y):
    # Brute Force Baby
    for i in range(20): #I figure since its mod 11 i dont need to go that high.
        if a**i %q == Y:
            return i

def main():
    q = 71
    a = 7
    Xa = 4
    Xb = 11
    ## A
    Ya = PubKey(a,q,Xa)
    ## B
    Yb = PubKey(a,q,Xb)
    ## C
    K = SharedSecretKey(Yb, Xa, q)
    print(f"{Ya=}\n{Yb=}\n{K=}")
    ## D
    a = 2
    q = 11
    x = ""
    for i in range(q):
        x = ("$2^{" + str(i+1) + "} = 2^{" + str(i) +r"} \times 2 \equiv " + str(2**i) + r" \times 2 = 2 \equiv " + str(2**i % 11)  + " (\mod 7)$")
        print(x)
    ## E
    print(DerivePrivateKey(q, a, 9))
    ## F
    print(SharedSecretKey(3,DerivePrivateKey(q, a, 9), q ))
    
    #print(f"Smallest primitive root of {11}, {findPrimitive(11)}")

if __name__ == "__main__":
    main()