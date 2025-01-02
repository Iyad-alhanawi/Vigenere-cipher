import numpy as np
import string

def vigenere_cipher():
    # Prompt user for choice of operation
    choice = input("Do you want to perform Vigenère encryption or decryption? (Type 'encryption' or 'decryption'):\n").strip().lower()

    # Initialize alphabet array
    alpha = np.array(list(string.ascii_lowercase))

    # Function to encrypt the plaintext
    def encrypt(plain_text, cipher_key):
        # Prepare indices for plaintext and cipher key
        plain_index = np.array([ord(char) - 97 for char in plain_text if char != ' '])
        key_indices = np.array([ord(char) - 97 for char in cipher_key if char != ' '])

        # Extend key indices to match the length of the plaintext
        while len(key_indices) < len(plain_index):
            key_indices = np.append(key_indices, key_indices[len(key_indices) % len(cipher_key)])

        # Encrypt the plaintext
        cipher_index = (plain_index + key_indices) % 26
        cipher_text = ''.join(chr(i + 97) for i in cipher_index)

        return cipher_text

    # Function to decrypt the ciphertext
    def decrypt(cipher_text, cipher_key):
        # Prepare indices for ciphertext and cipher key
        cipher_index = np.array([ord(char) - 97 for char in cipher_text if char != ' '])
        key_indices = np.array([ord(char) - 97 for char in cipher_key if char != ' '])

        # Extend key indices to match the length of the ciphertext
        while len(key_indices) < len(cipher_index):
            key_indices = np.append(key_indices, key_indices[len(key_indices) % len(cipher_key)])

        # Decrypt the ciphertext
        plain_index = (cipher_index - key_indices) % 26
        plain_text = ''.join(chr(i + 97) for i in plain_index)

        return plain_text

    # Execute based on user choice
    if choice == "encryption":
        plain_text = input("Enter your plain text:\n").strip().lower()
        cipher_key = input("Enter your key :\n").strip().lower()
        cipher_text = encrypt(plain_text, cipher_key)
        print("Encrypted text:", cipher_text)
    
    elif choice == "decryption":
        cipher_text = input("Enter your cipher text :\n").strip().lower()
        cipher_key = input("Enter your key :\n").strip().lower()
        plain_text = decrypt(cipher_text, cipher_key)
        print("Decrypted text:", plain_text)
    
    else:
        print("Invalid choice. Please select 'encryption' or 'decryption'.")

# Run the Vigenère cipher program
vigenere_cipher()