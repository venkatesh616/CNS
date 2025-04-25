# Function to create the order of columns based on key
def get_key_order(key):
    key_order = sorted([(char, idx) for idx, char in enumerate(key)])
    return [idx for char, idx in key_order]

# Encryption function
def encrypt(message, key):
    key_len = len(key)
    msg_len = len(message)
    rows = (msg_len + key_len - 1) // key_len  # ceiling division
    padded_len = rows * key_len
    padded_message = message.ljust(padded_len, 'X')  # pad with 'X'
    
    matrix = []
    for r in range(rows):
        row = []
        for c in range(key_len):
            row.append(padded_message[r * key_len + c])
        matrix.append(row)
    
    cipher = ''
    for col in get_key_order(key):
        for row in matrix:
            cipher += row[col]
    return cipher

# Decryption function
def decrypt(cipher, key):
    key_len = len(key)
    msg_len = len(cipher)
    rows = msg_len // key_len
    key_order = get_key_order(key)

    # Create empty matrix
    matrix = [['' for _ in range(key_len)] for _ in range(rows)]
    
    # Fill columns by key order
    index = 0
    for col in key_order:
        for row in range(rows):
            matrix[row][col] = cipher[index]
            index += 1

    # Read message row-wise
    message = ''
    for row in matrix:
        for char in row:
            message += char
    return message

# Frequency analysis
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
message = "meetmeaftertheparty"
key = "CARGO"

# Encrypt
cipher = encrypt(message, key)
print("Encrypted:", cipher)

# Frequency analysis of ciphertext
print("\nCiphertext letter frequency:")
cipher_freq = frequency_analysis(cipher)
for k in sorted(cipher_freq):
    print(f"{k}: {cipher_freq[k]}")

# Decrypt
decrypted = decrypt(cipher, key)
print("\nDecrypted:", decrypted)

# Frequency analysis of decrypted message
print("\nDecrypted message letter frequency:")
decrypted_freq = frequency_analysis(decrypted)
for k in sorted(decrypted_freq):
    print(f"{k}: {decrypted_freq[k]}")
