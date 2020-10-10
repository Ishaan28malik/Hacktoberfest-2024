lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaaa', 
        'K':'abaab', 'L':'ababa', 'M':'ababb', 'N':'abbaa', 'O':'abbab', 
        'P':'abbba', 'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba', 
        'U':'baabb', 'V':'baabb', 'W':'babaa', 'X':'babab', 'Y':'babba', 'Z':'babbb'} 

def decrypt(message): 
    decipher = '' 
    i = 0


    while True : 

        if(i < len(message)-4): 

            substr = message[i:i + 5] 

            if(substr[0] != ' '): 
            
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)] 
                i += 5 
            else:
                decipher += ' '
                i += 1  
        else: 
            break 

    return decipher 

def main(): 
    

    message = input("Enter Your Cipher Text: " )
    result = decrypt(message.lower()) 
    print (result) 

if __name__ == '__main__': 
    main() 
