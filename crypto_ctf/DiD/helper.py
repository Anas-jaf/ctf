#!/usr/bin/env python3

from random import randint
import sys
# from flag import flag
flag =555555

def die(*args):
	PRINT(*args)
	quit()

def PRINT(*args):
	s = " ".join(map(str, args))
	sys.stdout.write(s + "\n")
	sys.stdout.flush()

def user_input():
	return sys.stdin.buffer.readline()

def did(n, l, K, A):
	A, K = set(A), set(K)
	R = [pow(_, 2, n) + randint(0, 1) for _ in A - K]
	return R

def main():
	border = "+"
	PRINT(border*72)
	PRINT(border, ".::   Hi all, she DID it, you should do it too! Are you ready? ::.  ", border)
	PRINT(border*72)

	_flag = False
	n, l = 127, 20
	N = set(list(range(0, n)))
	K = [randint(0, n-1) for _ in range(l)]
	counter, STEP = 0, 2 * n // l - 1
 
	print(K , len(set(K)))

 
	while True:
		answer = user_input().decode().strip()
		try:
			answer_list = [int(_) for _  in answer.split(',')]
			if len(answer_list) <= l and set(answer_list).issubset(N):
				DID = did(n, l, K, answer_list)
				PRINT(border, f'DID = {DID}' , len(DID))
				if set(answer_list) == set(K):
					_flag = True
			else:
				die(border, 'Exception! Bye!!')
		except:
			die(border, 'Your input is not valid! Bye!!')
		if _flag:
			die(border, f'Congrats! the flag: {flag}')
		if counter > STEP:
			die(border, f'Too many tries, bye!')
		counter += 1

if __name__ == '__main__':
	main()
 
 