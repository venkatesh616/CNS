def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        q = temp_phi // e
        temp_phi, e = e, temp_phi % e
        x1, x2 = x2 - q * x1, x1
        y1, d = d - q * y1, y1
    return d + phi if d < 0 else d

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0: return False
    return True

def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        return "Both numbers must be prime."
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))  # (public_key, private_key)

def encrypt(message, key):
    e, n = key
    return [pow(ord(char), e, n) for char in message]

def decrypt(cipher, key):
    d, n = key
    return ''.join([chr(pow(char, d, n)) for char in cipher])

# === Demo ===
p, q = 61, 53  # Example small primes
public, private = generate_keys(p, q)

message = "RSA"
cipher = encrypt(message, public)
original = decrypt(cipher, private)

print("Public Key:", public)
print("Private Key:", private)
print("Original:", message)
print("Encrypted:", cipher)
print("Decrypted:", original)
