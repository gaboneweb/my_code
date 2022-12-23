alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(message_,key):
    encrypted_message = ''
    for char in message_:
        if char.isalpha():
           index = alphabet.index(char.upper())
           if index + key <= 26:
              encrypted_message += alphabet[index+key]
           else:
              encrypted_message += alphabet[index+key - 26]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message_,key):
    dencrypted_message = ''
    for char in message_:
        if char.isalpha():
           index = alphabet.index(char.upper())
           if index - key >= 0:
              dencrypted_message += alphabet[index-key]
           else:
              dencrypted_message += alphabet[26 - index ]
        else:
            dencrypted_message += char
    return dencrypted_message

if __name__ == "__main__":
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    decision = input("> ")

    print("Please enter the key (0 to 25) to use.")
    key = int(input("> "))

    print("Enter the message to encrypt.")
    message_ = input("> ")
    if decision.lower() == 'd':
        print(decrypt(message_,key))
    elif decision.lower() == 'e':
        print(encrypt(message_,key))