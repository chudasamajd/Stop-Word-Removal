from nltk import FreqDist
text = "Learn and practice and learn to practice"
words = text.split()
fdist1 = FreqDist(words)
print(fdist1)
print(fdist1.most_common())