
def gcdExtended(a, b): 
    # Base Case 
    if a == 0 :  
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
    print(f"{a} * {x} + {b} * {y} = {gcd}")
    return gcd,x,y

def main():
    print("Problem 4")
    gcdExtended( 42, 30)
    print("Part A\nCheck the Markdown Sheet")
    print("\nPart B\n")
    gcdExtended( 650 % 1769, 650)
    # print(f"650 mod 1769 = {gcdExtended( 650, 650 % 1769)}")
    print("\nPart C\n")
    gcdExtended( 2078 % 9602 ,2078)
    # print(f"GCD(2078, 9602) = {gcdExtended(2078, 2078 % 9602)}")
    print("\nPart D\n")
    gcdExtended(22142 % 16762, 22142)
    # print(f"GCD(22142, 16762) = {gcdExtended(22142, 22142 % 16762)}")

if __name__ == "__main__":
    main()