import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.word_to_guess = choose_word()
        self.max_attempts = 6
        self.guessed_letters = []

        self.word_display = tk.StringVar()
        self.word_display.set(display_word(self.word_to_guess, self.guessed_letters))

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, textvariable=self.word_display, font=("Arial", 16))
        self.word_label.pack(pady=20)

        self.guess_entry = tk.Entry(self.master, font=("Arial", 14))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, font=("Arial", 14))
        self.guess_button.pack(pady=10)

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showwarning("Repeated Guess", "You already guessed that letter. Try again.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word_to_guess:
            self.max_attempts -= 1
            messagebox.showinfo("Incorrect Guess", f"Incorrect guess! {self.max_attempts} attempts remaining.")
        else:
            messagebox.showinfo("Correct Guess", "Correct guess!")

        current_display = display_word(self.word_to_guess, self.guessed_letters)
        self.word_display.set(current_display)

        if "_" not in current_display:
            messagebox.showinfo("Congratulations!", "You guessed the word!")
            self.reset_game()

        if self.max_attempts == 0:
            messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts. The word was: {self.word_to_guess}")
            self.reset_game()

    def reset_game(self):
        self.word_to_guess = choose_word()
        self.max_attempts = 6
        self.guessed_letters = []
        self.word_display.set(display_word(self.word_to_guess, self.guessed_letters))
        self.guess_entry.delete(0, tk.END)

def choose_word():
    words = [
        "apple", "banana", "cherry", "elephant", "butterfly", "giraffe",
        "penguin", "monkey", "orange", "tiger", "sunflower", "bicycle",
        "rainbow", "guitar", "robot", "turtle", "flower", "jellyfish",
        "caterpillar", "dragonfly", "koala", "rocket", "puzzle", "panda",
        "bear", "candy", "rocket", "star", "book", "ocean", "moon",
        "kangaroo", "dolphin", "lion", "tree", "train", "carrot", "cloud",
        "fish", "ship", "frog", "snowflake", "heart", "butterfly", "lion",
        "duck", "rabbit", "frog", "starfish", "apple", "tree", "snowman",
        "balloon", "sun", "flower", "smile", "ghost", "spider", "cake",
        "robot", "fish", "rocket", "train", "bear", "moon", "dragon",
        "butterfly", "carrot", "duck", "frog", "lion", "star", "cake",
        "bird", "cat", "dog", "pig", "frog", "fish", "tree", "sun"
    ]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
