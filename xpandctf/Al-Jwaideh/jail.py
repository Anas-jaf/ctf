#!/usr/bin/python3
BLACK_LIST=['os', 'sh', 'bin', 'pty', 'eval', 'popen', 'echo', '\\x', '%', 'builtins', 'input', 'getattr', "\\", 'subprocess', '+', 'chr', 'import', '|', ':', 'system', 'ls', 'cat', 'flag.txt', 'print']

user_input=input("Go ahead, enter your payload -> ")

def check(strings_array,text):

    return any(string in text for string in strings_array)

try:

    if check(BLACK_LIST,user_input):
        print("BLACK LISTED!")
    else:
        print ("Good")
        exec(user_input)
        
        
except Exception as e:  
    print("Well that's not right")
    print(str(e))   
