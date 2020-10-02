def checkpalyndrom (teks) :

    """A palindrome is a word, number, phrase, or other sequence of characters which reads 
    the same backward as forward, such as madam, racecar. There are also numeric palindromes, 
    including date/time stamps using short digits 11/11/11 11:11 and long digits 02/02/2020. 
    Sentence-length palindromes ignore capitalization, punctuation, and word boundaries."""

    list = []
    tail = ''
    head = ''
    indicator = True
    for i in range (len(teks)) :
        if teks[i] != ',' and teks[i] != '.' and teks[i] != "'" and teks[i] != '"' and teks[i] != '!' and teks[i] != '?' and teks[i] != ' ' :
            list.append(teks[i])
    while len(list) > 1 and indicator  :
        head += list.pop(0)
        tail += list.pop()
        if tail != head :
            indicator = False
    if indicator :
        print(teks, "its palyndrom.")
    else :
        print(teks, "not palyndrom.")


inputdata = input("input : ")

print('Result : ')
checkpalyndrom(inputdata)
