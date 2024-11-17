def is_palindrome(s):
    return s == s[::-1]
s = input()
print("TRUE" if is_palindrome(s) else "FALSE")
