word = input("Give me a word: ")
counter = 0

for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        counter = counter + 1
print(counter)
