import re


# 3 ways to tokenize a sentence

sentence = "When I'M a Duchess,' she said to herself, (not in a very hopeful tone though), 'I won't have any pepper in my kitchen AT ALL. Soup does very well without--Maybe it's ! 12$ 82% always pepper $10.2 U.S.A. that makes people hot-tempered,'..."

sentence = sentence.lower()
print(sentence.split())

print('\n\n')
# Regex
b = re.findall('\w+', sentence)
print(b)

# Regex
print('\n\n')
a = re.split('\W+', sentence)
print(a)
