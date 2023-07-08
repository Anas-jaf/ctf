import os ,sys , glob , tarfile


print("Enter/Paste challenge_readme informations content. Ctrl-D to save it.")
challenge_readme = []
while True:
    try:
        line = input()
    except EOFError:
        break
    challenge_readme.append(line)

challenge_link = input('\n\n\nChallenge tar link :  ')

os.system(f'wget {challenge_link}')

tar_files = glob.glob('.' + '/*.txz')

for tar_path in tar_files:
    folder_name = tar_path.split('_')[0]
    # print (tar)
    
    # Extract the contents of the .txz file
    with tarfile.open(tar_path, 'r:xz') as tar:
        tar.extractall()
        
    # Create the readme file and write the content
    with open(folder_name+'/readme.md', 'w') as file:
        file.write('\n'.join([i for i in challenge_readme]))
    
    os.system(f'rm {tar_path}')
