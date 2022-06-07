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
