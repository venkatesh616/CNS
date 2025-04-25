def euclidean_algorithm(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a, b):
    s1, s2, t1, t2 = 1, 0, 0, 1
    while b > 0:
        q = a // b
        a, b = b, a % b
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
    return a, s1, t1  # GCD, x (s1), y (t1)

a, b = 56, 28
gcd = euclidean_algorithm(a, b)
gcd_ext, x, y = extended_euclidean_algorithm(a, b)

print(f"GCD of {a} and {b} is {gcd}")
print(f"Extended Euclidean Algorithm results: GCD = {gcd_ext}, x = {x}, y = {y}")