# Problem 5

# Bellew, Nathan D

## GF(256) calculator in m(x)=x^8+x^4+x^3+x+1

class Calculator:
    def __init__(self, f):
        self.f = self.parsePolynomial(f)
        self.MainFunction = [8,4,3,1,0]
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

    def __add__(self, other):
        output = []
        for poly in other.f:
            output.append(poly)
        return self.PolyMod(output)

    def __sub__(self, other):
        output = []
        for poly in other.f:
            self.f.append(poly)

        return self.PolyMod(output)
            

    def __mul__(self, other):
        output = []
        print(self.f, other.f)
        for F in self.f:
            for G in other.f:
                output.append(F+G)
        print(output)
        return self.PolyMod(output)

    def __truediv__(self, other):
        # Steps virst you must invert the other.f by finding the multiplicative inverse usinc the 
        # Extended algorithm
        
        return "1"

    def parsePolynomial(self, polynomial):
        poly = []
        polynomial = polynomial.split("+")
        for num in polynomial:
            if len(num) >= 3:
                exponent = int(num[2:]) # should be x^ then some number ie x^5 this makes the exponent variable
                poly.append(exponent)   # equivalent to 5
            elif len(num) == 1:
                if num == "x":
                    poly.append(1)
                elif int(num) == 1:
                    poly.append(0)
                else:
                    poly.append(-1)
        return sorted(poly, reverse=True) #ensures largest polynomial is on the left.

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
                        else:
                            Func.remove(remainder)
                else:
                    Func.append(i)
            else:
                Func.remove(i)
        func = Func
        return self.PrepOutput(func)

        
    def PrepOutput(self, Output):
        out = []
        for i in Output:
            out.append(self.ConvDict[i])
        return f'f(x) = {"+".join(out)}'

def main():
    c = Calculator("x^5+x^4+x^3+x+1")
    d = Calculator("x^2+x+1") 
    e = c + d
    f = c * d
    print(e)
    print(f)
    print(c/d)
    
if __name__ == "__main__":
    main()