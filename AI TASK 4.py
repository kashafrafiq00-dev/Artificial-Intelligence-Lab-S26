# LUHN Algorithm

def luhn_check(card_number):
    
    digits = [int(d) for d in str(card_number)]
    
    digits.reverse()
    
    total = 0
    
    for i in range(len(digits)):
        
        if i % 2 == 1:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]
    
    if total % 10 == 0:
        return "Valid Card Number"
    else:
        return "Invalid Card Number"


number = input("Enter card number: ")
print(luhn_check(number))

# Remove Punctuations

import string

text = input("Enter a sentence: ")

result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print("Sentence without punctuation:")
print(result)

# Sort Sentence Alphabetically

sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

print("Sentence in alphabetical order:")

for word in words:
    print(word)