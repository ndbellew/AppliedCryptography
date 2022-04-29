

# Extended Euclidean will recurse through until it finds the greatest
# common divisor and then will find x and y based on those results.
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
    print("Problem 5")
    gcdExtended( 42, 30)
    print("Part A\nCheck the Markdown Sheet")
    print("\nPart B\n")
 
    gcdExtended(650, 1769)
    print("\nPart C\n")
    gcdExtended(950 , 1767)
    print("\nPart D\n")
    gcdExtended(10012, 234378)


if __name__ == "__main__":
    main()