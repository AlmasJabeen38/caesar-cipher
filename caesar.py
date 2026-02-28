# Caesar Cipher Implementation
# Course: Information Security
# This program encrypts and decrypts text using Caesar Cipher

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        # Check if character is uppercase
        if char.isupper():
            # Shift within uppercase ASCII range
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # Check if character is lowercase
        elif char.islower():
            # Shift within lowercase ASCII range
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            # Keep spaces and special characters unchanged
            result += char

    return result


def caesar_decrypt(ciphertext, shift):
    result = ""

    for char in ciphertext:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            result += char

    return result


# Example usage
if __name__ == "__main__":
    message = input("Enter message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    print("Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted:", decrypted)