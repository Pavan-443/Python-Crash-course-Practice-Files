file_location = 'textfiles/alice.txt'

with open(file_location, encoding='utf-8') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += line.lower().count('the ')

print(count)