def countVowels(S):
    total_size = len(S)
    vowels = 0

    for char in S:
        # checking if vowel is present in the string if it is present then incrementing the vowel counter
        if char in 'aeiouAEIOU':
            vowels = vowels + 1

    # number of consonants will be determined by the following expression
    consonants = total_size - vowels
    # printing result
    if vowels > consonants:
        print('There are more vowels than consonants in the string ' + S)
    elif vowels == consonants:
        print('Both vowels and consonants are equal in the string ' + S)
    else:
        print('There are more consonants than vowels in the string ' + S)

countVowels('hello')
countVowels('hi')
countVowels('aeiocc')
