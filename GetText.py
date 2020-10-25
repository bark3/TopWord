def GetText(url):

	import requests
	from bs4 import BeautifulSoup

	# opens url
	page = requests.get(url)

	# parse html
	soup = BeautifulSoup(page.content, 'html.parser')

	#
	return soup.text 
