from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
TITLE_TEXT = "Language"
WORD_TEXT = "Word"


class FlashCardUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashcards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.image_card_front = PhotoImage(file="images/card_front.png")
        self.image_card_back = PhotoImage(file="images/card_back.png")

        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.create_image(400, 263, image=self.image_card_front)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.image_tick = PhotoImage(file="images/right.png")
        self.image_cross = PhotoImage(file="images/wrong.png")

        self.label_title = Label(text=TITLE_TEXT, font=FONT_TITLE, fg="black", bg="white", highlightthickness=0)
        self.label_title.place(x=400, y=150, anchor="center")
        self.label_word = Label(text=WORD_TEXT, font=FONT_WORD, fg="black", bg="white", highlightthickness=0)
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
        pass

    def button_cross_pressed(self):
        pass
