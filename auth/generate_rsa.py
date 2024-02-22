from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,  # Common key size for RSA
    backend=default_backend()
)

# Extract public key from private key
public_key = private_key.public_key()
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # Or use a supported encryption algorithm
)
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the private key to a file
with open('private_key.pem', 'wb') as f:
    f.write(pem_private_key)

# Save the public key to a file
with open('public_key.pem', 'wb') as f:
    f.write(pem_public_key)

