#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# f = open("./Input/Letters/starting_letter.txt")
# print(f.readlines())

f = open("./Input/Names/invited_names.txt", "r")
# print(f.readlines())

for word in f:
    name = word.strip('\n')
    letter = open("./Input/Letters/starting_letter.txt")
    new_letter = letter.replace("[name]", name)
    


