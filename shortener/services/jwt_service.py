from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import hmac
import time
import base64
import json

class JWT():
    def encode(self, username, private_key_pem, alg='HS256', exp=360):
        header = self.generate_header(alg)
        payload = self.encode_payload(exp, username)
        message = header + b"." + payload
        sign = self.generate_encrypt_msg(private_key_pem, message, alg)
        part = [message, sign]
        return b".".join(part).decode()

    def decode(self, token, key):
        token = token.encode()
        header, payload, req_sign = token.split(b".")
        header_str = self._safe_base64_url_decode(header)
        header_json = json.loads(header_str)
        message = header + b"." + payload
        self.verify_signature(key, message, req_sign, header_json["alg"])
        payload_str = self._safe_base64_url_decode(payload)
        payload_json = json.loads(payload_str)
        now = time.time()
        if int(now) > int(payload_json["exp"]):
            raise Exception("token expired")
        return payload_json["user"]

    def generate_encrypt_msg(self, key_pem, msg, alg):
        if alg == "HS256":
            sign = hmac.new(key_pem.encode(), msg, digestmod="sha256").digest()
        elif alg == "RS256":
            private_key = serialization.load_pem_private_key(key_pem, password=None)
            sign = private_key.sign(
                msg,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        else:
            raise ValueError("Invalid algorithm")
        return self._safe_base64_url_encode(sign)

    def verify_signature(self, key, message, signature, alg):
        if alg == "RS256":
            public_key = serialization.load_pem_public_key(key)
            try:
                public_key.verify(
                    self._safe_base64_url_decode(signature),
                    message,
                    padding.PKCS1v15(),
                    hashes.SHA256()
                )
            except Exception as e:
                raise ValueError("Invalid signature") from e
        elif alg == "HS256":
            key = key.encode()
            msg_sign = hmac.new(key, message, digestmod="sha256").digest()
            if self._safe_base64_url_encode(msg_sign) != signature:
                raise ValueError("Invalid signature")
        else:
            raise ValueError("Invalid algorithm")

    def encode_payload(self, exp, username: str):
        """Add exp to payload and encode it in base64
        """
        exp = time.time() + exp
        payload = """{"exp": "%d","user":"%s"}""" % (exp, username)
        return self._safe_base64_url_encode(payload)
    def generate_header(self, alg):
        """Indicate algorithm and signature type
        """
        header = """{"alg":"%s","typ":"jwt"}""" % (alg)
        return self._safe_base64_url_encode(header)
    # def generate_encrypt_msg(self, key, msg, alg):
    #     """Use sha256 to encrypt the message
    #     """
    #     if alg == "HS256":
    #         sign = hmac.new(key, msg, digestmod="sha256").digest()
    #     else:
    #         raise ValueError("Invalid algorithm")
    #     return self._safe_base64_url_encode(sign)

    def _safe_base64_url_encode(self, input):
        """Using Base64 encode the  input and return the result with ambiguity
        """
        if isinstance(input, str):
            input = input.encode()
        elif isinstance(input, bytes):
            pass
        else:
            raise TypeError("Unsupported input type")
        input_b64 = base64.urlsafe_b64encode(input)
        # replace = to avoid ambiguity
        return input_b64.replace(b"=", b"")

    def _safe_base64_url_decode(self, input):
        # retrieve the '=' that was replaced in _safe_base64_url_encode
        remain = len(input) % 4
        if remain > 0:
            input += b"=" * (4 - remain)
        return base64.urlsafe_b64decode(input)


jwt = JWT()

if __name__ == "__main__":
    username = "guozhinuan"

    # Load the private key from a PEM file
    with open("../private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,  # Use actual password if your key is encrypted
        )
    with open("../public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
        )

    # Convert private key to PEM format (bytes)
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Encode the JWT
    encoded_jwt = jwt.encode(username, private_key_pem, alg='RS256')
    print(encoded_jwt)
    # Convert public key to PEM format (bytes)
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Decode the JWT
    # Note: `encoded_jwt` is the JWT token you received
    try:
        decoded_username = jwt.decode(encoded_jwt, public_key_pem)
        print(decoded_username)
    except Exception as e:
        print(f"Error decoding JWT: {e}")

    encode_test = jwt.encode(username, "ppp", "HS256")
    print(encode_test)
    decode_test = jwt.decode(encode_test, "ppp")
    print(decode_test)
