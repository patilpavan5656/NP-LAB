import math

def power(a, b, P):
    return a ** b % P

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def d_h(P, G):
    a, b = 4, 3

    print("The value of P:", P)
    print("The value of G:", G)
    print("The private key a for Alice:", a)
    x = power(G, a, P)
    print("The private key b for Bob:", b)
    y = power(G, b, P)
    ka = power(y, a, P)
    kb = power(x, b, P)
    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

def rsa(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 7

    while gcd(e, phi) != 1:
        e += 1

    d = pow(e, -1, phi)
    message = 11
    c = pow(message, e, n)
    m = pow(c, d, n)

    print("Original Message =", message)
    print("p =", p)
    print("q =", q)
    print("n = pq =", n)
    print("phi =", phi)
    print("e =", e)
    print("d =", d)
    print("Encrypted message =", c)
    print("Decrypted message =", m)

if __name__ == "__main__":
    p, q = 13, 11
    print("RSA Algorithm:")
    rsa(p, q)

    print("\n\nDiffie Hellman Algorithm..")
    d_h(p, q)