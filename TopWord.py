# TopWord V1 outputs a .txt file containing a list of the n most frequently used words from a website. The list lenght (n) website's url are set in the set vars section. 

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
	
# print list to .txt
file = open('MostCommonWords.txt','w+')
file.write(WordList) 
file.close

