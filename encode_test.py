import base64

original = "bing.com"
original = original.encode()
coded = str(base64.b64encode(original))

print(type(coded))
print(coded[2:-1])