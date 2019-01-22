x = int(input("enter_numberx"))
y = int(input("enter_numbery"))

results = x + y
answer = f"the result of {x} + {y} is {results}" 
print("the answer is", results)
print(results)

if x < y:
    print("less")
elif x == y:
    print("equal")
else:
    print("greater")

