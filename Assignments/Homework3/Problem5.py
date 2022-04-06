# Problem 5

# Bellew, Nathan D

## GF(256) calculator in m(x)=x^8+x^4+x^3+x+1

import itertools as it

class Calculator:
    def __init__(self, f):
        self.f = self.parsePolynomial(f)
        self.MainFunction = [8,4,3,1,0]
        # Mapping so i can convert the array back into standard polynomial form. 
        self.ConvDict = {
        0 : "1",
        1 : "x",
        2 : "x^2",
        3 : "x^3",
        4 : "x^4",
        5 : "x^5",
        6 : "x^6",
        7 : "x^7"
    }

    # Function overides the '+' operator and performs this action when two calculator objects
    # (which are also polynomials) 
    def __add__(self, other):
        output = []
        for poly in other.f:
            output.append(poly)
        return self.PolyMod(output)

    # overrides the '-' operator
    def __sub__(self, other):
        output = []
        for poly in other.f:
            output.append(poly)
        return self.PolyMod(output)
            
    # Overrides the * operator
    def __mul__(self, other):
        output = []
        for F in self.f:
            for G in other.f:
                output.append(F+G)
        return self.PolyMod(output)

    # Overides the / operator
    def __truediv__(self, other):
        # Steps virst you must invert the other.f by finding the multiplicative inverse usinc the 
        # Extended algorithm
        # AllPolys = [1,2,3,4,5,6,7,8,9,0] # 9 does not exist i will remove it from all lists later.
        # AllPolyPerms = list(it.product(AllPolys, repeat=10))
        # for PolyCombo in AllPolyPerms:
        # yep I dont know
        return "1"

    # Takes polynomial in standard form and converts it into an array of exponents (since
    # there are no coefficients)
    def parsePolynomial(self, polynomial):
        poly = []
        polynomial = polynomial.split("+") # Creates list (array) of strings where each of them are the x's
        for num in polynomial:              # followed by the ^num
            if len(num) >= 3:
                exponent = int(num[2:]) # should be x^ then some number ie x^5 this makes the exponent variable
                poly.append(exponent)   # equivalent to 5
            elif len(num) == 1:
                if num == "x": # if its x then it would be by itself otherwise its +1 or the polynomial is 0
                    poly.append(1)
                elif int(num) == 1:
                    poly.append(0)
                else:
                    poly.append(-1)
        return sorted(poly, reverse=True) #ensures largest polynomial is on the left.

    # Function PolyMod will run modulo on the Polynomial for the main function
    # it will return a list of exponents that should be correctly reduced following G(2^8)
    def PolyMod (self, func):
        MF = [4,3,1,0] # Main Function but its what 8 becomes
        # Preload the funciton and ensure that its reduced properly
        Func = []
        for i in func:
            if i not in Func:
                if i > 8:
                    numof8 =  i // 8
                    remainder = i % 8
                    if numof8 % 2 == 1: # odd number of eight so only [4,3,1,0] should be there
                        F = MF
                        if remainder in F:
                            F.remove(remainder)
                        else:
                            F.append(remainder)
                        for num in F:
                            Func.append(num)
                    else:
                        if remainder not in Func:
                            Func.append(remainder)
                        else:# if there are 2 of a number like 2x^2 it becomes 0 because 2 mod 2 = 0.
                            Func.remove(remainder)
                else:
                    Func.append(i)
            else:# if there are 2 of a number like 2x^2 it becomes 0 because 2 mod 2 = 0.
                Func.remove(i)
        func = Func # idk why i did this it is unecessary but I am not changing it!
        return self.PrepOutput(func)

    # Will reformat the output from an array of exponents into the standard form
    # the valuess were originally made in.
    def PrepOutput(self, Output):
        out = []
        for i in Output:
            out.append(self.ConvDict[i])
        return f'f(x) = {"+".join(out)}'

def main():
    Polynomial1 = "x^5+x^4+x^3+x+1"
    Polynomial2 = "x^10+x^7+x^2+x+1"
    PolyObj1 = Calculator("x^5+x^4+x^3+x+1")
    PolyObj2 = Calculator("x^2+x+1") 
    Add = PolyObj1 + PolyObj2
    Sub = PolyObj1 - PolyObj2
    Mul = PolyObj1 * PolyObj2
    print(f"({Polynomial1}) + ({Polynomial2}) = {Add}")
    print(f"({Polynomial1}) - ({Polynomial2}) = {Sub}")
    print(f"({Polynomial1}) * ({Polynomial2}) = {Mul}")

if __name__ == "__main__":
    main()