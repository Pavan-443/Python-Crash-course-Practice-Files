file_location = 'textfiles/learning_python.txt'
with open(file_location) as file_object:
    content = file_object.read()
print(content.strip())
print('')
with open(file_location) as file_object2:
    for line in file_object2:
        print(line.strip())
print('')
with open(file_location) as file_object3:
    lines = file_object3.readlines()
for line in lines:
    print(line.strip())