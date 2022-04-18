def solve(A, B):
    XOR = A ^ B
    count = 0
    # Check for 1's in the binary form using
    # Brian Kernighan's Algorithm
    while (XOR):
        XOR = XOR & (XOR - 1)
        count += 1
    return count

def main():
    initial =   [
        "1200456789abcdeffedcba9876543210",
        "1d0034aece7225b6e26b174ed92b5588",
        "7b6e7f640fd2ff3ff2ecf9f9f7094cfa",
        "ce11a191a8499b964df86eeb2d11b8ed",
        "64a8e7e4384ffa688b6b51e66abc7e8a",
        "bc8d55329e6fae08e6b5cb30b96a5044",
        "94c5db6a304c88c61d25c50038516df6",
        "5b44e5f5c59baf88545ecb78a9cd3e84",
        "1d3b28c74ace8076422143b967af6c68",
        "e631cbf6f001f5fbd16e7ac78be99a9e",
        "f6bff8c82a8f297d294f9782539562a7"
        ]
    Secondary = [
        "1300456789abcdeffedcba9876543210",
        "1c0034aece7225b6e26b174ed92b5588",
        "0b56472c0fd2ff3ff2ecf9f9f7094cfa",
        "da1bab8f9a7bcdf23f6e8a995f4d96c3",
        "73037596bb7fb03b56d62d449d160439",
        "a09a69fa2771d8452dc185c18e8f9ee2",
        "9356c0601f2c407d79c00a326b2752bf",
        "df1804e12cd8fbd91f381fc6ed971056",
        "e6e276587831da0f1c27c865cfcca829",
        "746e69ed49087ea5bee032ae9abced59",
        "23eb1ac227ff18027011b0a69dbdf33a"

    ]
    Tertiary = [
        "1200456789abcdeffedcba9876543310",
        "1d0034aece7225b6e26b174ed92b5488",
        "7b6e7f64d3ad5ce3f2ecf9f9f7094cfa",
        "ae5181b188598ba6299cc22371f500b1",
        "9674ab3ec834a6602113c8058fd54ef8",
        "b80929875a209651b42d3eca4745575f",
        "decaeb706acf7c6f17f420e92ff3bf3f",
        "fd2202683589b490cf45c730497aca4e",
        "a02bcffa1560ef8bae083ec663f32c5c",
        "242f8ed77387d3507d92ae44b265eec2",
        "30bd25129bd015a01f7eed377766dd4a"
    ]
    Table1,Table2 = [],[]
    for i in range(len(initial)):
        if i == 0:
            Table1.append(f"| |{initial[i]}<br>{Secondary[i]}| {solve(int(initial[i],16), int(Secondary[i],16))}|")
            Table2.append(f"| |{initial[i]}<br>{Tertiary[i]}| {solve(int(initial[i],16), int(Tertiary[i],16))}|")
        Table1.append(f"|{i}|{initial[i]}<br>{Secondary[i]}| {solve(int(initial[i],16), int(Secondary[i],16))}|")
        Table2.append(f"|{i}|{initial[i]}<br>{Tertiary[i]}| {solve(int(initial[i],16), int(Tertiary[i],16))}|")
    
    with open("AvalancheEffect.txt", 'w+') as f:
        for items in Table1:
            f.write('%s\n' %items)
        f.write('\n')
        for items in Table2:
            f.write('%s\n' %items)

if __name__=="__main__":
    main()