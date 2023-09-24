# Playing with strings 

def mysteryFunc():
    return "This is a mystery"

print(mysteryFunc())

# print(mysteryFunc([3:4])) 
# Can you use string slicing on a function? Seems like you can't

bestJoke = "Why did the scarecrow get an award?"

bestAnswer = "Because he was out standing in his field"

print(bestJoke[-10:-1])

print(bestJoke + " " + bestAnswer)

print(bestJoke[1:2] + " " + bestAnswer[6:7] + " l l " + bestJoke[19:20])