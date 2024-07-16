from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import os
from datetime import datetime

def generate_key():
    return get_random_bytes(16)  # AES-128 bit key

def save_key_to_pem(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

def load_key_from_pem(filename):
    with open(filename, 'rb') as file:
        return file.read()

def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    return iv, ct

def aes_decrypt(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def encryption_workflow():
    text = input("Enter the text to encrypt: ")
    key = generate_key()
    iv, encrypted_text = aes_encrypt(text, key)
    
    print(f"Original Text: {text}")
    print(f"Encrypted Text: {encrypted_text}")

    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    encrypted_filename = f"encrypted_{current_time}.bj"
    key_filename = f"key_{current_time}.pem"
    iv_filename = f"iv_{current_time}.iv"
    
    save_to_file(encrypted_filename, encrypted_text)
    save_key_to_pem(key, key_filename)
    save_to_file(iv_filename, iv)

    print(f"Encrypted text saved to file: {encrypted_filename}")
    print(f"Key saved to file: {key_filename}")
    print(f"IV saved to file: {iv_filename}","\n")

def decryption_workflow():
    encrypted_filename = input("Enter the filename to decrypt: ")
    key_filename = input("Enter the key filename (.pem) to use: ")
    iv_filename = input("Enter the IV filename (.iv) to use: ")
    
    key = load_key_from_pem(key_filename)
    with open(encrypted_filename, 'r') as file:
        encrypted_text = file.read().strip()
    with open(iv_filename, 'r') as file:
        iv = file.read().strip()
    
    decrypted_text = aes_decrypt(iv, encrypted_text, key)
    
    print(f"Decrypted Text: {decrypted_text}")

    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_filename = f"decrypted_{current_time}.dec"
    save_to_file(output_filename, decrypted_text)
    print(f"Decrypted text saved to file: {output_filename}")
    
    # Print decrypted text after saving
    print(f"Decrypted Text Output: {decrypted_text}","\n")

def main():
    while True:
        print("Select an option:")
        print("1. Encrypt a text")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            encryption_workflow()
        elif choice == '2':
            decryption_workflow()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
