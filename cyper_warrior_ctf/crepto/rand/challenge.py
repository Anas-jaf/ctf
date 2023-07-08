import random

seed = random.randint(1,255)

random.seed(seed)
flag="FLAGK{fake_flag}"

print(flag)
print(f"The length is : {len(flag)}")


_ord = []
for i in range(len(flag)):
	_ord.append(i)

random.shuffle(_ord)

t=[]
enc = []
for i in flag:
	t.append(ord(i))

for i in t:
	number = random.randint(1,30)
	enc.append(i^number)

final = []
for i in _ord:
	final.append(enc[i])

print(final)
# def decode(length, final, seed):
#     random.seed(seed)

#     _ord = []
#     for i in range(length):
#         _ord.append(i)

#     random.shuffle(_ord)

#     dec = []
#     for i in _ord:
#         dec.append(final[i])

#     flag = ""
#     for i in dec:
#         number = random.randint(1, 30)
#         flag += chr(i ^ number)

#     return flag

# # Given input values
# length = 44
# final = [125, 112, 121, 120, 127, 114, 86, 73, 96, 119, 113, 116, 104, 111, 110, 69, 109, 97, 77, 116, 102, 102, 119, 70, 98, 99, 108, 120, 88, 69, 116, 106, 107, 117, 121, 101, 98, 126, 75, 88, 118, 87, 99, 112]

# # Iterate over seed values from 1 to 255
# for seed in range(1, 256):
#     decoded_flag = decode(length, final, seed)
#     print("Seed:", seed, "Decoded flag:", decoded_flag)
    


# final = [125, 112, 121, 120, 127, 114, 86, 73, 96, 119, 113, 116, 104, 111, 110, 69, 109, 97, 77, 116, 102, 102, 119, 70, 98, 99, 108, 120, 88, 69, 116, 106, 107, 117, 121, 101, 98, 126, 75, 88, 118, 87, 99, 112]
# length = 44