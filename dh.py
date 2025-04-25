def power(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

# Commonly agreed public values
p = 23  # Prime number
g = 5   # Primitive root

# Alice's secret
a = 6
A = power(g, a, p)

# Bob's secret
b = 15
B = power(g, b, p)

# Shared secret computation
shared_A = power(B, a, p)
shared_B = power(A, b, p)

print("Alice sends:", A)
print("Bob sends:", B)
print("Shared key at Alice:", shared_A)
print("Shared key at Bob:", shared_B)

# Eve intercepts and replaces keys
# Alice → Eve → Bob

# Eve picks her own secrets
e1 = 13
e2 = 7

# Fake keys sent to both
fake_A = power(g, e1, p)  # Eve sends to Bob
fake_B = power(g, e2, p)  # Eve sends to Alice

# Eve computes both shared secrets
eve_with_alice = power(A, e2, p)
eve_with_bob = power(B, e1, p)

# Alice and Bob compute wrong keys (with Eve's keys)
alice_thinks = power(fake_B, a, p)
bob_thinks = power(fake_A, b, p)

print("\n--- MitM Attack ---")
print("Eve shares with Alice:", eve_with_alice)
print("Eve shares with Bob:", eve_with_bob)
print("Alice computes:", alice_thinks)
print("Bob computes:", bob_thinks)
