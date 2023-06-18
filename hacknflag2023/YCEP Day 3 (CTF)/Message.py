import base64

def xor_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % key_length]))
    return encrypted_text

def reverse_string(text):
    return text[::-1]

# Encrypt the string with Base32
encrypted_text = base64.b32encode(text.encode()).decode()

# Reverse the encrypted string
reversed_text = reverse_string(encrypted_text)

# Define the XOR key
xor_key = "iliketoxor"

# Perform XOR encryption
encrypted_result = xor_encrypt(reversed_text, xor_key)

print("Encrypted Result:", encrypted_result)
