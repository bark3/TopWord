def GetText(url):
	# GetText takes a webpage's URL (as a string), parses the html, and outputs a string containing the words from the webpage. This function requires the BeautifulSoup and requests packages. 

	# Set env
	import requests
	from bs4 import BeautifulSoup

	# Opens url
	page = requests.get(url)

	# Parse html
	soup = BeautifulSoup(page.content, 'html.parser')

	# Returns the webpage's text
	return soup.text 
