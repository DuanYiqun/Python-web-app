def trim(word):
    if word[:1] !=' ' and word[-1:] !=' ':
        return word
    elif word[:1]==' ':
        return trim(word[1:])
    else:
        return trim(word[:-1])

print(trim("hello        "))