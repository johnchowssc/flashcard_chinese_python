import pandas as pd

SOURCE_FILE = "data/chinese_2K_by_frequency.csv"  # From jeff carp's Weibo post analysis
# https://www.jeffcarp.com/posts/2020/most-common-chinese-words-on-weibo/

# Load csv in dataframe #


class FlashControl:
    def __init__(self):
        self.timer=None
        try:
            self.df = self.load_file(SOURCE_FILE)
            print("File Loaded")
        except FileNotFoundError as error:
            print(error)
        self.random_row = ""
        self.random_word = ""
        self.random_definition = ""

    # Load File

    def load_file(self, filename):
        data_frame = pd.read_csv(filename)
        return data_frame

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

        # Debugging Stuff
        # print(f"{self.random_word}\n{self.random_definition}")
        # Debugging Stuff