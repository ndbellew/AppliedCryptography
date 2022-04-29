from sympy.ntheory import discrete_log as DL

def main():
    BASE = 2
    MODULO = 29
    Table = list()
    Row = ""
    Row2 = ""
    Row3 = ""
    for i in range(MODULO):
        if i == 0:
            Row+=f"|Discrete Logarithms to the base 2 Modulo 29|"
            Row3+="|-|"
            Row2+=f"|a|"
        else:
            Row+= " |"
            Row3+="-|"
            Row2+= f" {i}|"
    Table.append(Row)
    Table.append(Row3)
    Row = ""
    Table.append(Row2)
    for i in range(MODULO):
        if i == 0:
            Row += "|\log_{2,29}(a)|"# hard coded because f strings are silly
        else:
            Row+= f"{DL(MODULO, i, BASE)}|"
    Table.append(Row)
    with open("TableOfDiscreteLogarithms.txt", 'w+') as f:
        for items in Table:
            f.write('%s\n' %items)

if __name__ == "__main__":
    main()