import hmac
import time
import base64
import json

class JWT():
    def encode(self, username, key, alg='HS256', exp=360):
        header = self.generate_header(alg)
        # copy payload to avoid modification to original payload
        payload = self.encode_payload(exp, username)
        message = header + b"." + payload
        sign = self.generate_encrypt_msg(key.encode(), message, alg)
        part = [message, sign]
        return b".".join(part).decode()

    def decode(self, token, key, alg='HS256'):
        token = token.encode()
        header, payload, req_sign = token.split(b".")
        message = header + b"." + payload
        payload_sign = self.generate_encrypt_msg(key.encode(), message, alg)
        if req_sign != payload_sign:
            raise Exception("invalid token")
        payload_str = self._safe_base64_url_decode(payload)
        payload_json = json.loads(payload_str)
        now = time.time()
        if int(now) > int(payload_json["exp"]):
            raise Exception("token expired")
        return payload_json["user"]

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
    def generate_encrypt_msg(self, key, msg, alg):
        """Use sha256 to encrypt the message
        """
        if alg == "HS256":
            sign = hmac.new(key, msg, digestmod="sha256").digest()
        else:
            raise ValueError("Invalid algorithm")
        return self._safe_base64_url_encode(sign)

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
    user_name = "guozhinuan"
    key = "test"
    s = jwt.encode(user_name, key)
    print(s)
    encode_name = jwt.decode(s, 'test2')
    print(encode_name)
