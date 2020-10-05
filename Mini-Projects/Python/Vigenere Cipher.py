# -*- coding: utf-8 -*-

""" ------------------------- Vigenere Cipher --------------------------- """

""" ---------- INITIALIZING ALPHABETS AND THEIR INDEX VALUES ---------------"""

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," "]

num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]


""" -------------------- TAKING INPUT FROM THE USER ---------------------"""
 
plaintext = input("Enter the text to be encrypted : ")

while(True):
    keyword = input("Enter a keyword : ")
    
    if (len(keyword) > len(plaintext)):
        print("The length of KEYWORD should be LESS than that of PLAINTEXT. Please try again.")
    else:
        break
    
keyword_list = list(keyword.strip())

for i in range(len(plaintext)):
    if (len(keyword_list) < (len(plaintext))):   
        keyword_list.append(keyword_list[i])   # increasing the length of keyword
        
    else:
        keyword_list = ''.join(map(str, keyword_list))

""" ------------------------------ Encryption Process -------------------------------- """

encryptedtext = []

def encryption(plaintext,keyword,alpha,num):
    
    for i in range(len(plaintext)):
        a = plaintext[i]                   # taking one letter of plaintext at a time
        b = keyword[i]                     # taking one letter of keyword at a time
        
        plaintext_index_in_alpha = alpha.index(a) # numeric value of plaintext index
        keyword_index_in_alpha = alpha.index(b)   # numeric value of keyword index
        
        c = num[plaintext_index_in_alpha]       # getting the numeric value of the letter
        d = num[keyword_index_in_alpha]         # getting the numeric value of the letter
        
        e = int((c+d)%53)                 # getting the numeric value of encrypted word by taking mod 26
        
        f = alpha[e]             # getting the letter from the index value
        
        encryptedtext.append(f)
        
        encrypted_text =''.join(map(str,encryptedtext))

    print("Encrypted text : {}".format(encrypted_text))
    decryption(encrypted_text,keyword,alpha,num)
    
""" ------------------------------ Decryption Process -------------------------------- """

decryptedtext = []

def decryption(encrypted_text, keyword, alpha, num):
    for i in range(len(plaintext)):
        a = encrypted_text[i]
        b = keyword[i]
        
        encrypted_text_index_in_alpha = alpha.index(a) # numeric index value of encrypted text
        keyword_index_in_alpha = alpha.index(b)        # numeric index value of keyword text
        
        c = num[encrypted_text_index_in_alpha]       # numeric value of the encrypted letter
        d = num[keyword_index_in_alpha]              # numeric value of the keyword 
        
        e = int((c-d+53)%53)                 # calculation
        
        f = alpha[e]                         # getting the letter from the index value of the letter
        
        decryptedtext.append(f)
        
        decrypted_text = ''.join(decryptedtext)

    print("Decrypted text : {}".format(decrypted_text))
 
a = encryption(plaintext,keyword_list,alpha,num)

print("New Keyword : {}".format(keyword_list))

