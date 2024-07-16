from cryptography.fernet import Fernet
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv(override=True)

# Embedded encrypted keys
ENCRYPTED_KEYS = b"gAAAAABmlU0dJpNsnxGZjj2jBHjV1JJIyq2wOv4gtMGzY9KW9WFjuzm9SkIKTuuITIAuRh8GWAyZJBdclqwD3o5UhqkI35pHAPYZc3xK7_j8elQeJ5oxTQpu582u_1Ak37KBpylt9enYysOkSjZh81Cwr6-d2npdZwhdsIPb9L747TSLVjxPJT_tdhrFO0RXre7kr5UBocBTf_kCLJNP7z3GNTHvdjNyP9AbjLvn3FqGxDfjMoDU2M9zXbcffs7-_bMqxpobU3EH7EahGYCjNUGNHTDHL03irLWdyAjVUSbGLcZ_F0Lxi_j5zKuWTNfPOs64aMtri-CkO1ASUKOYMAmHTuSsKzbhlNwhnfYPh8FfqRxpxbbraSE="


class Authenticator:
    def __init__(self, encrypted_keys):
        self.encrypted_keys = encrypted_keys
        self.encryption_key = os.getenv("BULLPENFI_ENCRYPTION_KEY")
        if not self.encryption_key:
            raise ValueError("Encryption key not found in environment variables")
        self.valid_api_keys = self._decrypt_keys()

    def _decrypt_keys(self):
        cipher_suite = Fernet(self.encryption_key)
        decrypted_keys = cipher_suite.decrypt(self.encrypted_keys)
        return decrypted_keys.decode().split(",")

    def authenticate(self, api_key):
        if api_key not in self.valid_api_keys:
            raise PermissionError("Invalid API Key")


authenticator = Authenticator(ENCRYPTED_KEYS)

logger.info("Authenticator initialized with embedded encrypted keys")
