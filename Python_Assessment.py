
# Q1. Check Even or Odd
num = int(input(" Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q2. Print Grade
marks = int(input(" Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Q3. Positive / Negative / Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q4. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Q5. Multiplication Table
num = int(input(" Enter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Q6. Sum of First N Natural Numbers
n = int(input(" Enter N: "))
sum_ = 0
i = 1
while i <= n:
    sum_ += i
    i += 1
print("Sum:", sum_)

# Q7. Palindrome Check
text = input(" Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Q8. Continue & Break
print(" Printing numbers 1 to 20 (skip 5, stop at 15):")
for i in range(1, 21):
    if i == 5:
        continue
    if i == 15:
        break
    print(i)

# Q9. Math Module
import math
num = int(input(" Enter a number: "))
print("Square Root:", math.sqrt(num))
print("Factorial:", math.factorial(num))

# Q10. Rock-Paper-Scissors Game
import random
print(" Rock-Paper-Scissors Game")
print("Choices: Rock, Paper, Scissors")
user = input("Enter your choice: ").lower()
comp_choice = random.randint(1, 3)
if comp_choice == 1:
    comp = "rock"
elif comp_choice == 2:
    comp = "paper"
else:
    comp = "scissors"
print("Computer chose:", comp)
if user == comp:
    print("It's a Tie!")
elif (user == "rock" and comp == "scissors") or \
     (user == "paper" and comp == "rock") or \
     (user == "scissors" and comp == "paper"):
    print("You Win!")
else:
    print("You Lose!")
