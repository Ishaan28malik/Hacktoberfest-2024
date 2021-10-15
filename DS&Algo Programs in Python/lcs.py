def longestCommonSubsequence( A, B):
    m = len(A)
    n = len(B)
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i==0 or j==0:
                memo[i][j]=0
            if A[i - 1] == B[j - 1]:
                memo[i][j] = 1 + memo[i - 1][j - 1]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[m][n]

A = "abc"
B = "abc"
print("Length of LCS is ", longestCommonSubsequence(A, B) )
