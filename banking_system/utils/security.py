import hashlib

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(entered_password, stored_hash):
    """Verifies an entered password against a stored hash."""
    return hash_password(entered_password) == stored_hash
