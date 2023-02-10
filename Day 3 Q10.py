def editDistance(word1, word2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if word1[m-1] == word2[n-1]:
        return editDistance(word1, word2, m-1, n-1)
    return 1 + min(editDistance(word1, word2, m, n-1),
                   editDistance(word1,word2, m-1, n),
                   editDistance(word1,word2, m-1, n-1))
word1 = input("enter a word:")
word2 = input("enter a word:")
print(editDistance(word1,word2,len(word1),len(word2)))
