"""
Utility functions for PlanVenture API.
Includes password hashing and validation utilities.
"""

from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def hash_password(password: str) -> str:
    """
    Hash a password using werkzeug's generate_password_hash.
    Uses pbkdf2:sha256 method with a salt.
    
    Args:
        password: Plain text password to hash
        
    Returns:
        Hashed password string
    """
    return generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

def verify_password(password_hash: str, password: str) -> bool:
    """
    Verify a password against its hash.
    
    Args:
        password_hash: The hashed password from database
        password: Plain text password to verify
        
    Returns:
        True if password matches, False otherwise
    """
    return check_password_hash(password_hash, password)

def generate_salt(length: int = 32) -> str:
    """
    Generate a random salt for additional security purposes.
    
    Args:
        length: Length of the salt in bytes (default: 32)
        
    Returns:
        Hex-encoded random salt string
    """
    return secrets.token_hex(length)

def generate_secure_token(length: int = 32) -> str:
    """
    Generate a secure random token for API keys, reset tokens, etc.
    
    Args:
        length: Length of the token in bytes (default: 32)
        
    Returns:
        URL-safe random token string
    """
    return secrets.token_urlsafe(length)
