"""
Day 2 : Daily Python Challenge

Challenge: Aisa Python program likhna hai jo user se ek sentence le aur usme jitne words hain, count kare!

Example:  
Input: "Python is amazing!"  
Output: Total words: 3  

Hint: 
- split() function ka use karke sentence ko words me tod sakte ho.  
- len() function se words ki total count nikal sakte ho.

"""

sentence = input("Enter a Sentence: ") #Aisha Iqbal

# separate words
words = sentence.split()
print(words) #['Aisha', 'Iqbal']

# count words
total_words = len(words)
print(f"Total Words: {total_words}") #2

# reversed words
reversed_word = " ".join(words[::-1])
reversed_word1 = " ".join(reversed(words))

print(reversed_word)
print(reversed_word1)
