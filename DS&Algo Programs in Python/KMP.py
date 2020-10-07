def KMP(pat, txt): 
    M = len(pat) 
    N = len(txt)    
    lps = [0]*M 
    j = 0 
    findLps(pat, M, lps) 
    i = 0 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            print("Found pattern at index " + str(i-j) )
            j = lps[j-1] 
  
        elif i < N and pat[j] != txt[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
def findLps(pat, M, lps): 
    j = 0  
    lps[0]
    i = 1  
    while i < M: 
        if pat[i]== pat[j]: 
            j += 1
            lps[i] = j
            i += 1
        else: 
            if j != 0: 
                j = lps[j-1]                 
            else: 
                lps[i] = 0
                i += 1
  
txt = "ABABDABACDABABCABA"
pat = "ABABCABA"
KMP(pat, txt) 
