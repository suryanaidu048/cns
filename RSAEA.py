import random
from sympy import isprime

# Generate prime numbers
def generate_prime(bits=8):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# Extended Euclidean Algorithm to find the modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Modular inverse
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

# RSA Key Generation
def generate_rsa_keys(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) == 1
    e = random.randint(2, phi - 1)
    while extended_gcd(e, phi)[0] != 1:
        e = random.randint(2, phi - 1)
    
    # Compute d such that d * e ≡ 1 (mod phi)
    d = mod_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# RSA Encryption
def encrypt(plain_text, public_key):
    e, n = public_key
    # Convert each character to its corresponding integer representation
    cipher_text = [pow(ord(char), e, n) for char in plain_text]
    return cipher_text

# RSA Decryption
def decrypt(cipher_text, private_key):
    d, n = private_key
    # Decrypt each character using the private key
    plain_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return plain_text

# Example Usage
if __name__ == "__main__":
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys(bits=8)
    print("Public Key:", public_key)
    print("Private Key:", private_key)
    
    message = "Hello"
    print("Original Message:", message)
    
    # Encrypt the message
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)
