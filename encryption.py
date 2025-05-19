import os
from cryptography.fernet import Fernet

KEY_FILE = 'secret.key'
TRANSFER_FOLDER = 'transferred_files'

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as file:
        original_data = file.read()
    
    encrypted_data = fernet.encrypt(original_data)
    filename = os.path.basename(file_path)
    
    encrypted_path = os.path.join(TRANSFER_FOLDER, f"encrypted_{filename}")
    with open(encrypted_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    return encrypted_path

def decrypt_file(file_path, output_name="decrypted_output"):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        return None, str(e)
    
    output_path = os.path.join(TRANSFER_FOLDER, output_name)
    with open(output_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    return output_path, "Decryption successful"
