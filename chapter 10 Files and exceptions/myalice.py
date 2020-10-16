file_location = 'textfiles/alice.txt'
try:
    with open(file_location, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("sorry the file Doesn't Exist!")
else:
    words = content.split()
    num_words = len(words)
    print(f'Given book is having roughly about {num_words} words in it.')
