import hashlib
import os
from datetime import datetime

def generate_signature(file_path, secret_key):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Calculate SHA-256 hash with secret key
    sha256 = hashlib.sha256()
    sha256.update(file_data)
    sha256.update(secret_key.encode('utf-8'))  # Convert secret_key to bytes
    signature = sha256.hexdigest()

    return signature

def save_signature(file_path, signature):
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    signature_filename = f"{file_path}.sig"
    
    with open(signature_filename, 'w') as file:
        file.write(signature)
    
    print(f"Digital signature saved to file: {signature_filename}","\n")

def load_signature(signature_file):
    with open(signature_file, 'r') as file:
        return file.read().strip()

def verify_signature(file_path, signature_file, secret_key):
    signature = load_signature(signature_file)
    
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # Calculate SHA-256 hash with secret key
    sha256 = hashlib.sha256()
    sha256.update(file_data)
    sha256.update(secret_key.encode('utf-8'))  # Convert secret_key to bytes
    calculated_signature = sha256.hexdigest()
    
    if calculated_signature == signature:
        print("Digital signature is valid.","\n")
    else:
        print("Digital signature is invalid.","\n")

def main():
    while True:
        print("Select an option:")
        print("1. Generate Digital Signature")
        print("2. Verify Digital Signature")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            file_path = input("Enter the .bj file to generate signature: ")
            if os.path.exists(file_path):
                secret_key = input("Enter the secret key: ")
                signature = generate_signature(file_path, secret_key)
                save_signature(file_path, signature)
            else:
                print("File not found.")
        
        elif choice == '2':
            file_path = input("Enter the .bj file path to verify signature: ")
            signature_file = input("Enter the .sig file path to verify signature: ")
            
            if os.path.exists(file_path) and os.path.exists(signature_file):
                secret_key = input("Enter the secret key: ")
                verify_signature(file_path, signature_file, secret_key)
            else:
                print("File or signature file not found.")

        elif choice == '3':
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
