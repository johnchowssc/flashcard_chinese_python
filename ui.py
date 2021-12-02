from tkinter import *
from tkinter import messagebox
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

        self.label_title = self.canvas.create_text(400, 150, text=TITLE_TEXT, font=FONT_TITLE, fill="black")
        self.label_word = self.canvas.create_text(400, 263, text=WORD_TEXT, font=FONT_WORD, fill="black", width=700)
        self.button_cross = Button(image=self.image_cross, highlightbackground="white", highlightthickness=0, bd=0,
                                   command=self.button_cross_pressed)
        self.button_cross.grid(row=1, column=0)
        self.button_tick = Button(image=self.image_tick, highlightbackground="white", highlightthickness=0, bd=0,
                                  command=self.button_tick_pressed)
        self.button_tick.grid(row=1, column=1)
        self.timer = None

        self.load_previous = messagebox.askyesno(title="Load?", message="Load previous?")
        self.flashcard = FlashControl(self.load_previous)
        self.window.mainloop()

    # Button functions #

    def button_tick_pressed(self):
        # Check if initial
        if self.flashcard.random_word == "":
            pass
        else:
            self.flashcard.remove_word()
        self.flash()

    def button_cross_pressed(self):
        self.flash()

    def check_timer(self):
        #  Check to see if timer has already started, and reset if so.
        if self.timer == None:
            pass
        else:
            self.window.after_cancel(self.timer)

    def flash(self):
        self.check_timer()
        self.flashcard.get_random()
        self.canvas.itemconfig(self.canvas_image, image=self.image_card_front)
        self.canvas.itemconfig(self.label_title, text=SOURCE_LANGUAGE)
        self.canvas.itemconfig(self.label_word, text=self.flashcard.random_word, font=FONT_WORD)
        self.timer = self.window.after(5000, func=self.flip)

    def flip(self):
        self.canvas.itemconfig(self.label_title, text=TARGET_LANGUAGE)
        self.canvas.itemconfig(self.label_word, text=self.flashcard.random_definition, font=FONT_DEFINITION)
        self.canvas.itemconfig(self.canvas_image, image=self.image_card_back)