import base64

base64str = "bDNhcm5fdGgzX3IwcDM1"
decode = base64.b64decode(base64str).decode('utf-8')
print(decode)