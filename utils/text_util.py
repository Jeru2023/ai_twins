import hashlib


def generate_unique_id(text):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Convert the text to bytes and hash it
    sha256_hash.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    unique_id = sha256_hash.hexdigest()

    return unique_id
