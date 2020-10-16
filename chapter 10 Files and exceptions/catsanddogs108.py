file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    try:
        with open(file_name) as f:
            contents = f.read()
            print(contents.strip())
            print('')
    except FileNotFoundError:
        print(f'sorry the file{file_name} is not found!\n')