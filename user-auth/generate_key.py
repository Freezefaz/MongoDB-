import os
import binascii

# to create a secret key
# IGNORE the quotes and b
print(binascii.hexlify(os.urandom(24)))