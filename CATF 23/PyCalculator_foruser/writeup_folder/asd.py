from pwn import *

payload = '''
dir(path)
'''

l = listen()
r = remote('20.121.4.239', 30120)
print(r.recvuntil('Welcome'))

# print(f'got{r.recv()}')

# r.interactive()