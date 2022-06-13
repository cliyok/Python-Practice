name = input("What is your name: ")
greetings = input("Please input your greetings: ")
age = input("Please type in your age: ")

print(greetings + name)
# creates a space between the two variables
print(greetings + " " + name)
Books_by_order = "Atomic Habits\nThe Intelligent investor\nPsychology of money"
print(Books_by_order)
Ordered_Books = "Atomic Habits\tThe Intelligent investor\tPsychology of money"
print(Books_by_order)
print(name + "said,'we should improve our python programming'")
print(name + "said,\"we should improve our python programming\"")
favorite_books =""" Atomic Habits
The Intelligent investor
Psychology of money"""
print(favorite_books)
print(name + """said,"we should improve our python programming" """)

for ball in range(8, 30):
    print(ball)
parrot = "Kenyan Blue"
print(parrot[1])
print(parrot[0])
print(parrot[1:9])
print(parrot[:7])
print(parrot[4:])
print(parrot[1:10:3])

pain = "Headache"
print("ache" in pain)
print("{} age is {}".format(name, age))
for books in range(3, 100, 3):
    print("{} books {:3} has {:4} pages which will take {:4}days to complete".format(name, books, books ** 4, books * 5))

print("Pi is {0:13} ".format(22/7))
print("Pi is {:13.50} ".format(22/7))
