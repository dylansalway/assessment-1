import math
import sympy as sp
import tkinter as tk
import random

def question1(num):
    if num > 0 and num <= 100:
        return (num + 1) % 6 == 0
    else:
        return False

# Example function call
print(question1(9))  # Output: True

def question2(x):
    # Ensure the denominator is not zero
    if x != 7/3:
        return (math.sqrt(x) + 3 * x**5) / (3 * x - 7)
    else:
        print("The value of x makes the denominator zero. Function is undefined.")
        return None

# Example function call
result = question2(5)
print("Result:", result)

def question3(a, b, c, d):
    # Define the variable and function
    x = sp.Symbol('x')
    f = a * sp.sin(b * x * c) + c * sp.exp(d * x)
    
    # Calculate f(5)
    f_at_5 = f.subs(x, 5)
    
    # Calculate the third derivative of f(x) with respect to x
    third_derivative = sp.diff(f, x, 3)
    
    # Calculate the integral of f(x) from 2pi to sqrt(6)
    integral_result = sp.integrate(f, (x, 2 * sp.pi, sp.sqrt(6)))
    
    return [f_at_5, third_derivative, integral_result]

# Example function call
result = question3(1, 2, 3, 4)
print("Results:", result)

def question4():
    game = GuessingGame()
    game.mainloop()

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guessing Game")
        self.geometry("300x150")
        self.random_number = random.randint(0, 100)
        self.guess_count = 0
        
        self.label = tk.Label(self, text="Guess the number (0-100):")
        self.label.pack()
        
        self.entry = tk.Entry(self)
        self.entry.pack()
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        
        self.button = tk.Button(self, text="Submit Guess", command=self.check_guess)
        self.button.pack()
        
    def check_guess(self):
        guess = int(self.entry.get())
        self.guess_count += 1
        
        if guess == self.random_number:
            self.result_label.config(text="Congratulations! You guessed it right.")
            self.button.config(state=tk.DISABLED)
        elif guess < self.random_number:
            self.result_label.config(text=f"Guess {self.guess_count}: {guess} is too low.")
        else:
            self.result_label.config(text=f"Guess {self.guess_count}: {guess} is too high.")
        
        if self.guess_count == 6 and guess != self.random_number:
            self.result_label.config(text=f"Sorry! You've used all your guesses. The number was {self.random_number}.")
            self.button.config(state=tk.DISABLED)

# Call the function to start the game
question4()
