from _ast import While

tesla = {"make": "sedan",
         "model": "model X",
         "color": ["red","yellow","green","white"],
         "engine size": "3200cc"}
print(tesla)
print(tesla["model"])
tesla["engine type"] = "Hybrid"
print(tesla)

del tesla["make"]
print(tesla)
# tesla.clear() #deletes everything in the dictionary
print(tesla)
for typed in tesla:
    print(tesla[typed])

print(tesla.keys())
print(tesla.values())

while True:
    dict_key = input("Please enter the select one in each model, color, make, engine size, engine type: ")
    if dict_key == "quit":
        break
    # if dict_key in tesla:
    car_make = tesla.get(dict_key, "We do not have " + dict_key)  # the dict_key + " is not acceptable" replaces,
    # if changed indentation is important  the else in line 24
    print(car_make)
    else:
        print("{} is not acceptable".format(dict_key))

# join method

myList = ["a", "b", "c", "d"]
new_string =" "
new_string = ",".join(myList)
print(new_string)
