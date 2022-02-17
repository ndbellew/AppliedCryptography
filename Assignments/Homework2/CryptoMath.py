import math
# Takes in list of Values and uses Shannon's entropy formula

def Events(numOfEvents, ListOfChances):
    Answer = 0.0
    for eventNum in range(numOfEvents):
        Answer += Entropy(ListOfChances)
    return round(Answer, 4)

def Entropy(Values):
    TotalSum = 0.0
    for Value in Values:
        TotalSum += Value * math.log2(1/Value)
    return TotalSum

def BuildEntropy(Number):
    TempList = []
    for i in range(Number):
        TempList.append(1/Number)
    return TempList

def main():
    print("Problem 1")
    print("Part A")
    print(Events(1, BuildEntropy(6)))
    print(Events(4, BuildEntropy(6)))
    print("Part B")
    print(Events(1, [1/6,1/6,1/6,3/6]))
    print(Events(5, [1/6,1/6,1/6,3/6]))
    print("Part C")
    print(Events(1, [1/6,1/6,1/6,1/6,1/6,1/6]))
    print(Events(1, [1/6,1/6,1/6,1/6,2/6]))
    print("Part D")
    print(Events(1, [1]))
    print("Problem 2")
    print("Part A")
    print(Events(1, [3/9, 2/9, 4/9]))
    print(Events(30, [3/9, 2/9, 4/9]))
    print("Part C")
    print(Events(1, [4/11, 3/11, 4/11]))

if __name__ == "__main__":
    main()