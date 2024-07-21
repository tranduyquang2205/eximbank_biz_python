from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64

def Ht(e, t):
    # Load the public key
    public_key = serialization.load_pem_public_key(
        f"-----BEGIN PUBLIC KEY-----\n{t}\n-----END PUBLIC KEY-----".encode()
    )
    
    # Encrypt the message
    encrypted = public_key.encrypt(
        e.encode('utf-8'),  # Convert the string to bytes
        padding.PKCS1v15()
    )
    
    # Return the base64 encoded encrypted message
    return base64.b64encode(encrypted).decode('utf-8')

# Example usage
e = "121650448"
t = "Khanh675@"
encrypted_message = Ht(e, t)
print(encrypted_message)
