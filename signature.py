# Basic RSA components
def gcd(a, b): return a if b == 0 else gcd(b, a % b)
def modinv(e, phi):  # Extended Euclidean Algorithm
    d, x1, x2 = 0, 0, 1
    while e: phi, e, x1, x2, d = e, phi % e, x2 - (phi // e) * x1, x1, x1
    return d + phi if d < 0 else d

def gen_keys(p, q):
    n, phi, e = p * q, (p - 1) * (q - 1), 3
    while gcd(e, phi) != 1: e += 2
    return ((e, n), (modinv(e, phi), n))

# Simple hash function
def hash_msg(msg): return sum(ord(c) for c in msg)

# RSA encryption/decryption
def encrypt(msg, key): return pow(msg, key[0], key[1])

# === Demo ===
p, q = 61, 53
pub, priv = gen_keys(p, q)

message = "Hello"
h = hash_msg(message)
signature = encrypt(h, priv)  # Signed by sender

# On receiver's side
verified_hash = encrypt(signature, pub)
print("Message:", message)
print("Signature:", signature)
print("Verified:", verified_hash == hash_msg(message))
