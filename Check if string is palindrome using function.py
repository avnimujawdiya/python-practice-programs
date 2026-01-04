def is_palindrome(s):
    return s == s[::-1]
s = input("Enter string: ")
print("palindrome" if is_palindrome(s)else "not palindrome")