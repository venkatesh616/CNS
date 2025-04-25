# Radix-64 character set
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode_radix64(data):
    binary = ''.join([format(ord(c), '08b') for c in data])
    while len(binary) % 6 != 0:
        binary += '0'
    encoded = ''
    for i in range(0, len(binary), 6):
        encoded += chars[int(binary[i:i+6], 2)]
    while len(encoded) % 4 != 0:
        encoded += '='
    return encoded

def decode_radix64(encoded):
    encoded = encoded.rstrip('=')
    binary = ''
    for c in encoded:
        binary += format(chars.index(c), '06b')
    decoded = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            decoded += chr(int(byte, 2))
    return decoded

# Example
text = "Hello!"
encoded = encode_radix64(text)
decoded = decode_radix64(encoded)

print("Original:", text)
print("Encoded:", encoded)
print("Decoded:", decoded)
