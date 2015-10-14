__author__ = 'Polle'
def split(word, letter):
    """Function for splitting strings on a specific character."""
    word_list = []
    currentWord = ""
    for l in word:
        if l == letter:
            word_list.append(currentWord)
            currentWord = ""
        else:
            currentWord += l
    word_list.append(currentWord)
    return word_list
