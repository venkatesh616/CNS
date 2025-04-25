# Encryption function
def encrypt(message, key):
    ciphertext = ''
    for char in message:
        if 'A' <= char <= 'Z':
            ciphertext += chr((ord(char) - 65 + key) % 26 + 65)
        elif 'a' <= char <= 'z':
            ciphertext += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

# Decryption function
def decrypt(ciphertext, key):
    message = ''
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            message += chr((ord(char) - 65 - key) % 26 + 65)
        elif 'a' <= char <= 'z':
            message += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            message += char
    return message

# Frequency analyzer
def frequency_analysis(text):
    freq = {}
    for char in text:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            ch = char.lower()
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq

# === Demo ===
message = "Hello World, Caesar Cipher!"
key = 3

# Encrypt
cipher = encrypt(message, key)
print("Encrypted:", cipher)

# Frequency analysis of ciphertext
print("Ciphertext letter frequency:")
cipher_freq = frequency_analysis(cipher)
for k in sorted(cipher_freq):
    print(f"{k}: {cipher_freq[k]}")

# Decrypt
decrypted = decrypt(cipher, key)
print("\nDecrypted:", decrypted)

# Frequency analysis of decrypted text
print("Decrypted text letter frequency:")
decrypted_freq = frequency_analysis(decrypted)
for k in sorted(decrypted_freq):
    print(f"{k}: {decrypted_freq[k]}")
