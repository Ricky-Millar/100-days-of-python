#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_list = []
letter = ''
with open('./input/names/invited_names.txt') as names:
    name_list = names.readlines()

print(name_list)
for name in range(len(name_list)):
    name_list[name] = name_list[name].strip('\n')
    with open('./input/letters/starting_letter.txt') as template:
        letter = template.read()
        letter = letter.replace('[NAME]', name_list[name])
    with open(f'./output/ReadyToSend/{name_list[name]}.txt', mode = 'w') as completed_letter:
        completed_letter.write(letter)


