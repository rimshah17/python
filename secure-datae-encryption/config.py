from dataclasses import dataclass, field
from typing import Dict, Any
import streamlit as st

@dataclass
class Config:
    """Application configuration."""
    MAX_ATTEMPTS: int = 3
    LOCKOUT_TIME: int = 30  # seconds
    APP_TITLE: str = "🔒 Secure Data Encryption System"
    DATA_FILE: str = "data.json"
    STYLE: Dict[str, Any] = field(default_factory=lambda: {
        "primary_color": "#FF4B4B",
        "background_color": "#F0F2F6",
        "text_color": "#262730",
        "font": "sans serif"
    })

    @staticmethod
    def get_encryption_key() -> str:
        """Get the encryption key from Streamlit secrets."""
        try:
            return st.secrets.encryption_key
        except (AttributeError, KeyError):
            # Fallback for local development
            return "default-dev-key-replace-in-production"
    
    @staticmethod
    def get_jwt_secret() -> str:
        """Get the JWT secret from Streamlit secrets."""
        try:
            return st.secrets.jwt_secret
        except (AttributeError, KeyError):
            # Fallback for local development
            return "default-jwt-secret-replace-in-production"
    
    @staticmethod
    def get_cookie_name() -> str:
        """Get the cookie name from Streamlit secrets."""
        try:
            return st.secrets.cookie_name
        except (AttributeError, KeyError):
            return "secure_data_cookie"
    
    @staticmethod
    def get_session_expiry() -> int:
        """Get session expiry days from Streamlit secrets."""
        try:
            return int(st.secrets.session_expiry_days)
        except (AttributeError, KeyError):
            return 30

config = Config()
