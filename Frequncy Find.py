from operator import pos

import nltk
#from Cython.Tempita.compat3 import text


#from statsmodels.sandbox.distributions.examples.ex_gof import freq

wordstring =  open("Articles\\1.txt" , encoding="utf-8").read()


wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
wordfreq.sort()
print("Frequencies\n" + str(wordfreq[::-1]) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))