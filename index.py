# comprehensions
# Here's a list. Let's capitalize every work in it and put those capped words in a new list while we're at it
stuff = ["name", "age", "address", "phone"]

# These three examples do the same thing: loop through the stuff list and make a new list that contains the words capitalized
#1 good old for loop example
cap_stuff = []
for foo in stuff:
  cap_stuff.append(foo.capitalize())

#2 map example
cap_stuff = list(map(lambda foo: foo.capitalize(), stuff))
print(cap_stuff)

# comprehension
cap_stuff = [ foo.capitalize() for foo in stuff ]


# Comprehensions can run on any collection. Here's a dictionary example
profile = {
  "name": "Fred",
  "age": 34,
  "address": "123 Sesame St"
}

# for loop version
profile_strings = []
for key, value in profile.items():
    profile_strings.append(f"The key is {key}. The value is {value}")


# Here, we represent that data from the dict as strings, then add them to a new list
profile_strings = [ f"The key is {key}. The value is {value}" for key, value in profile.items() ]
print(profile_strings)
