def caesar_encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result +=char
    return result

def caesar_decrypt(text,shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt: ").lower()
    message = input("Enter Your message:")
    shift = int(input("Enter the shift value (e.g., 3):"))

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'd':
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Use 'E' or 'D'.")

main()