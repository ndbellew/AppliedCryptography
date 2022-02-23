# Euclidean Algorithm 
# Problem 4

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    print("Problem 4")
    print("Part A\nCheck the Markdown Sheet")
    print("")

if __name__ == "__main__":
    main()