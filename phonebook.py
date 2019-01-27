person = {"name": "Eli", "email": "a@ja.com", "number": 1234567}

all_contacts =[]
all_contacts.append(person)
print(all_contacts)


name = str(input("Enter name:"))
while len(str(name)) > 20 or len(str(name)) < 3 or len(str(name)) == 3:
  name = str(input("Invalid name. Re-enter name(more than 2 letters): "))

email = input("Enter email:")
while "@" not in(email) and "." is not (email):
  email = input("Enter valid email:")

number = int(input("Enter number:"))
while len(str(number)) > 10 or len(str(number)) < 10:
  number = int(input("Invalid number. Re-enter phonenumber(10 digits):"))


new_person = {"name": name, "email": email, "number": number}


all_contacts.append(new_person)
print(all_contacts)





# for x in all_contacts:
#     print(x)

# any(char.isdigit() for char in "tool1")

# x = "t56l1"
# for char in x:
#     print(char.isdigit())
