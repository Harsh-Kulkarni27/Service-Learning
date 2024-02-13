import random
import tkinter as tk
from PIL import Image, ImageTk

class MatchGame:
    def __init__(self, root):
        self.root = root
        self.words = ["bear", "bird", "cat", "cow", "dog", "duck", "fish", "frog", "lion", "wolf"]
        self.selected_words = random.sample(self.words, 5)
        self.word_to_picture = {word: word + ".png" for word in self.selected_words}
        self.selected_images = [self.word_to_picture[word] for word in self.selected_words]
        self.selected_words_shuffled = self.selected_words.copy()
        random.shuffle(self.selected_words_shuffled)
        self.selected_word = None
        self.selected_picture = None
        self.score = 0

        self.load_images()
        self.create_widgets()

    def load_images(self):
        self.photo_images = [self.load_and_resize_image(picture) for picture in self.selected_images]

    def load_and_resize_image(self, picture):
        original_image = Image.open(picture)
        resized_image = original_image.resize((150, 150), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def create_widgets(self):
        self.word_frame = tk.Frame(self.root)
        self.word_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.picture_frame = tk.Frame(self.root)
        self.picture_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 30))
        self.message_label.pack(side="bottom", fill="both", expand=True)

        for i, word in enumerate(self.selected_words_shuffled):
            word_button = tk.Button(self.word_frame, text=word, font=("Helvetica", 40), command=lambda w=word: self.word_selected(w))
            word_button.grid(row=i, column=0, padx=0, pady=40)
            # Use a default argument to capture the current value of 'word'
            picture_button = tk.Button(self.picture_frame, image=self.photo_images[i], command=lambda p=self.word_to_picture[word], w=word: self.picture_selected(p, w))
            picture_button.grid(row=i, column=0, padx=10, pady=10)

        tk.Label(self.root, text=f"Score: {self.score}", font=("Helvetica", 20)).pack(side="bottom", fill="x", padx=10)

    
    def picture_selected(self, picture, word):
        self.selected_picture = picture
        self.selected_word = word
        self.update_selection()


    def word_selected(self, word):
        self.selected_word = word
        self.update_selection()



    def update_selection(self):
        if self.selected_word and self.selected_picture:
            if self.selected_word == self.selected_picture:
                self.show_message("Match Well done!")
                self.score += 1
                self.selected_picture = None
                self.selected_word = None
                self.update_score()
            else:
                self.show_message("Error Incorrect match!")


    def show_message(self, message):
        self.message_label.config(text=message)
        self.root.after(2000, self.clear_message)

    def clear_message(self):
        self.message_label.config(text="")

    def update_score(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text").startswith("Score"):
                widget.destroy()

        tk.Label(self.root, text=f"Score: {self.score}", font=("Helvetica", 20)).pack(side="bottom", fill="x", padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    match_game = MatchGame(root)
    root.mainloop()
