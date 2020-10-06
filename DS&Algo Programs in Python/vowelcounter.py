def countVowels(S):
    total_size = len(S)
    vowels = 0

    for char in S:
        if char in 'aeiouAEIOU':
            vowels = vowels + 1
    consonants = total_size - vowels
    
    if vowels > consonants:
        print('There are more vowels than consonants in the string ' + S)
    elif vowels == consonants:
        print('Both vowels and consonants are equal in the string ' + S)
    else:
        print('There are more consonants than vowels in the string ' + S)

countVowels('hello')
countVowels('hi')
countVowels('aeiocc')
