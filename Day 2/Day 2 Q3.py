def maxwords(sentences):
    max_words=0
    for sentence in sentences:
        words=sentence.split()
        max_words=max(max_words, len(words))
        return max_words
sentences=[input("")]
print("the maximum number of words in aa single sentence is", maxwords(sentences))
