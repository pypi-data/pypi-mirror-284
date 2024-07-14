from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance (run this once and save the key)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message.
    
    Args:
        message (str): The message to encrypt.
    
    Returns:
        str: The encrypted message.
    """
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message.
    
    Args:
        encrypted_message (str): The encrypted message to decrypt.
    
    Returns:
        str: The decrypted message.
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

# Example usage
# generate_key()  # Run once to generate and save the key
# encrypted = encrypt_message("Hello, World!")
# print(f'Encrypted: {encrypted}')
# decrypted = decrypt_message(encrypted)
# print(f'Decrypted: {decrypted}')
