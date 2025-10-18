import itertools

s=  input("Enter a word: ")

t=list(itertools.permutations(s, len(s)))
text_file = open("output.txt", "w")

for i in range(0, len(t)):
    #writing lines makes it a lot slower
    text_file.write(''.join(t[i]) + "\n")

print(i)
