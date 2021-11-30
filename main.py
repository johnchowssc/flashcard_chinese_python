import pandas as pd
import ui

SOURCE_FILE = "data/chinese_2K_by_frequency.csv"  # From jeff carp's Weibo post analysis
# https://www.jeffcarp.com/posts/2020/most-common-chinese-words-on-weibo/

data_dict = {}

# Read from CSV #


def load_file(filename):
    data_frame = pd.read_csv(filename)
    return data_frame

# Strip HTML tags #


def html_strip(html_string: str) -> str:
    html_stripped = html_string.replace("<br/>", "\n").replace("<b>", "").replace("</b>", "")
    return html_stripped


# Load csv in dataframe #

df = load_file(SOURCE_FILE)
ui = ui.FlashCardUI()

random_row = df.sample()
random_word = random_row.word.iloc[0]
random_definition = random_row.back.iloc[0]
random_definition = html_strip(random_definition)
print(f"{random_word}\n{random_definition}")
