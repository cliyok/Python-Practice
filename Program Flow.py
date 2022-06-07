from _ast import Break

name = input("Please enter your name ")
age = int(input("What is your age {}? ".format(name)))

if 21 >= age <= 65:  # ages between 21 and 65 are not included in the associate ranks
    print("You are welcome to join the associate rank")
else:  # ages
    print("You are considered an elite member of the society")
if age >= 18:
    print("You are welcome to join the brotherhood of the secret society")
    print("Remember to follow the rules of the secret society")
else:
    print("You have {} years to join the brotherhood of the secret society".format(18 - age))
    print("You are welcome to read about the brotherhood")
# In Python true is 1 and false is zero and in conditions any non zero or non-empty values evaluate to true


# for loops
number_characters = input("Please enter the number/ numbers or character/ characters of your choice ")
cleaned_number_characters = " "
Cleaned_number_characters = " "
for typed in range(0, len(number_characters)):
    if number_characters[typed] in name:
        cleaned_number_characters += number_characters[typed]
new_number_characters = cleaned_number_characters  # this prevents the loop from repeating , making it perfom once through the loop
print(new_number_characters)

for char in number_characters:
    if char in name:
        Cleaned_number_characters += char
print(Cleaned_number_characters)

# Continue & Break

Movies = ["Spiderman", "Watchdogs", "Zombie Apocalypse", "Escape", "Wanted"]
for movie in Movies:
    if movie == "Watchdogs":
        continue
    print("I need to watch {} in the theaters".format(movie))
Watched_movie = " "
movie = " "
for movie in Movies:
    if movie == "Watchdogs":
        Watched_movie = movie
        break
else:
    print(" I will buy a tickets for {}".format(Movies))

if Watched_movie == "Watchdogs":
    print("I have watched {}".format(movie))
input_o = 'Please type in your IP_address, An IP_address contains 4 numbers, separated' \
          ' from each other with a fullstop'
IP_address = input("Please type in your IP_address, An IP_address contains 4 numbers,"
                   " separated from each other with a fullstop: ")
if IP_address[-1] != ".":
    IP_address += "."

print(len(IP_address))

segments = 1
length = 0
character = " "

for character in IP_address:
    if character ==".":
        print("segment {} contains {} characters".format(segments, length))
        segments += 1
        length = 0
    else:
        length += 1
if character != ".":
    print("segment {} contains {} characters".format(segments, length))
if IP_address == " ":
    print("Invalid IP address")