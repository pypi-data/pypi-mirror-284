from cryptography.fernet import Fernet
import os

from dotenv import load_dotenv

load_dotenv(override=True)

# Path to the encrypted keys file
ENCRYPTED_KEYS_FILE = os.path.join(os.path.dirname(__file__), "encrypted_keys.bin")


class Authenticator:
    def __init__(self, encrypted_keys_file):
        self.encrypted_keys_file = encrypted_keys_file
        self.encryption_key = os.getenv("BULLPENFI_ENCRYPTION_KEY")
        if not self.encryption_key:
            raise ValueError("Encryption key not found in environment variables")
        self.valid_api_keys = self._decrypt_keys()

    def _decrypt_keys(self):
        with open(self.encrypted_keys_file, "rb") as f:
            encrypted_keys = f.read()
        cipher_suite = Fernet(self.encryption_key)
        decrypted_keys = cipher_suite.decrypt(encrypted_keys)
        return decrypted_keys.decode().split(",")

    def authenticate(self, api_key):
        if api_key not in self.valid_api_keys:
            raise PermissionError("Invalid API Key")


authenticator = Authenticator(ENCRYPTED_KEYS_FILE)
