inputString = input("What is input string? ")

while len(inputString) == 0:
    inputString = input("Input string should not be empty. Input your string: ")

charCount = len(inputString)

print(inputString, "has " +  str(charCount) + " characters.")