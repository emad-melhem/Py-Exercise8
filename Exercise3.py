   # Exercise 3.1
def indexOf_letter(letter):
    letter = str(letter)
    letters = []  
    for i in range(97, 123):  
        letters.append(chr(i))
    if letter.lower() in letters:
        return letters.index(letter.lower()) + 1
    else:
        return -1

print(indexOf_letter('a'))
print(indexOf_letter('G'))
print(indexOf_letter('z'))

   # Exercise 3.2
def is_pangram(text):
    letters = []  
    for i in range(97, 123):  
        letters.append(chr(i))
    for letter in text:
        if letter.lower() in letters:
            letters.remove(letter)
    return len(letters) == 0

print(is_pangram('abcdefghijklmnopqrstuvwxyz'))