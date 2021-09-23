import posTagger as pt
tagger = pt.posTagger()
sentence = 'તારુ નામ શુ છે?'  # What is your name?
print(tagger.pos_tag(sentence))