from collections import defaultdict

grams = defaultdict(int)

def ngrams(text, n):
	def remove_specials(text):
		letters = [chr(x) for x in range(65,91)]
		return "".join([x for x in text if x in letters])

	text = remove_specials(text.upper()).lower()
	for x in [text[i:i+n] for (i,e) in enumerate(text[:(len(text) - (n-1))])]:
		grams[x] += 1

text = "a a. a,a. bc bc abcd abcd abcd"

grams = defaultdict(int)
ngrams(text, 1)
m = max(grams.values())
data = [x for x in grams if grams[x] == m]
print "Unigram:", sorted(data)[0]


grams = defaultdict(int)
ngrams(text, 2)
m = max(grams.values())
data = [x for x in grams if grams[x] == m]
print "Digram:", sorted(data)[0]


grams = defaultdict(int)
ngrams(text, 3)
m = max(grams.values())
data = [x for x in grams if grams[x] == m]
print "Trigram:", sorted(data)[0]
