def caesar(word, shiftNumber, decodeEncode):
    deCipherText = ""
    if decodeEncode == "decode":
        shiftNumber *= -1
    for char in word:
        if char not in alphabet:
            deCipherText += word
        else:
            shiftedPosition = alphabet.index(char) + shiftNumber
            shiftedPosition %= len(alphabet)
            deCipherText += alphabet[shiftedPosition]
    print(f"Your {decodeEncode}d text is {deCipherText}")


print("CAESAR CIPHER")
rerun = True

while rerun:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(word=text, shiftNumber=shift, decodeEncode=direction)

    restart = input("Type 'yes' to continue or 'no' to stop: ").lower()
    if restart == "no":
        rerun = False
        print("Goodbye!")