
# String Utilities Project

# Function to count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


# Function to reverse a string
def reverse(s):
    return s[::-1]


# Function to check palindrome
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# Main program
print("===== STRING UTILITIES =====")

text = input("Enter a string: ")

print("Number of vowels:", count_vowels(text))
print("Reversed string:", reverse(text))

if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
