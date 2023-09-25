# list = [] 
# If you require a collection that's going to have more than one of the same value e.g. 1, 1, 1 then you should use a list 

xmas = [25, 25, 25, True, "kenturkey", 3.5]

food = xmas[4:5] 

print(food)

turkeyAge = xmas[4:]

print(turkeyAge)

food.append("hulahoops")

print(food)

# set = {} or set()
# If you need to maintain an unordered collection of only unique items, then use a set
#  You can't use indexing cause they reorder themselves

setExample = {1, 1, 0, "howdy", 3.5, True, False}

print(setExample) # True and False won't print because they are classified as 1 and 0

setExample2 = {1, 1, 2, "howdy", 3.5, True, False}

print(setExample2) # False prints cause I got rid of the int 0

# Dictionary = {} this creates an empty dictionary, so that's why an empty set needs to be created using its inbuilt function

foodScores = {"chocolate": 10, "chicken breast": 7, "grilled chicken thighs": 10, "plazma": 100}

print(foodScores)
print(foodScores.keys()) # This works but it's a bit ugly

for keys, values in foodScores.items():
    print(keys)
    print(values)


# tuple = ()
# Indexing will work 
# Tuples are immutable 
# For some reason, you can make a tuple without adding the brackets e.g. tuple1 = 1, 2, 3

tuple1 = (1, 2, 3, 4, 4, 4)

tuple2 = tuple1, 5, 5

print(tuple1)
print(tuple2)
print(len(tuple2))