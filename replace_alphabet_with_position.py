from string import ascii_lowercase

Letters={Letter : str(index) for index,Letter in enumerate(ascii_lowercase,start=1)}
def alphabet_position(text):
    text=text.lower()
    text_numbers=[Letters[i] for i in text if i in Letters]
    return ' '.join(text_numbers)