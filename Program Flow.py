name = input("Please enter your name ")
age = int(input("What is your age {}?".format(name)))

if 21>=age<=65:#ages between 21 and 65 are not included in the associate ranks
    print("You are welcome to join the associate rank")
else:#ages
    print("You are considered an elite member of the society")
if age >= 18:
    print("You are welcome to join the brotherhood of the secret society")
    print("Remember to follow the rules of the secret society")
else:
    print("You have {} years to join the brotherhood of the secret society".format(18-age))
    print("You are welcome to read about the brotherhood")
#in Python true is 1 and false is zero and in conditions any non zero or non-empty values evaluate to true


# for loops
number_characters = input("Please enter the number/ numbers or character/ characters of your choice ")
cleaned_number_characters = " "
for typed in range(0, len(number_characters))
    if number_characters[typed] in name:
        cleaned_number_characters += number_characters[typed]
new_number_characters = cleaned_number_characters# this prevents the loop from repeating , making it perfom once through the loop
print(new_number_characters)

for char in number_characters:
    if char in name:
        cleaned_number_characters+=char
print(cleaned_number_characters)
