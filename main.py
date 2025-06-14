#Basic Encryption Cipher by JustinPhi

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shouldEnd = False
while not shouldEnd:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    #note for future imporovements: make it so they can enter symbols and spaces as well
    text = input("Type your message (letters only):\n").lower()
    shift = int(input("Type a number for your encryption key:\n"))
    #using modulus (%) incase someone enters a message that is greater than 26 (the size of our array)
    shift = shift % 26

    def encrypt(plainText, shiftAmount):
        cipherText = ""
        for letter in plainText:
            position = alphabet.index(letter)
            newPosition = position + shiftAmount
            newLetter = alphabet[newPosition]
            cipherText += newLetter
        print(f"Your coded text = {cipherText}")

    def decrypt(cipherText, shiftAmount):
        plainText = ""
        for letter in cipherText:
            position = alphabet.index(letter)
            newPosition = position - shiftAmount
            plainText += alphabet[newPosition]
        print(f"Your decoded text = {plainText}")

    if direction == "encode":
        encrypt(plainText=text, shiftAmount=shift)
    elif direction == "decode":
        decrypt(cipherText=text, shiftAmount=shift)

    restart = input("Type 'y' if you want to encode or decode another message. Otherwise type 'n'.\n")
    if restart == "n":
        shouldEnd = True
        print("\nGoodbye")

