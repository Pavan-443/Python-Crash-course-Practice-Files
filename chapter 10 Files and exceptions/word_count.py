def count_words(file_location):
    """count the Approximate no.of words in a utf-8 text file"""
    try:
        with open(file_location, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"sorry the file Doesn't Exist! at the location {file_location}")
    except UnicodeDecodeError:
        print('Only UTF-8 files Please...')
    else:
        words = content.split()
        num_words = len(words)
        print(f'Given book is having roughly about {num_words} words in it\n')


file_locations = []

try:
    file_count = int(input('About How many files you want to know words in them: '))
except ValueError:
    print('Please enter a Valid input!')
else:
    for num in range(1,file_count+1):
        file = input('Please enter the location of file: ')
        file_locations.append(file)

for file_location in file_locations:
    count_words(file_location)

