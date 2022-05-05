from egcd import egcd
from bitstring import BitArray as BA

from functools import reduce

def factors(val):    
    return [(i, int(val / i)) for i in range(1, int(val**0.5)+1) if val % i == 0]

def Problemb():
    ## B
    e = 31
    n = 3599
    Factors = factors(n)
    print(f"Factors: {Factors}")
    for F in Factors:
        p,q = F
        phi = (p-1)*(q-1)
        gcd, a, m = egcd(phi, e)
        if gcd == 1:
            print(f"{phi=}\n{gcd=}\n{a=}\n{m=}")
            if e*a%phi == 1:
                print(f"PR = ({a}, {n})")
            elif e*m%phi ==1:
                print(f"PR = ({m}, {n})")
            else:
                print("Error")
                quit(1)

def EfficientPubKey(a, b, n):
    bRow = "|$b_i$|"
    cRow = "|c|"
    fRow = "|f|"
    c = 0
    f = 1
    for i in range(len(b),0, -1):
        Bi = int(b[i-1])
        c = 2*c
        f = (f*f) % n   
        if Bi ==1:
            c = c+1
            f = f*a % n
            print(c,f)
        bRow += f"{b[i-1]}|"
        cRow += f"{c}|"
        fRow += f"{f}|"
    Table = f"{bRow}\n{cRow}\n{fRow}"
    return f, Table

def Problemc():
    a = 5
    B = 596
    b = str(bin(B)[2:])[::-1]
    n = 1234
    TableList = ""
    TableList += "| i | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |\n"
    TableList += "|---|----|---|---|---|---|---|---|---|---|---|---|\n"
    #bi
    _, Entries = EfficientPubKey(a,b,n)
    TableList += Entries
    print(TableList)


if __name__=="__main__":
    Problemc()

