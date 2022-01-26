'''
Problem 6 Hill Cipher
'''
import math
import string
import numpy as np

AlphaLower = string.ascii_lowercase

'''
readFile is a function that is used to read in a file and generate a list where each member of the list is a line in the file.
'''
def readFile(File):
    with open(File) as f:
        read_data = f.read()
    f.close()
    return read_data.split("\r\n")# Returns a list separated by the endline parameter for strings


'''
writeFile is used to write to a File where each line is determined by each member of a list.
'''
def writeFile(File, Text):
    with open(File, 'w') as f:
        for sentence in Text:
            f.write(sentence+"\n")
    f.close()

def main():
    InputToEncrypt = readFile("textFiles/class_input_b.txt")
    InputToDecrypt = readFile("textFiles/class_input_c.txt")
    EncKey = GetKey(InputToEncrypt[0].lower())
    print(EncKey)

def Encrypt():
    pass

def Decrypt():
    pass

def GetKey(text):
    TempList = []
    MatrixLength = int(math.sqrt(len(text)))
    for i in text:
        TempList.append(AlphaLower.index(i))
    MatrixKey = np.array(TempList)
    return MatrixKey

if __name__ == "__main__":
    main()