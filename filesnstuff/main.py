

#This is a bit spooky as if you dont close the file it will automaticaly close sometime in the future, but you dont know when.
file = open('my_file.txt')
content = file.read()
print(content)
file.close()
#This method only uses the file within the 'with' part, once exited the file is closed.
with open('my_file.txt') as file:
    content = file.read()
    print(content)

with open('my_file.txt', mode='a') as file:
    content = file.write('BANANA')
    print(content)