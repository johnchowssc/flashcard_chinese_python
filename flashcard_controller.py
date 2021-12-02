import pandas as pd

# Load csv in dataframe #

SOURCE_FILE = "data/chinese_2K_by_frequency.csv"  # From jeff carp's Weibo post analysis
# https://www.jeffcarp.com/posts/2020/most-common-chinese-words-on-weibo/

TARGET_FILE = "data/chinese_subset.csv"

class FlashControl:
    def __init__(self, load_previous):
        self.df = ""
        self.random_row = ""
        self.random_word = ""
        self.random_definition = ""
        if load_previous:
            self.df = pd.read_csv(TARGET_FILE)
        else:
            self.df = pd.read_csv(SOURCE_FILE)

    # Strip HTML tags #

    def html_strip(self, html_string: str) -> str:
        html_stripped = html_string.replace("<br/>", " ").replace("<b>", "").replace("</b>", "\n")
        return html_stripped

    # Get Random Row

    def get_random(self):
        self.random_row = self.df.sample()
        self.random_word = self.random_row.word.iloc[0]
        self.random_definition = self.random_row.back.iloc[0]
        self.random_definition = self.html_strip(self.random_definition)
        print(self.random_row.index)

        # Debugging Stuff
        # print(f"{self.random_word}\n{self.random_definition}")
        # Debugging Stuff

    def remove_word(self):
        row_index = self.random_row.index
        self.df = self.df.drop(index=row_index)
        print(f"Row deleted: {row_index}, Size: {self.df.count()}")
        try:
            self.df.to_csv(TARGET_FILE)
        except FileNotFoundError as error:
            print(error)
