import base64
enc = base64.b64encode("password".encode("utf-8"))
print(enc)
print(base64.b64decode(enc).decode("utf-8"))
