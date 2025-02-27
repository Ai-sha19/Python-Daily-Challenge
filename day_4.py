"""

Day 4 : Daily Python Challenge
Challenge:Write a Python program that converts numbers into words!

Example:
Input: 123
Output: "One Hundred Twenty-Three"

Input: 5067
Output: "Five Thousand Sixty-Seven"

"""

from num2words import num2words

num = int(input("Enter a number: "))
words = num2words(num)
print(words.capitalize())