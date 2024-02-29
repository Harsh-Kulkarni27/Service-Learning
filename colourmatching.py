import tkinter as tk
from tkinter import messagebox
import random

# Define a dictionary of colors and their corresponding names
colors = {
    "red": "#FF0000",
    "blue": "#0000FF",
    "green": "#00FF00",
    "yellow": "#FFFF00",
    "pink": "#FFC0CB",
    "orange": "#FFA500",
    "purple": "#800080",
    "brown": "#A52A2A",
    "gray": "#808080",
    "black": "#000000",
}

# Concatenate folder path with image filenames
for name, color_code in colors.items():
    colors[name] = color_code

# Define a function to check the answer
def check_answer(selected_option):
    global correct_color
    if selected_option == correct_color:
        messagebox.showinfo("Correct", "Correct Option!")
        next_color()  # Automatically move to the next question if correct
    else:
        messagebox.showerror("Incorrect", f"Wrong Answer! Correct answer is: {correct_color}")

# Define a function to display the next color and options
def next_color():
    global correct_color
    global color_object
    global option_buttons
    
    # Randomly choose a color
    color_name, color_code = random.choice(list(colors.items()))
    correct_color = color_name
    
    # Display the color
    color_object.config(bg=color_code)
    
    # Get all color names except the correct one
    option_names = list(colors.keys())
    option_names.remove(correct_color)
    
    # Randomly select 3 incorrect options
    incorrect_options = random.sample(option_names, 3)
    
    # Add correct answer to options
    options = incorrect_options + [correct_color]
    random.shuffle(options)
    
    # Update option buttons
    for i in range(4):
        option_buttons[i].config(text=options[i])

# Create the main window
root = tk.Tk()
root.title("Color Matching Game")

# Create the color label with fixed size
color_object = tk.Label(root, width=30, height=2)
color_object.pack(pady=(10, 10))

# Create the option buttons
options_frame = tk.Frame(root, width=600, height=100)
options_frame.pack(pady=(0, 10))

# Create option buttons with larger font size
option_buttons = []
for i in range(4):
    option_button = tk.Button(options_frame, text="", font=("Arial", 16), width=15, height=2,
                              command=lambda idx=i: check_answer(option_buttons[idx]["text"]))
    option_button.pack(side=tk.LEFT, padx=10)
    option_buttons.append(option_button)

# Create the next button with larger font size
next_button = tk.Button(root, text="Next Color", font=("Arial", 16), width=15, height=2, command=next_color)
next_button.pack(pady=(0, 10))

# Bind the escape key to close the window
root.bind("<Escape>", lambda event: root.destroy())

# Display the first color and options
next_color()

# Run the Tkinter event loop
root.mainloop()
