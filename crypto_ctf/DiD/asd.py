import socket
from random import randint
import subprocess

def brute_force():
    
    # Server information
    server_host = '00.cr.yp.toc.tf'
    server_port = 11337

    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_host, server_port))

    # Receive and print the server banner
    banner = sock.recv(1024).decode()
    # print(banner)


    power_l = {}
    expected_list = []

    for i in range(0,127):
        power_l[i] = (pow(i,2,127))

    while True:
        for set_value in range(0, 127, 20):
            if set_value == 120:
                end_value =127
                numbers = [i for i in range(set_value, end_value)]+[str(i) for i in range(0, 12)]
            else : 
                end_value = set_value + 20 
                numbers = [i for i in range(set_value, end_value)]
            
            for item in numbers:
                for key, value in power_l.items():
                    if set([item]).issubset(numbers) and set([key]).issubset(numbers) and (item == value or item - 1 == value):
                        # print('value OF', item , ' -----> ', key)
                        expected_list.append(key)
            print(banner)
            numbers_str = ','.join([str(i) for i in numbers])
            print(numbers_str)
            sock.send(numbers_str.encode() + b'\n')
            
            # Receive and print the response
            response = sock.recv(1024).decode()
            print(response)
            DID_output = [int(i) for i in response.lstrip('+ DID = [').rstrip(']\n').replace(" ", "").split(',')]
            
            if 'Congrats' in response:
                break
            elif 'Too many tries, bye!' in response:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((server_host, server_port))
                banner = sock.recv(1024).decode()
                print(banner)
                continue            
    
    sock.close()        

def did(n, supposed_list, my_answer):
	my_answer, supposed_list = set(my_answer), set(supposed_list)
	result = [pow(_, 2, n) + randint(0, 1) for _ in my_answer - supposed_list]
	return result


brute_force()