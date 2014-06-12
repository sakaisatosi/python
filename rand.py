import nltk
def generate_model(cfdist, word, num=15):
    for i in range(num):
	print word,
	word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
biagrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(biagrams)
#cfd.plot()
#print(cfd)
generate_model(cfd, 'living')
