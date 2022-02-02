'''
Problem 6 Hill Cipher
Bellew, Nathan

This is a Hill Cipher coder and decoder. The use of this is the modify the hardcoded text in the main function in order to actually run the cipher. 
But this can easily be modified by using python's input() function. The Cipher is able to encrypt/decrypt any m x m key so long as:
1. the key length is not prime (it will not autofill the key if its too small) and
2. the message can be correctly divided (if the message mod Key row/column length equals 0).
following these two conditions the program is able to properly encrypt or decrypt any message with a key. 

Libraries:
math
 - This program makes use of the math library, primarily for finding the squareroot of the key length. 
string
 - The string library is called in order to easily create a list of the english alphabet in lowercase. As seen below called AlphaLower.
numpy as np\
 - The numpy library is used primarily to solve some of the more difficult linear algebra math problems that are related to solving the matrices for a Hill Cipher. 
'''
import math
import string
import numpy as np

AlphaLower = string.ascii_lowercase

"""
The main function is what is called when the program is run. From here the function RunCipher is called which will run the actual cipher. I use main mostly for testing grounds but when testing is completed i removed everything and replaced it with only what is necessary.
"""
def main():
    RunCipher("textFiles/class_input_b.txt", "textFiles/class_output_b_Problem6.txt", True)
    RunCipher("textFiles/class_input_c.txt", "textFiles/class_output_c_Problem6.txt", False)
    RunCipher("textFiles//Encryption_Bellew_Input_Problem6.txt", "textFiles/Encryption_Bellew_Output_Problem6.txt", True)
    RunCipher("textFiles/Decryption_Bellew_Input_Problem6.txt", "textFiles/Decryption_Bellew_Output_Problem6.txt", False)

'''
readFile is a function that is used to read in a file and generate a list where each member of the list is a line in the file.
'''
def readFile(File):
    with open(File) as f:
        read_data = f.read()
    f.close()
    # Occasionally read in files would read an additional newline even if there were none, this is to ensure
    # that I am only reading in the first 2 lines.
    data_list = read_data.split("\n")
    data_tuple = (data_list[0], data_list[1])
    return data_tuple# Returns a list separated by the endline parameter for strings


'''
writeFile is used to write to a File where each line is determined by each member of a list.
'''
def writeFile(File, Text):
    with open(File, 'w') as f:
        for sentence in Text:
            f.write(sentence+"\n")
    f.close()

"""
Run Cipher prepares all the information for finding the answer. From the inputFile it will grab the Key and the Input Message. From the Key it willdetermine both the encryption key and the decryption key. It is not efficient to find the Decryption Key without finding the Encryption Key first. 
So even if I do not need the Decryption Key I find it easier to find both at the same time, (Process takes less than a second for small keys anyway)
"""
def RunCipher(InputFile, OutputFile, needEncrypt):
    # needEncrypt is a Boolean variable that determines if the Encrypt or Decrypt function needs to run.
    Key, InputMessage= readFile(InputFile)
    EncKey, DecKey = GetKey(Key.lower())
    if needEncrypt:
    # Outputs Encryption information into a file. I include the Key in the first line so that it mimics the initial file format.
        writeFile(OutputFile, [Key, Encrypt(EncKey, CleanPunctuation(InputMessage).lower())])
    else:
        writeFile(OutputFile, [Key, Decrypt(DecKey, CleanPunctuation(InputMessage).lower())])
    
"""
The Encryption and Decryption functions are virtually the same function. The only reason they are separated is to simplify testing. 
Thinking about creating a single function for both called HillCipher(Key, text) it should work. 
First the number of rows is determined (this is the m in the m x m).
This is used to send to CreateMatrixList which changes the text into a series of 1 x m vectors where m is the RowNum. When the List of Vectors is created I loop through the vectors and do a Matrix dot Matrix formula. 
Where the Key is multiplied against the Vector, mod 26 is then taken, and that vector has then been changed into a new vector which is the encryption/decryption.
Noted below there were some problems with multiplying matrices that were 2x2. So there is a boolean statement to cover that issue. 
After the vectors have been encrypted/decrypted the Vectors are are iterated through and the numbers modified to letters. The letters are then 
added to the CipherText which will be what is outputted to the chosen OutPutFile.
"""
def Encrypt(EncKey, text):
    RowNum = EncKey.shape[0] #np.array.shape should return m,n where m is number of rows and n is number of colums 
    # Need to turn text into 1xM where m is the total number of rows in the key.
    ListOfMessageVectors = CreateMatrixList(text, RowNum)    
    EncryptedText = ""
    for Vector in ListOfMessageVectors:
        if RowNum < 3:
            EncVector = np.matrix((np.dot(EncKey, Vector) % 26)).tolist()[0] # Rationale in Decrypt
        else:
            EncVector = np.dot(EncKey , Vector) % 26
        for letter in EncVector:
            EncryptedText += AlphaLower[letter]
    return EncryptedText

# def HillCipher(Key, text):
#     RowNum = Key.shape[0] # np.array.shape should return m,n where m is number of rows and n is number of columns 
#     # Need to turn text into 1xM where m is the total number of rows in the key.
#     ListOfMessageVectors = CreateMatrixList(text, RowNum)
#     DecryptedText = ""
#     for Vector in ListOfMessageVectors:
#         if RowNum <3:
#             # For some reason when i did the dot matrix formula on the 2x2 matrix it created an immutable
#             # matrix that I couldn't modify or iterate through so i had to force it into a python list
#             # in order to modify it because in addition to being immutable it became a 2 dimensional vector
#             # Which is not possible for vectors. 
#             DecVector = np.matrix((np.dot(Key, Vector)% 26)).tolist()[0]
#             # if the added stuff was nto done the value would be matrix([[x, y]]) instead of matrix([x,y]) and
#             # the matrix would become immutable and non-iterable.
#         else:
#             DecVector =  (np.dot(Key, Vector) % 26)
        
#         for letter in DecVector:
#             DecryptedText += AlphaLower[letter]
#     return DecryptedText

def Decrypt(DecKey, text):
    print(DecKey)
    RowNum = DecKey.shape[0]
    ListOfMessageVectors = CreateMatrixList(text, RowNum)
    DecryptedText = ""
    for Vector in ListOfMessageVectors:
        if RowNum <3:
            # For some reason when i did the dot matrix formula on the 2x2 matrix it created an immutable
            # matrix that I couldn't modify or iterate through so i had to force it into a python list
            # in order to modify it because in addition to being immutable it became a 2 dimensional vector
            # Which is not possible for vectors. 
            DecVector = np.matrix((np.dot(DecKey, Vector)% 26)).tolist()[0]
            # if the added stuff was nto done the value would be matrix([[x, y]]) instaed of matrix([x,y]) and
            # the matrix would become immutable and non-iterable.
        else:
            DecVector =  (np.dot(DecKey, Vector) % 26)
        
        for letter in DecVector:
            DecryptedText += AlphaLower[letter]
    return DecryptedText

"""
GetKey is used to find the Encryption and Decryption Key. 
The Encryption key is simple, it is made from the Key which is given by the RunCipher function and made from the first line of the input. 
The Key is used to find the m which i call matrix length, this is the squareroot of the length of the key.
From there I loop through each letter position (this is an int like i in most for loops) of the key and change it into a number by indexing the letter from the AlphaLower alphabet list.
Now that i know the location of the letter in the alphabet it is appended to the TempList.
After Appending the letter position I check to see how many letters have been added. What I am doing is creating a TempList with length m (MatrixLength) which should follow the letter+1. So if letter+1 mod m is 0 then i know that the TempList has the maximum number of numbers needed for that row of the MatrixKey.
I then add the TempList to the MatrixKey and clear TempList.
When the loop is done I convert the MatrixKey list into a numpy matrix and that is the EncryptionKey. 
From there I calculate the Decryption Key, calculating this when m is 3 or more is simple and involves a transposition. Doing it when m is 2 is harder and requires a little bit more precision. So i differentiate the two and handle a 2x2 matrix key different from a 3x3 or 4x4.
The Decryption Key is found by calculating the Determinant, then calculating the MultiplicativeInverse of that Determinant (I brute force the Multiplicative Inverse since the max length is 26).
From there I find the Adjugate Matrix for a 2x2 or the Ctrans which is C^T in linear algebra terms. Last I use the Adjugate Matrix times the Multiplicative Inverse mod 25 to calculate the Decryption Key. Or I use the Ctrans inplace of the AdjugateMatrix.
"""
def GetKey(Key):
    TempList = [] # Will hold the current working row for the matrix. I will build the matrix row by row.
    MatrixKey = [] # House the M x M list which will become a matrix later.
    EncKey, DecKey = None, None # Initialize the Keys.
    MatrixLength = int(math.sqrt(len(Key))) # Determine the M.
    for letter in range(len(Key)):
        # letter is an integer number that will be checked against to see if it has reached an M.
        TempList.append(AlphaLower.index(Key[letter]))
        if (letter+1) % MatrixLength  == 0:
            # If letter is an M, the current row needs to be added and the next row can be started.           
            MatrixKey.append(TempList)
            TempList = []
    EncKey = np.array(MatrixKey)
    # Encryption Key is just a matrixed version of the starting key text.
    if MatrixLength >= 3:
        Determinant = (round(np.linalg.det(EncKey)) % 26)
        MultiplicativeInverse = getMultiplicativeInverse(Determinant)
        Ctrans = (np.matrix.getH(EncKey) % 26).T
        DecKey = (np.dot(MultiplicativeInverse, Ctrans)%26).astype(int)
    else:
        # Had some issues with using the above formula to calculate 2x2. So I just decided to hard code this portion.
        # all test were successful on the above formula so long as m is greater than 2. 
        a, b, c, d = np.matrix.getA1(EncKey)
        Determinant = ((a*d) - (b*c) % 26)# Calculate determinant.
        MultiplicativeInverse = getMultiplicativeInverse(Determinant)
        AdjugateMatrix = np.matrix([[d, -b+26], [-c+26, a]])# Manually modify the 2x2 matrix to create an adjuage Matrix. 
        # Numbers cannot be negative so I add 26 to the negative numbers.
        DecKey = (MultiplicativeInverse * AdjugateMatrix) % 26
        # DecKey is the MultiplicativeInverse * AdjugateMatrix mod 26.
    return EncKey, DecKey

"""
CreateMatrixList will take text and m and create a matrix out of the entire text that is 1 x m
so there may be punctuation in the text which will not work for my purposes so the first if statement of the for loop ignores any punctuation or spaces.
If it is not puncutation or a space then the letter is indexed and the alphabet position is added to the TempList. 
Similar to GetKey above TempList will be added to the ListOfMessageVectors then set to [] every m loops. 
When TempList is added to ListOfMessageVectors, it is converted into a numpy matrix. 
"""
def CreateMatrixList(text, size):
    TempList = []
    ListOfMessageVectors = []
    for letter in range(len(text)):
        if text[letter].lower() not in AlphaLower:
            # This is only true for non-letters which will be ignored for this assignment
            continue
        TempList.append(AlphaLower.index(text[letter]))
        if (letter+1) % size == 0:
            # for every size loops, where size is the m of the m x m key, the new TempList will be added as a numpy matrix.
            ListOfMessageVectors.append(np.array(TempList))
            TempList = []
        # ListOfMessageVectors should be a List of Matrices that are all 1xm where m==size
    return ListOfMessageVectors

"""
getMultiplicativeInverse brute forces the MultiplicativeInverse.
The MI is calculated by checking if (MI * Determinant) % 26 == 1. If so then whatever that MI is is the Multiplicative Inverse.
"""
def getMultiplicativeInverse(Determinant):
    for x in range(26):
        # English alphabet only has 26 letters so it has to be one of the 26
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