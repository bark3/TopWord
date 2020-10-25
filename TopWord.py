# Set Env
import spacy
from collections import Counter
from GetText import GetText

# Set vars
n = 100 # Length of most common list
url = "https://mitvergnuegen.com/2017/21-ziemlich-gute-tipps-fuer-den-herbst-in-berlin-2017/" # Url of Webpage to be screened

#####

# load spacy medium german nlp
nlp = spacy.load('de_core_news_md')

# import website text from GetText
doc = GetText(url)
doc = nlp(doc)

# Gets vector of words on the webpage
words = [token.text for token in doc if token.is_punct != True and token.is_space != True]

# Gets most common words
freq = Counter(words)
list = freq.most_common(n)
WordList = str(list).strip('[]')

# Format list for print
# for x in list 
	


# print list to .txt
file = open('MostCommonWords.txt','w+')
file.write(WordList) 
file.close

