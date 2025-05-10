# Functions for secure data encryption and storage
from typing import Dict, Optional, Any
import base64
import hashlib
import json
from cryptography.fernet import Fernet, InvalidToken
from passlib.hash import pbkdf2_sha256
import os
from config import config
from pathlib import Path

class EncryptionError(Exception):
    """Custom exception for encryption-related errors."""
    pass

def generate_key(passkey: str) -> bytes:
    """Generate a Fernet key from a passkey and system encryption key."""
    try:
        # Combine user passkey with system encryption key for added security
        system_key = config.get_encryption_key()
        combined_key = f"{passkey}{system_key}"
        return base64.urlsafe_b64encode(hashlib.sha256(combined_key.encode()).digest())
    except Exception as e:
        raise EncryptionError(f"Failed to generate key: {str(e)}")

def hash_passkey(passkey: str) -> str:
    """Hash a passkey using PBKDF2."""
    try:
        return pbkdf2_sha256.hash(passkey)
    except Exception as e:
        raise EncryptionError(f"Failed to hash passkey: {str(e)}")

def verify_passkey(hashed_passkey: str, input_passkey: str) -> bool:
    """Verify a passkey against its hash."""
    try:
        return pbkdf2_sha256.verify(input_passkey, hashed_passkey)
    except Exception:
        return False

def encrypt_data(plain_text: str, passkey: str) -> str:
    """Encrypt data using Fernet symmetric encryption."""
    try:
        key = generate_key(passkey)
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(plain_text.encode())
        return encrypted_data.decode()
    except Exception as e:
        raise EncryptionError(f"Failed to encrypt data: {str(e)}")

def decrypt_data(encrypted_text: str, stored_passkey_hash: str, input_passkey: str) -> Optional[str]:
    """Decrypt data using Fernet symmetric encryption."""
    if not verify_passkey(stored_passkey_hash, input_passkey):
        return None
    
    try:
        key = generate_key(input_passkey)
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_text.encode()).decode()
        return decrypted_data
    except InvalidToken:
        return None
    except Exception as e:
        raise EncryptionError(f"Failed to decrypt data: {str(e)}")

def load_data() -> Dict[str, Any]:
    """Load stored data from JSON file."""
    data_file = Path(config.DATA_FILE)
    try:
        if not data_file.exists():
            return {}
        with open(data_file, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If file is corrupted, backup and return empty dict
        if data_file.exists():
            data_file.rename(data_file.with_suffix('.json.bak'))
        return {}

def save_data(data: Dict[str, Any]) -> None:
    """Save data to JSON file with error handling."""
    try:
        with open(config.DATA_FILE, 'w') as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        raise EncryptionError(f"Failed to save data: {str(e)}")
