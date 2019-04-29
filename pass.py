import pyperclip
import secrets
import sys

n = 16
if len(sys.argv) > 1:
    n = int(sys.argv[1])
password = ''.join(chr(secrets.randbelow(94) + 33) for i in range(n))
print(password)
pyperclip.copy(password)