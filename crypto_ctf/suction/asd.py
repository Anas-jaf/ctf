#!/usr/bin/env python3

from Crypto.Util.number import *
# from flag import flag

def keygen(nbit, r):
	while True:
		p, q = [getPrime(nbit) for _ in '__']
		e, n = getPrime(16), p * q
		phi = (p - 1) * (q - 1)
		if GCD(e, phi) == 1:
			N = bin(n)[2:-r]
			E = bin(e)[2:-r]
			PKEY = N + E
			pkey = (n, e)
			return PKEY, pkey

def encrypt(msg, pkey, r):
	m = bytes_to_long(msg)
	n, e = pkey
	c = pow(m, e, n)
	C = bin(c)[2:-r]
	return C

flag = "CCTF{12345678}"
r, nbit = 8, 128
PKEY, pkey = keygen(nbit, r)
# PKEY = 55208723145458976481271800608918815438075571763947979755496510859604544396672
print(f'PKEY = {int(PKEY, 2)}')
FLAG = flag.lstrip('CCTF{').rstrip('}').encode()
enc = encrypt(FLAG, pkey, r)
print(f'enc = {int(enc, 2)}')

r = 8
nbit = 10

int(keygen(nbit, r)[0],2)

# while True: 
#     nbit += 1
#     PKEY = int(keygen(nbit, r)[0],2)
#     if PKEY == 55208723145458976481271800608918815438075571763947979755496510859604544396672 :
#         print ("the prime number is {0}".format(PKEY))
#         break
#     else: 
#         print(PKEY , '\n', nbit)
    