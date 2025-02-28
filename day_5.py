"""
Day 5 : Daily Python Challenge
Challenge:
Aisa Python program likhna hai jo user se ek number lega aur uska sum calculate karega 1 se lekar us number tak. 🔢💡

Example:
Input: 5
Output: Sum: 15 (kyunki 1 + 2 + 3 + 4 + 5 = 15)

Hint:
1. sum = n * (n + 1) / 2 ye ek shortcut formula hai jo direct sum de sakta hai.
2. Loop use kar ke bhi solve kar sakte ho (for ya while loop).
3. Agar recursion use karna chahtay ho to function ke andar function call karna hoga!

"""
n = int(input("Enter a number: "))
sum_result = n * (n + 1) //2
print("Sum: ", sum_result)

# // ka use isliye kiya gaya taake output pure integer aaye, / k use output float mai ata.
