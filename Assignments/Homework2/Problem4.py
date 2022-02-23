# Euclidean Algorithm 
# Problem 4

def gcd(a,b):
    if b == 0:
        return a
    Quotient = int((a - (a%b)) / b)
    print(f"| {a} = {Quotient} X {b} + {a%b} | d = gcd({b}, {a%b}) |")
    return gcd(b, a%b)

def main():
    print("Problem 4")
    print("Part A\nCheck the Markdown Sheet")
    print("\nPart B\n")
    print(f"GCD(1105, 425) = {gcd(1105, 425)}")
    print("\nPart C\n")
    print(f"GCD(2078, 9602) = {gcd(2078, 9602)}")
    print("\nPart D\n")
    print(f"GCD(22142, 16762) = {gcd(22142, 16762)}")

if __name__ == "__main__":
    main()