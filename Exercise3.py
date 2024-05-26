   # Exercise 3.1
def indexOf_letter(letter): #return the index of a letter and return -1 if not in it.
    letters = list(map(chr ,range(97, 123))) # creat list of lower letters.
    if letter.lower() in letters:
        return letters.index(letter.lower()) + 1
    else:
        return -1

print(indexOf_letter('a'))
print(indexOf_letter('G'))
print(indexOf_letter('z'))

   # Exercise 3.2
def is_pangram(text):
    letters = list(map(chr ,range(97, 123))) # creat list of lower letters.
    for letter in text:
        if letter.lower() in letters:
            letters.remove(letter) # remove the same letter from letters to get the letters that are not present in the text.
    return len(letters) == 0 # True if all letters are present in the text.otherwise False

print(is_pangram('abcdefghijklmnopqrstuvwxyz'))