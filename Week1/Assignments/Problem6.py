'''
Problem 6 Hill Cipher
'''
import math
import string
import numpy as np

EnglishDictionary = enchant.Dict("en_US")
AlphaLower = string.ascii_lowercase

'''
readFile is a function that is used to read in a file and generate a list where each member of the list is a line in the file.
'''
def readFile(File):
    with open(File) as f:
        read_data = f.read()
    f.close()
    return read_data.split("\n")# Returns a list separated by the endline parameter for strings


'''
writeFile is used to write to a File where each line is determined by each member of a list.
'''
def writeFile(File, Text):
    with open(File, 'w') as f:
        for sentence in Text:
            f.write(sentence+"\n")
    f.close()

def main():
    Key, InputToEncrypt = readFile("textFiles/HillEncryptionInputTest.txt")
    EncKey, DecKey = GetKey(Key.lower())
    print(EncKey)
    print(DecKey)
    writeFile("textFiles/HillEncryptionOut.txt", [Key, Encrypt(EncKey, CleanPunctuation(InputToEncrypt).lower())])
    Key, InputToDecrypt, _ = readFile("textFiles/HillEncryptionOut.txt")
    writeFile("textFiles/HillDecryptionOut.txt", [Key, Decrypt(DecKey, CleanPunctuation(InputToDecrypt).lower())])

def Encrypt(EncKey, text):
    RowNum = EncKey.shape[0] #np.array.shape should return m,n where m is number of rows and n is number of colums 
    # Need to turn text into 1xM where m is the total number of rows in the key.
    ListOfMessageVectors = CreateMatrixList(text, RowNum)    
    EncryptedText = ""
    for Vector in ListOfMessageVectors:
        EncVector = np.dot(EncKey , Vector) % 26
        for letter in EncVector:
            EncryptedText += AlphaLower[letter]
    return EncryptedText

def Decrypt(DecKey, text):
    RowNum = DecKey.shape[0]
    ListOfMessageVectors = CreateMatrixList(text, RowNum)
    DecryptedText = ""
    for Vector in ListOfMessageVectors:
        DecVector =  np.dot(DecKey, Vector) % 26
        for letter in DecVector:
            DecryptedText += AlphaLower[letter]
    # return enchantText(DecryptedText)
    return DecryptedText

def GetKey(text):
    TempList = []
    MatrixKey = []
    EncKey, DecKey = None, None
    MatrixLength = int(math.sqrt(len(text)))
    for letter in range(len(text)):
        TempList.append(AlphaLower.index(text[letter]))
        if (letter+1) % MatrixLength  == 0:            
            MatrixKey.append(TempList)
            TempList = []
    EncKey = np.array(MatrixKey)
    if MatrixLength >= 3:
        Determinant = (int(np.linalg.det(EncKey)) % 26)
        MultiplicativeInverse = getMultiplicativeInverse(Determinant)
        Ctrans = (np.matrix.getH(EncKey) % 26).T
        DecKey = (np.dot(MultiplicativeInverse, Ctrans)%26).astype(int)
    else:
        a, b, c, d = np.matrix.getA1(EncKey)
        Determinant = ((a*d) - (b*c) % 26)
        MultiplicativeInverse = getMultiplicativeInverse(Determinant)
        AdjugateMatrix = np.matrix([[d, -b+26], [-c+26, a]])
        DecKey = MultiplicativeInverse * AdjugateMatrix
    return EncKey, DecKey

def CreateMatrixList(text, size):
    TempList = []
    ListOfMessageVectors = []
    for letter in range(len(text)):
        if text[letter].lower() not in AlphaLower:
            continue
        #print(letter, text[letter])
        TempList.append(AlphaLower.index(text[letter]))
        if (letter+1) % size == 0:
            ListOfMessageVectors.append(np.array(TempList))
            TempList = []
    return ListOfMessageVectors

def getMultiplicativeInverse(Determinant):
    for x in range(100):
            if (x * Determinant) % 26 == 1:
                return x

"""
The Logic for incorporating spaces and punctuation is not normally used in the Hill Cipher. I know this from the class input
file, so to generalize this, a user can put any phrase or sentence in regardless of punctuation and still get a result. 
This function Clean Punctuation just removes Punctuation and spaces from the text.
"""
def CleanPunctuation(Text):
    NewText = ""
    for Letter in Text:
        if Letter.lower() in AlphaLower:
            NewText+=Letter
    return NewText

if __name__ == "__main__":
    main()