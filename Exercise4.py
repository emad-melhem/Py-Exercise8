def is_vowel(letter):
    vowel_lst = 'aeiou'
    return letter.lower() in vowel_lst

text = input("Enter a text : ")
vowel_num = 0
consonants_num = 0
for letter in text:
    if is_vowel(letter):
        vowel_num += 1
    elif letter.isalpha():
        consonants_num += 1
print(f"The number of vowels = {vowel_num}\n"+
      f"The number of consonants = {consonants_num}")