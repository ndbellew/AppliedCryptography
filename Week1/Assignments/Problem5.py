# HW 1
import string
import enchant
AlphaLower = string.ascii_lowercase
AlphaUpper = string.ascii_uppercase

def readFile(File):
    with open(File) as f:
        read_data = f.read()
    f.close()
    return read_data.split("\r\n")# Returns a list separated by the endline parameter for strings

def writeFile(File, Text):
    with open(File, 'w') as f:
        for sentence in Text:
            f.write(sentence+"\n")
    f.close()
        
def main():
    inputB = readFile("class_input_b.txt")
    inputC = readFile("class_input_c.txt")
    EnKey = int(input("Enter an Encryption Key\n"))%26
    outB = Encrypt(inputB, EnKey)
    outC = Decrypt(inputC)
    writeFile("class_output_b.txt", outB)
    if outC is int():
        print(outC)
    writeFile("class_output_c.txt", outC)

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
                                    # (in this instance its justa  word but will still work)
        print(Test)
        EnglishDictionary = enchant.Dict("en_US")
        if EnglishDictionary.check(Test):
            return NewText
    return 0 # Should throw error

if __name__ == "__main__":
    main()