"""
Refer : http://www.dictionary.com/slideshows/food-idioms?prev=umwords.obviously#nutshell

For every slide, we are going to extract:
- the word
- the pronunciation
- audio data of the corresponding pronunciation.

"""
from bs4 import BeautifulSoup
import pprint as pp
import urllib


page = 'source_1.htm'
soup = BeautifulSoup(open(page), "lxml")

#Get content of all headwords
headings = soup.find_all('div', class_='headword')

#More generally :
#headings = soup.find_all('div', {'class', 'headword'} )

#All info
all_info = []

for head in headings:
	word = head.find('a').text.strip()
	pronunciation = head.find_next_sibling('div', class_='pron').text.strip()
	audio_url = head.find('source',{'type':'audio/mpeg'}).get('src')
	
	mp3file = urllib.urlopen(audio_url)
	local_url = 'audio/{}.mp3'.format(word)
	print "Fetching {} ... ".format(audio_url)

	with open(local_url,'w+') as aout:
		while True:
			data = mp3file.read(4096)
			if data:
				aout.write(data)
			else:
				break

	all_info.append( (str(word), str(pronunciation), audio_url, local_url) )

pp.pprint(all_info, indent=4)

#print [w for w,p,a,l in all_info]
