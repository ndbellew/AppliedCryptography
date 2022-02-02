'''
Problem 5 Caesar Cipher
Bellew, Nathan
The Caesar cipher is one of the first ciphers everyone learns to code first and while this isnt the first time I have done it, it is the first time I will be graded for it. This program will take in a file input, file output, and either encrypt or decrypt depending on the need.  It uses a function called RunCipher which is used to generate the Encryption Key and Decryption Key from the first letter of the key text (line 1 of the input). Using the Key it will perform the necessary actions to get the desired output. Below I used AlphaLower and AlphaUpper as two lists of the english alphabet in both upper and lowercase. This way I can encrypt/decrypt Caesar Cipher messages with or without capitalization.
Libraries:
String
 - The String library is used to make modifications with the string type, but in this instance it is used to automatically generate a list of upper and lowercase alphabets. 


'''

import string

AlphaLower = string.ascii_lowercase
AlphaUpper = string.ascii_uppercase

"""
 Main is called when the program starts it is where most of my testing is completed when building the program. 
 In Main I send RunCipher an InputFile, OutputFile, and True Or False. True means the text should be encrypted, False means it should be Decrypted. 
 Outputs can be found on the corresponding Output files. 
"""
def main():
    # RunCipher( Input File Name, Output File Name, This Needs to be Encrypted True or False?)
    RunCipher("textFiles/class_input_b.txt", "textFiles/Bellew_Output_5b.txt", True)
    RunCipher("textFiles/Bellew_Output_5b.txt", "textFiles/TestOutput.txt", False)

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
            f.write(f"{sentence}\n")
    f.close()

"""
Run Cipher will prepare the Key and input message for encryption or decryption.
the Key and Mesage are extracted from the InputFile text. The Key is the first line and the message is the second. 
Once I have the starting Key I need to modify it into the Encryption Key. The Key is usually a long word but only the first letter is the actual Key 
So the encryption Key is the first letter of the Key + 1 (This is because I will use the Key to move the letters up or down the alphabet if I take the indexing of the key as is then the letter 'A' will be 0 and if my key is 0 then the output would look the same as the input. Therefore I add 1 so that 'A' would equal 1 instead of 0). The Decryption key should be the negative version of the Encryption Key, I verified this on Cryptii.com a cipher site. 
From there I write to a file using the CaesarCipher function to modify the input Text. Notice that I send either the EncKey or the DecKey. 
This is decided based on if needEncrypt is true or not. If its True then I send the Encryption Key.
"""
def RunCipher(InputFile, OutputFile, needEncrypt):
    Key, InputMessage = readFile(InputFile)
    # Key is only the first letter of the string so it needs to be modified here
    EncKey = AlphaLower.index(Key[0].lower())+1 
    # First letter of the Key word indexed into an integer based on position.
    #I am under the assumption that if the key is A then A=1 so I add 1 to the Key
    DecKey = EncKey*-1
    # DecKey should be the negative encKey
    if needEncrypt:
        # Needs to be encrypted send the Encryption Key
        writeFile(OutputFile, [Key, CaesarCipher(EncKey, InputMessage)])
    else:
        # Needs to be Decrypted send the Decryption Key
        writeFile(OutputFile, [Key, CaesarCipher(DecKey, InputMessage)])

"""
CaesarCipher applies the actual cipher to the message and returns the encrypted/decrypted message.
NewText will be the newly encrypted/decrypted text, letters will be added to it as they are encrypted/decrypted.
I loop through each letter in the Text (including punctuation, spaces, and numbers).
    If the letter is in the alphabet and is lowercase then i modify the letter according to the Key that was sent. Then the new letter is added to NewText
    If the letter is in the alphabet but uppercase i do the same as above but its an uppercase letter instead.\
    If it is not a letter it is not modified and added to the NewText that way it contain everything and only the numbers are changed.
When the looping is Done I should be left with a new text that has either been encrypted or decrypted from the original Text.
"""
def CaesarCipher(Key, Text):
    NewText = "" # Answer
    for letter in Text:
        # First two statements do the same thing but for upper and lowercase letters
        if letter in AlphaLower:
            # to change the letter in the word i need to change the position so i first index the letter and get the position it is in the alphabet. 
            index = AlphaLower.index(letter)
            # Next I modify the Index by adding the Key, mod it by the length of the alphabet (26)
            # At the sametime I find the letter that the new number is equivalent to and add it to the NewText
            NewText += AlphaLower[((index+Key) % 26)]
        elif letter in AlphaUpper:
            index = AlphaUpper.index(letter)
            NewText += AlphaUpper[((index+Key) % 26)]
        else:
            # Punctuation or spaces or numbers
            NewText += letter
    return NewText

if __name__ == "__main__":
    main()