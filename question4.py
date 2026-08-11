text = (input("Enter Text: "))
upper_case = 0
lower_case = 0
digits = 0
spaces = 0
others = 0
for char in text:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1
print("Upper Case: ",upper_case)
print("Lower Case: ",lower_case)
print("Digits: ",digits)
print("Spaces: ",spaces)
print("Others: ",others)


