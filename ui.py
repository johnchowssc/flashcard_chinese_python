from tkinter import *
from flashcard_controller import FlashControl

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
FONT_DEFINITION = ("Arial", 20, "normal")
TITLE_TEXT = "Language"
WORD_TEXT = "Word"
SOURCE_LANGUAGE = "Chinese"
TARGET_LANGUAGE = "English"

class FlashCardUI:
    def __init__(self):
        self.flashcard = FlashControl()

        self.window = Tk()
        self.window.title("Flashcards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.image_card_front = PhotoImage(file="images/card_front.png")
        self.image_card_back = PhotoImage(file="images/card_back.png")

        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas_image = self.canvas.create_image(400, 263, image=self.image_card_front)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.image_tick = PhotoImage(file="images/right.png")
        self.image_cross = PhotoImage(file="images/wrong.png")

        self.label_title = Label(text=TITLE_TEXT, font=FONT_TITLE, fg="black", bg="white", highlightthickness=0)
        self.label_title.place(x=400, y=150, anchor="center")
        self.label_word = Label(text=WORD_TEXT, font=FONT_WORD, fg="black", bg="white", highlightthickness=0,
                                wraplength=700, justify="center")
        self.label_word.place(x=400, y=263, anchor="center")
        self.button_cross = Button(image=self.image_cross, highlightbackground="white", highlightthickness=0, bd=0,
                                   command=self.button_cross_pressed)
        self.button_cross.grid(row=1, column=0)
        self.button_tick = Button(image=self.image_tick, highlightbackground="white", highlightthickness=0, bd=0,
                                  command=self.button_tick_pressed)
        self.button_tick.grid(row=1, column=1)

        self.window.mainloop()

    # Button functions #

    def button_tick_pressed(self):
        self.flashcard.get_random()
        self.canvas.itemconfig(self.canvas_image, image=self.image_card_front)
        self.label_title.config(text=SOURCE_LANGUAGE, bg="white")
        self.label_word.config(text=self.flashcard.random_word, font=FONT_WORD, bg="white")
        self.window.after(5000, func=self.flip)

    def button_cross_pressed(self):
        self.flashcard.flash()
        self.label_title.config(text=SOURCE_LANGUAGE)

    def flip(self):
        self.label_title.config(text=TARGET_LANGUAGE, bg=BACKGROUND_COLOR)
        self.label_word.config(text=self.flashcard.random_definition, font=FONT_DEFINITION, bg=BACKGROUND_COLOR)
        self.canvas.itemconfig(self.canvas_image, image=self.image_card_back)