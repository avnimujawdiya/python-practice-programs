def is_vowel(s):
    count = 0
    for char in s:
        if char.lower()in "aeiou":
            count+=1
    return count
s = input("Enter string: ")
print("Number of vowels: ",is_vowel(s))