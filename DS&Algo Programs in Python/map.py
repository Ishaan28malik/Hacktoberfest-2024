filename = input('Please provide filename:')
pattern = input('Please provide the word to search:')
file = open(filename)
if file:
    d = dict()
    for lines in file:
        lines = lines.rstrip()
        words = lines.split()
        if words.count(pattern) > 0:
            for word in words:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
        else:
            print(pattern, ' does not exist in the given file.')

print('The frequency of the word ', pattern, ' is ', d[pattern])
