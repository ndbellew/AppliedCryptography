from random import randint

DestFolder = "Inputs/thisAttempt"
for i in range(1000):
    Key = hex(randint(0,18446744073709551615))[2:].upper()
    while len(Key) < 16:
        Key+="F"
    Plaintext = hex(randint(0,18446744073709551615))[2:].upper()
    while len(Plaintext) < 16:
        Plaintext += "A"
    with open(f"{DestFolder}{i}.txt", 'w') as Writer:
        Writer.write("16\n"
                     f"{Key}\n"
                     f"{Plaintext}")