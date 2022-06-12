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

Days_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

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

days_weeks = "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
print(days_weeks)
days_weeks = days_weeks[0],"No work", days_weeks[2]
print(days_weeks)
