# Caesar Cipher
'''
This is a Caesar Cipher program that is able to read in two files, one can be encrypted and the other can be decrypted. The files are
hardcoded as class_input_b and class_input_c the output is the same but the word output replaces input. For this program two external libaries are being used.

The String library is used to make modifications with the string type, but in this instance it is used to automatically generate a list of upper and lowercase alphabets. 

The enchant library is a massive multi-language library that can confirm and sometimes autocorrect english words. This is used to decrypt caesar cipher and check for an
english word. 
'''


import string
#import enchant
AlphaLower = string.ascii_lowercase
AlphaUpper = string.ascii_uppercase

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
    inputB = readFile("textFiles/class_input_b.txt")
    inputC = readFile("textFiles/class_input_c.txt")
    MyInputEnc = readFile("textFiles/my_input_for_Encryption.txt")
    MyInputDec = readFile("textFiles/my_input_for_Decryption.txt")
    EnKey = AlphaLower.index(inputB[0][0].lower())+1
    outB = Encrypt(inputB, EnKey)
    #outC = Decrypt(inputC)
    MyOutEnc = Encrypt(MyInputEnc, EnKey)
    #MyOutDec = Decrypt(MyInputDec)
    writeFile("textFiles/class_output_b.txt", outB)
    #writeFile("textFiles/class_output_c.txt", outC)
    writeFile("textFiles/my_output_for_Encryption.txt", MyOutEnc)
    #writeFile("textFiles/my_output_for_Decryption.txt", MyOutDec)

def Encrypt(Text, Key):
    NewText = []
    NewSentence = ""
    for sentence in Text:
        for letter in sentence:
            if letter in AlphaLower:
                index = AlphaLower.index(letter)
                NewSentence += AlphaLower[((index+Key)%len(AlphaLower))]
            elif letter in AlphaUpper:
                index = AlphaUpper.index(letter)
                NewSentence += AlphaUpper[((index+Key)%len(AlphaUpper))]
            else:
                # Punctuation or spaces
                NewSentence += letter
        NewText.append(NewSentence)
    return NewText

def Decrypt(Text):
    for Key in range(26):
        NewText = []
        NewSentence = ""
        for sentence in Text:
            for letter in sentence:
                if letter in AlphaLower:
                    index = AlphaLower.index(letter)
                    NewSentence += AlphaLower[((index+Key)%len(AlphaLower))]
                elif letter in AlphaUpper:
                    index = AlphaUpper.index(letter)
                    NewSentence += AlphaUpper[((index+Key)%len(AlphaUpper))]
                else:
                    # Punctuation or spaces
                    NewSentence += letter
            NewText.append(NewSentence)
        Test = NewText[0].split()[0] # This will take a sentence and split it down into a single word
                                    # (in this instance its just a  word but will still work)
        print(Test)
        EnglishDictionary = enchant.Dict("en_US")
        if EnglishDictionary.check(Test):
            return NewText
    FailureText = f"Unable to Decrypt {' '.join(NewText)} it may not be Caesar Cipher"
    return FailureText # Should throw error

if __name__ == "__main__":
    main()