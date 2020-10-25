def countVowels(S):
    total_size = len(S)
    vowelString = "AaEeIiOoUu"
    vowels = len([each for each in S if each in vowelString])
    consonants = total_size - vowels
    print("There are {} vowels and {} consonants in {}".format(vowels, consonants, S))
countVowels('hello')
countVowels('hi')
countVowels('aeiocc')
