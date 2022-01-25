# HW 1
import string
AlphaLower = string.ascii_lowercase
AlphaUpper = string.ascii_uppercase

def readFile(File):
    with open(File) as f:
        read_data = f.read()
    f.close()
    return read_data

def writeFile(File, data):
    with open(File) as f:
        f.write(data)
    f.close()
        
def main():
    inputB = readFile("class_input_b.txt")
    inputC = readFile("class_input_c.txt")
    EnKey = int(input("Enter an Encryption Key\n"))%26
    outB = Encrypt(inputB, EnKey)
    writeFile("class_output_b.txt", outB)

def Encrypt(Text, Key):
    NewText = ""
    for letter in Text:
        if letter in AlphaLower:
            index = AlphaLower.index(letter)
            print(index)
            NewText += AlphaLower[((index+Key)%len(AlphaLower))]
        elif letter in AlphaUpper:
            index = AlphaUpper.index(letter)
            NewText += AlphaUpper[((index+Key)%len(AlphaUpper))]
        else:
            # Punctuation or spaces
            NewText += letter
    return NewText

def Decrypt(Text, Key):
    pass

if __name__ == "__main__":
    main()