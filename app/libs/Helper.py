def is_isbn_or_key(word):
    """
        this function is to judge the searching word is isbn or key_word
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'key'
    return isbn_or_key