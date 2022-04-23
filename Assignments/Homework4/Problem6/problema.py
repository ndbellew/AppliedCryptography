
def main():
    Modulo = 13
    Table = list()
    Row = ""
    for i in range(Modulo-1):
        if i == 0:
            Row+="|$a$|"
        else:
            Row += f"$a^{i+1}$|"
    Table.append(Row)
    for i in range(1, Modulo):
        Row = "|"
        for j in range(1, Modulo):
            Row += f"{i**j % Modulo}|"
        Table.append(Row)
    with open("PowersofIntegers.txt", 'w+') as f:
        for items in Table:
            f.write('%s\n' %items)

if __name__ == "__main__":
    main()