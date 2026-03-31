def august_cipher_encrypt(text):
    encrypted_message = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + 1) % 26 + start
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def august_cipher_decrypt(text):
    decrypted_message = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start - 1) % 26 + start
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message

if __name__ == "__main__":
    original_message = "Hello, World! This is the August Cipher."
    print("Original: ", original_message)

    encrypted = august_cipher_encrypt(original_message)
    print("Encrypted:", encrypted)

    decrypted = august_cipher_decrypt(encrypted)
    print("Decrypted:", decrypted)