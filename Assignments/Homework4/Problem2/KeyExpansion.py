from re import X
import sys, hashlib, string, getpass
from copy import copy, deepcopy
from random import randint

sboxOrig = [
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5','30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0','ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc','34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a','07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0','52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b','6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85','45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5','bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17','c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88','46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c','c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9','6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6','e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e','61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94','9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68','41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
]

reverse_aes_sbox = [
    ['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
    ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
    ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
    ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
    ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
    ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
    ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
    ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
    ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
    ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
    ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
    ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
    ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
    ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
    ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
    ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']
]

Rcon = {1:"01", 2:"02", 3:"04", 4:"08", 5:"10", 
        6:"20", 7:"40", 8:"80", 9:"1B", 10:"36"}

KeyExpansionTable = []

def XOR(left, right):
    Value = hex(int(left, 16) ^ int(right, 16))[2:]
    # Validate that the equation creates the correct output. Sometimes it will put 7 instead of 07
    # String = split_string(Value).split()
    # for i in range(len(String)):
    #     if len(String[i])<2:
    #         String[i] = "0"+String[i]
    return Value

def Hex2Dec(Hex):
    switcher={
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15
    }
    return switcher.get(Hex, "xxInvalid")

def RotWord(word):
    temp = word[0]
    word.remove(word[0])
    word.append(temp)
    return word

def SubWord(Hex):
    Left, Right = Hex.upper()
    Left = Hex2Dec(Left)
    Right = Hex2Dec(Right)
    return sboxOrig[Left][Right]

def KeyExpansion(Key):
    w0 = Key[0:4]
    w1 = Key[4:8]
    w2 = Key[8:12]
    w3 = Key[12:16]
    print(w0,w1,w2,w3)
    Keys = []
    Keys.append([w0,w1,w2,w3])
    KeyWords = []
    AuxFunc = []
    KeyWords.append(f"|W0 = {' '.join(w0)}<br>W1 = {' '.join(w1)}<br>W2 = {' '.join(w2)}<br>W3 = {' '.join(w3)}")
    for round in range(10):
        incr = round+1
        x = ""
        y=""
        z=""
        ans = []
        temp = w3
        w3 = tuple(w3) # Kept getting modified so made it a tuple. 
        x = RotWord(temp)
        print(f"RotWord(W{round*4+3}) = {' '.join(x)}")
        for i in x:
            ans.append(SubWord(i))
        print(f"SubWord(X{incr}) = {' '.join(ans)}")
        y = "".join(ans)
        print(f"Rcon ({incr}) = {split_string(Rcon[incr])} 00 00 00")
        z = XOR(y[:2], Rcon[incr])
        z = z + y[2:]
        AuxFunc.append(f"|RotWord(W{round*4+3}) = {' '.join(x)}<br>SubWord(X{incr}) = {' '.join(ans)}<br>Rcon ({incr}) = {split_string(Rcon[incr])} 00 00 00<br>y xor Rcon = {split_string(z)}|")

        print(f"y xor Rcon = {split_string(z)}")
        print("__________________________________________________________")
        w0 = split_string(XOR("".join(w0), z)).split()
        print(f"W{incr*4} = W{round*4} Xor z = {' '.join(w0)}")

        w1 = split_string(XOR("".join(w0), "".join(w1))).split()
        print(f"W{incr*4+1} = W{incr*4} Xor W{round*4+1}  = {' '.join(w1)}")

        w2 = split_string(XOR("".join(w1), "".join(w2))).split()
        print(f"W{incr*4+2} = W{incr*4+1} Xor W{round*4+2}  = {' '.join(w2)}")

        w3 = split_string(XOR("".join(w2), "".join(w3))).split()
        print(f"W{incr*4+3} = W{incr*4+2} Xor W{round*4+3}  = {' '.join(w3)}")
        KeyWords.append(f"|W{incr*4} = W{round*4} $\oplus$ z = {' '.join(w0)}<br>W{incr*4+1} = W{incr*4} $\oplus$ W{round*4+1}  = {' '.join(w1)}<br>W{incr*4+2} = W{incr*4+1} $\oplus$ W{round*4+2}  = {' '.join(w2)}<br>W{incr*4+3} = W{incr*4+2} $\oplus$ W{round*4+3}  = {' '.join(w3)}")
        Keys.append([w0,w1,w2,w3])
        if incr == 10:
            AuxFunc.append("|Empty|")
    return AuxFunc, KeyWords, Keys

def aes(Keys):
    pass

def main():
#   Key = "0e 00 71 c9 47 d9 e8 59 1c b7 ad d6 af 7f 67 98".split()
    Key = "0f 55 71 c9 47 d9 e8 59 0c b7 ad d6 af 7f 67 98".split()
    PlainText = "22 00 45 67 89 ab cd ef fe dc ba 98 76 54 32 10".split()
    Aux, KeyWords, AllKeys = KeyExpansion(Key)
    aes(AllKeys)
    Table = []
    for i in range(len(KeyWords)):
        Table.append(KeyWords[i]+Aux[i])
    with open("KeyExpansionTable.txt", 'w+') as f:
        for items in Table:
            f.write('%s\n' %items)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def split_string(s):
    return " ".join(chunks(s, n=2))

if  __name__ == "__main__":
    main()