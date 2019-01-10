# Create a tuple named zoo that contains your favorite animals.
zoo = tuple(("orca", "red panda", "bengal tiger"))

# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index("orca")) # PRINT RESULT: 0

# Determine if an animal is in your tuple by using value in tuple.
if "red panda" in zoo:
  print("animal exists") # PRINT RESULT: animal exists

# Create a variable for each of the animals in your tuple with this cool feature of Python.
(orca, red_panda, bengal_tiger) = zoo
print(orca) # PRINT RESULT: orca
print(red_panda) # PRINT RESULT: red panda
print(bengal_tiger) # PRINT RESULT: bengal tiger

# Convert your tuple into a list.
zoo = list(zoo)

# Use extend() to add three more animals to your zoo.
zoo.extend(["bald eagle", "cat", "sailfish"])

# Convert the list back into a tuple.
zoo = tuple(zoo)
print(zoo) # PRINT RESULT: ('orca', 'red panda', 'bengal tiger', 'bald eagle', 'cat', 'sailfish')