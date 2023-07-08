file_path = './file2'

import io

# file_path = 'path/to/file.txt'

with io.open(file_path, 'r', encoding='utf-8') as file:
    file_contents = file.read()

print(file_contents)


# with open(file_path, 'r') as file:
#     # file_contents = file.read().replace('\n', '')
#     file_contents = file.read()    

# print(file_contents)
