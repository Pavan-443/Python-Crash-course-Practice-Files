file_location = 'textfiles/learning_python.txt'
with open(file_location) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.strip()
    line.replace('python', 'c')
    print(line)