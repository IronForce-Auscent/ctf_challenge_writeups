def letter_in_word(letter, word, i):

    if letter in word and letter == word[i]:
        return "^"
    elif letter in word:
        return "!"
    else:
        return "x"

