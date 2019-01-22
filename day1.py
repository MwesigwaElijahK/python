x = int(input("year of birth"))

age = 2019 - x
print(age)

if age <= 18:
    print("minor")
elif age < 36:
    print("youth")
else:
    print("elder")