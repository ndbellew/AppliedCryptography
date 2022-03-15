

class DES:
    def __init__(des, key, text, NumOfRounds):
        des.NumOfRounds = NumOfRounds
        des.InitialPerm = [58, 50, 42, 34, 26, 18, 10, 2,
                           60, 52, 44, 36, 28, 20, 12, 4,
                           62, 54, 46, 38, 30, 22, 14, 6,
                           64, 56, 48, 40, 32, 24, 16, 8,
                           57, 49, 41, 33, 25, 17, 9, 1,
                           59, 51, 43, 35, 27, 19, 11, 3,
                           61, 53, 45, 37, 29, 21, 13, 5,
                           63, 55, 47, 39, 31, 23, 15, 7]
        
        des.sbox =  {
        "sbox1":[ [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                  [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                  [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                  [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
            
        "sbox2":[ [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                  [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                  [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                  [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
   
        "sbox3":[ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                  [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                  [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                  [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
       
        "sbox4":[ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                  [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                  [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                  [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
        
        "sbox5":[ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                  [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                  [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                  [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
       
        "sbox6":[ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                  [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                  [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                  [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
         
        "sbox7":[ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                  [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                  [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                  [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
        
        "sbox8":[ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                  [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                  [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                  [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] }
   
        des.FinalPerm = [ 40, 8, 48, 16, 56, 24, 64, 32,
                          39, 7, 47, 15, 55, 23, 63, 31,
                          38, 6, 46, 14, 54, 22, 62, 30,
                          37, 5, 45, 13, 53, 21, 61, 29,
                          36, 4, 44, 12, 52, 20, 60, 28,
                          35, 3, 43, 11, 51, 19, 59, 27,
                          34, 2, 42, 10, 50, 18, 58, 26,
                          33, 1, 41, 9, 49, 17, 57, 25 ]

        des.ExpansionDbox =  [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
                              6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
                              12, 13, 12, 13, 14, 15, 16, 17,
                              16, 17, 18, 19, 20, 21, 20, 21,
                              22, 23, 24, 25, 24, 25, 26, 27,
                              28, 29, 28, 29, 30, 31, 32, 1 ]

        des.StraightPermutation = [ 16,  7, 20, 21,
                                    29, 12, 28, 17,
                                     1, 15, 23, 26,
                                     5, 18, 31, 10,
                                     2,  8, 24, 14,
                                    32, 27,  3,  9,
                                    19, 13, 30,  6,
                                    22, 11,  4, 25 ]
        
        des.KeyPerm = [57, 49, 41, 33, 25, 17, 9,
                       1, 58, 50, 42, 34, 26, 18,
                       10, 2, 59, 51, 43, 35, 27,
                       19, 11, 3, 60, 52, 44, 36,
                       63, 55, 47, 39, 31, 23, 15,
                       7, 62, 54, 46, 38, 30, 22,
                       14, 6, 61, 53, 45, 37, 29,
                       21, 13, 5, 28, 20, 12, 4 ]
 
        des.key = des.hexTobin(key)
        des.keyPerm = des.Permutation(des.key, des.KeyPerm, 56)
        des.ShiftTable = [1, 1, 2, 2,
                          2, 2, 2, 2,
                          1, 2, 2, 2,
                          2, 2, 2, 1 ]

        des.KeyCompression = [14, 17, 11, 24, 1, 5,
                              3, 28, 15, 6, 21, 10,
                              23, 19, 12, 4, 26, 8,
                              16, 7, 27, 20, 13, 2,
                              41, 52, 31, 37, 47, 55,
                              30, 40, 51, 45, 33, 48,
                              44, 49, 39, 56, 34, 53,
                              46, 42, 50, 36, 29, 32 ]
        
        RoundKeyBits, RoundKey = des.getRoundKeys()

        des.ciphertext = des.Encrypt(text, RoundKeyBits, RoundKey) 
        # List of bits

    def Encrypt(des, plaintext, RoundKeyBits, RoundKey):
        PlainText = des.hexTobin(plaintext)

        IP = des.Permutation(PlainText, des.InitialPerm, 64)
        print("After initial permutation", des.binToHex(IP))

        left =  IP[0 :32]
        right = IP[32:64]
        print(f"After Splitting, L0={des.binToHex(left)} R0={des.binToHex(right)}")
        for round in range(0, des.NumOfRounds):
            left, right = des.Round(left, right, RoundKeyBits, RoundKey, round)
            print(f"Round, {round+1} {des.binToHex(RoundKeyBits[round])} {des.binToHex(left)} {des.binToHex(right)}.")
        combined = left+right

        cipher_text = des.Permutation(combined, des.FinalPerm, 64)

        return des.binToHex(cipher_text)


    def Round(des, left, right, RoundKeyBits, RoundKey, Round):

        RightExpanded = des.Permutation(right, des.ExpansionDbox, 48)

        Xor_RoundKey = des.xor(RightExpanded, RoundKeyBits[Round])

        sbox = des.getSbox(Xor_RoundKey)
        sbox = des.Permutation(sbox, des.StraightPermutation, 32)

        result = des.xor(left, sbox)
        left = result
        
        if Round != 15:
            left, right = right, left
        
        return left, right

    # Takes a text which can be anything like the key, a Permutation Pattern, and
    # the number of bits that will be left in the permutation. Then it loops through 
    # each bit and appends it to a string called perm. each bit is found by taking the 
    # the current number and tossing it into the PermPattern which should be preset.
    def Permutation(des, text, PermPattern, NumOfBits):
        perm = ""
        for bit in range(0, NumOfBits):
            perm += text[PermPattern[bit] - 1]
        return perm

    def Circular_Left_Shift(des, Key, Number_Of_Shifts):
        Shifted_Text = ""
        # Take the cycle through the text and add the first number to the end of 
        # the list. Do this by adding all but the first Number for Each loop. 
        for shift in range(Number_Of_Shifts):
            for EachInKey in range(1, len(Key)):
                # grab all but the first number and toss it into a string
                Shifted_Text = Shifted_Text + Key[EachInKey]
            # Now add the new first number and reset the Key so that 
            # the number has shifted to the left. 
            Shifted_Text = Shifted_Text + Key[0]
            Key = Shifted_Text
            Shifted_Text = ""
        return Key

    def getRoundKeys(des):
        RoundKeyBits = []
        RoundKey = []
        left =  des.key[0 :28]
        right = des.key[28:56]
        
        for round in range(0, des.NumOfRounds):
            left = des.Circular_Left_Shift(left, des.ShiftTable[round])
            right = des.Circular_Left_Shift(right, des.ShiftTable[round])

            combineSides = left+right
            roundkey = des.Permutation(combineSides, des.KeyCompression, 48)
            RoundKeyBits.append(roundkey)
            RoundKey.append(des.binToHex(roundkey))
        return RoundKeyBits, RoundKey

    def getSbox(des, xor):
        sbox = ""
        for i in range(0, 8):
            row = des.binToDec(int(xor[i * 6] + xor[i * 6 + 5]))
            col = des.binToDec(int(xor[i * 6 + 1] + xor[i * 6 + 2] + xor[i * 6 + 3] + xor[i * 6 + 4]))
            # Kind of complex, but this will return a string that should be an integer
            # the f ensures to use the correct sbox in the sbox list as listed in __init__.
            val = des.sbox[f'sbox{i+1}'][row][col]
            sbox += des.decToBin(val)
        return sbox

    def xor(des, Lista, Listb): 
        ans = ""
        for i in range(len(Lista)): # Should be same as b
            if Lista[i] == Listb[i]:
                ans += "0"
            else:
                ans += "1"
        return ans

    def hexTobin(des, Hex):
        HexToBinMap = {'0' : "0000",
                       '1' : "0001",
                       '2' : "0010",
                       '3' : "0011",
                       '4' : "0100",
                       '5' : "0101",
                       '6' : "0110",
                       '7' : "0111",
                       '8' : "1000",
                       '9' : "1001",
                       'A' : "1010",
                       'B' : "1011",
                       'C' : "1100",
                       'D' : "1101",
                       'E' : "1110",
                       'F' : "1111" }
        Binary = ""
        for H in range(len(Hex)):
            Binary += HexToBinMap[Hex[H]]
        return Binary

    def binToHex(des, Bin):
        BinToHexMap = {"0000" : '0',
                       "0001" : '1',
                       "0010" : '2',
                       "0011" : '3',
                       "0100" : '4',
                       "0101" : '5',
                       "0110" : '6',
                       "0111" : '7',
                       "1000" : '8',
                       "1001" : '9',
                       "1010" : 'A',
                       "1011" : 'B',
                       "1100" : 'C',
                       "1101" : 'D',
                       "1110" : 'E',
                       "1111" : 'F' }
        hex = ""
        for B in range(0,len(Bin),4):
            char = ""
            char += Bin[B]
            char += Bin[B + 1]
            char += Bin[B + 2]
            char += Bin[B + 3]
            hex += BinToHexMap[char]
            
        return hex

    def decToBin(des, dec):
        res = bin(int(dec)).replace("0b", "")
        if(len(res)%4 != 0):
            div = len(res) / 4
            div = int(div)
            counter =(4 * (div + 1)) - len(res)
            for i in range(0, counter):
                res = '0' + res
        return res

    def binToDec(des, binary):
       
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return decimal

def main():
    # Testing Class Input 1
    NumOfRounds = 16
    key  = "0F1571C947D9E859"
    text = "02468ACEECA86420"
    des = DES(key, text, NumOfRounds)
    print(des.ciphertext)

if __name__ == "__main__":
    main()