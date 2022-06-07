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

for ball in range(7, 30):
    print(ball)
parrot = "Kenyan Blue"
print(parrot[0])
print(parrot[-1])
print(parrot[0:9])
print(parrot[:6])
print(parrot[3:])
print(parrot[0:10:3])

pain = "Headache"
print("ache" in pain)
print("{} age is {}".format(name, age))
for books in range(2, 100, 3):
    print("{} books {:2} has {:4} pages which will take {:4}days to complete".format(name, books, books ** 4, books * 5))

print("Pi is {:12} ".format(22/7))
print("Pi is {:12.50} ".format(22/7))
