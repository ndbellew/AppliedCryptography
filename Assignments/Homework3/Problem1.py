import numpy as np
from itertools import permutations

class DES:
    def __init__(des, key, text):
        des.key = des.PermutedChoice1(key)
        des.text = des.InitialPermutation(text) # List of bits

    def InitialPermutation(des, Text):
        perm = permutations(Text)
        return perm

    def InversePermutation(des, Permutation): 
        inv = np.empty_like(Permutation)
        inv[Permutation] = np.arange(len(inv), dtype=inv.dtype)
        return inv

    def Round(des, text):
        Left, Right = text[:len(text)//2], text[len(text)//2:]
        RightExpanded = des.ExpansionPermutation(Right)

    def Circular_Left_Shift(des, Key, Number_Of_Shifts):
        Shifted_Text = ""
        # Take the cycle through the text and add the first number to the end of 
        # the list. Do this by adding all but the first Number for Each loop. 
        for FirstNumber in range(Number_Of_Shifts):
            for EachInKey in range(1, len(Key)):
                # grab all but the first number and toss it into a string
                Shifted_Text = Shifted_Text + Key[EachInKey]
            # Now add the new first number and reset the Key so that 
            # the number has shifted to the left. 
            Shifted_Text = Shifted_Text + Key[FirstNumber]
            Key = Shifted_Text
            Shifted_Text = ""
        return Key

    def PermutedChoice1():
        pass

    def PermutedChoice2():
        pass

    def xor(Lista, Listb): 
        ans = ""
        for i in range(len(Lista): # Should be same as b
            if Lista[i] == Listb[i]:
                ans += "0"
            else:
                ans += "1"
        return ans

    def ExpansionPermutation(des, text):
        return [text[31], text[0],  text[1],  text[2],  text[3],  text[4],
                text[3],  text[4],  text[5],  text[6],  text[7],  text[8],
                text[7],  text[8],  text[9],  text[10], text[11], text[12],
                text[11], text[12], text[13], text[14], text[15], text[16],
                text[15], text[16], text[17], text[18], text[19], text[20], 
                text[19], text[20], text[21], text[22], text[23], text[24],
                text[23], text[24], text[25], text[26], text[27], text[28],
                text[27], text[28], text[29], text[30], text[31], text[0]]

def main():
    key  = int("f34f9dd8f5051fa5",16)
    text = list(bin(int("c1a51e55deadc0de", 16)))[2:]
    print(text)

if __name__ == "__main__":
    main()