from sage.crypto.util import ascii_to_bin
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Convert the flag to binary
FLAG = "flag{debug_flag}"
m = int(str(ascii_to_bin(FLAG)), 2)

# Generate a 512-bit RSA key pair
p = random_prime((2^512)-1, False, 2^(512-1))
q = random_prime((2^512)-1, False, 2^(512-1))
n = pq
e = 65537
d = inverse_mod(e, (p-1)(q-1))

# Encrypt the message using RSA-OAEP encryption with AES-128-CBC
sym_key = get_random_bytes(16)
iv = get_random_bytes(AES.block_size)
cipher = AES.new(sym_key, AES.MODE_CBC, iv)
padded_message = pad(str(m).encode(), AES.block_size)
encrypted_message = cipher.encrypt(padded_message)
oaep_msg = bytes([0]) + get_random_bytes(15) + encrypted_message
c = pow(bytes_to_long(oaep_msg), e, n)

print(f"{n = }")
print(f"{e = }")
print(f"{sym_key = }")
print(f"{iv = }")
print(f"{c = }")

# Decrypt the ciphertext using RSA-OAEP decryption with AES-128-CBC
oaep_msg_decrypted = pow(c, d, n)
oaep_msg_decrypted_bytes = long_to_bytes(oaep_msg_decrypted)
if oaep_msg_decrypted_bytes[0] != 0:
    print("Error: OAEP decryption failed")
    exit()
iv_decrypted = oaep_msg_decrypted_bytes[1:AES.block_size+1]
encrypted_message_decrypted = oaep_msg_decrypted_bytes[AES.block_size+1:]
cipher_decrypted = AES.new(sym_key, AES.MODE_CBC, iv_decrypted)
padded_message_decrypted = cipher_decrypted.decrypt(encrypted_message_decrypted)
m_decrypted = int(unpad(padded_message_decrypted, AES.block_size).decode())
flag_decrypted = bin_to_ascii(str(m_decrypted))

print(f"{flag_decrypted = }")
