# Caesar Cipher
import art
print("**************** Welcome To ****************")
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)


def caesar(direction,text,shift):

    if direction== "encode":
        encrypt_text = ""
        for x in text:
            if x in alphabet:
                place = alphabet.index(x)
                shifted_index = place + shift
                if shifted_index >= len(alphabet):
                     new_index=shifted_index-len(alphabet)
                     encrypt_text=encrypt_text+alphabet[new_index]
                else:
                    encrypt_text += alphabet[shifted_index]
            else:
                encrypt_text+=x
        print(f"The encrypted message is: {encrypt_text}")
        user_choice=input("Do you want to start again? Type 'Yes' or 'No': \n").lower()
        if user_choice=="yes":
            start()
        else:
            print("*******Good Bye*******")
            exit()

    elif direction == "decode":
        decrypt_text = ""
        for x in text:
            if x in alphabet:
                current_index = alphabet.index(x)
                shifted_index = current_index - shift
                if shifted_index < 0:
                    new_index = len(alphabet) + shifted_index
                    decrypt_text += alphabet[new_index]
                else:
                    decrypt_text += alphabet[shifted_index]
            else:
                decrypt_text+=x
        print(f"The decrypt message is: {decrypt_text}")
        user_choice = input("Do you want to start again? Type 'Yes' or 'No': \n").lower()
        if user_choice == "yes":
            start()
        else:
            print("*******Good Bye*******")
            exit()

    else:
        print("Invalid choice.Try again.")
        user_choice = input("Do you want to start again? Type 'Yes' or 'No': \n").lower()
        if user_choice == "yes":
            start()
        else:
            print("*******Good Bye*******")
            exit()


start()
