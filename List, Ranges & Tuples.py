# Lists
Farm_tools = ["Machete", "Jembe", "Rake", "Pan", "Plough"]
Kitchen_utensils = ["Knife", "fork", "spoon", "serving spoon"]

for tools in Farm_tools:
    print("This is the farm tool available at the store " + tools)
print(Farm_tools)

tools = Farm_tools + Kitchen_utensils
print(sorted(tools))
tools.sort()  # the sort method works only on the object that is called upon
print(tools)

Birds = []
Birds.append(["Hen", "Dove", "Eagle", "Vulture", "Turkey", "Geese"])
Birds.append(["Hen", "Dove", "Turkey", "Geese"])
Birds.append(["Eagle", "Vulture"])
Birds.append(["Dove", "Eagle", "Turkey", "Geese"])
Birds.append(["Hen", "Dove", "Vulture", "Turkey", "Geese"])

for specie in Birds:
    if not "Vulture" in Birds:
        print(specie)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
another_even = even
another_even.sort(reverse=True)
print(even)

numbers = even, odd
for numbers_set in numbers:
    print(numbers_set)

for value in iter(even):
    print(value)

for values in iter(even):
    print(values)

Days_list = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday","Sunday"]

my_iterator = iter(Days_list)

for value in range(0, len(Days_list)):
    next_item = next(my_iterator)
    print(next_item)

for i in range(199,1,-2):
    print(i)

for word in Days_list:
    print(word[::-1])

O = range(0, 100, 2)
print(O)
p=O[::5]
print(p)

Days_list[0] = "No work"
print(Days_list)

days_weeks = "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"
print(days_weeks)
days_weeks = days_weeks[0],"No work", days_weeks[2]
print(days_weeks)

Tesla = "model X","Electric", 2018
Toyota = "Toyota Corolla","Diesel", "2020"
Honda = "Honda CRV", "Hybrid", 2021
# unpacking tuples
Model, Type, Year = Tesla
print(Model)
print(Type)
print(Year)
print(Model, Type, Year)

eminem = "The Eminem Show", "Eminem", "2002", (
    (1, "White America"), (2, "Business"), (3,"Cleaning Out My Closet[Explicit]"), (4, "Square Dance"),
    (5, "The Kiss"), (6, "Soldier"), (7, "Say Goodbye Hollywood"), (8, "Drips"), (9, "Without Me"), (10,"Paul Rosenberg"), (11, "Sing for the Moment [Explicit]"),
    (12, "Superman"), (13, "Hallie song"), (14, "Steve Berman(Skit)"), (15, "When Music stops"), (16, "Say What you Say"), (17, "Till I Collapse"), (18, "My Dad's Gone Crazy"), (19, "Curtains Close(skit)"))
Title, Artist, Year, Tracks = eminem
print(Title)
print(Artist)
print(Year)
for song in Tracks:
    track,title = song
    print("\tTrack {}, song: {}".format(track, title))
# Binary data

for numbers in range(256,1000):
    print("{0:>2} in binary is {0:>08b}".format(numbers))
for numerics in range(256,1000):
    print("{0:>2} in hexadecimal is {0:>02x}".format(numerics))
