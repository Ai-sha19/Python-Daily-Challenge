"""
Day 3 :Daily Python Challenge
Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 🔢💡

Example:
Input: 7
Output: Yes, it's a prime number!
Input: 10
Output: No, it's not a prime number!

Submit your solution before midnight!
Form Link: https://forms.gle/1nVhXy8rtjqRnuWFA

Hint:
1️⃣ Prime Number wo hota hai jo sirf 1 aur apne aap se divisible ho.
2️⃣ Tum loops (for/while) aur modulus operator (%) ka use kar sakte ho.
3️⃣ Edge Cases: 1 aur negative numbers prime nahi hote!

"""


num = int(input("Enter a number: "))  # User se number lena

if num < 2:  # 1 ya negative numbers prime nahi hote
    print("No, it's not a prime number!")
else:
    is_prime = True  # Assume karte hain ke number prime hai
    for i in range(2, num):  # 2 se lekar (num-1) tak check karenge
        if num % i == 0:  # Agar num kisi number se divisible hai
            is_prime = False  # Toh prime nahi hai
            break  # Loop ko yahin rok dete hain
    if is_prime:
        print("Yes, it's a prime number!")
    else:
        print("No, it's not a prime number!")
