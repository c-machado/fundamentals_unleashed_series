def rev_phrase(phrase):
    words = []
    length = len(phrase)
    spaces = [' ']

    i = 0

    while i < length:
        if phrase[i] not in spaces:
            print(phrase[i])
    i += 1
rev_phrase(' holi ')