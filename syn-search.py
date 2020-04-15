import nltk 
import requests
from nltk.corpus import wordnet
import re 

words = []

#human readable query -> wnid
query = input("Enter your search query: ")
#searching from words.txt
synset = open("words.txt","r", 1)
synset.seek(0)
for line in synset:
    if (query.lower() in line.lower()):
        wnid = line[0:9]
        words.append(wnid)
synset.close()


#get children wnid
payload = {'full': '1', 'wnid': words[0]}
r = requests.get('http://www.image-net.org/api/text/wordnet.structure.hyponym', params = payload)
# print(r.url)
page_contents = r.text #string
# print (type(page_contents))
page_contents_to_list = re.split(r'[\n\r]\s*', page_contents)
words.append(page_contents_to_list[0]) #html page formatted weird
for id in page_contents_to_list[1:]:
    words.append(id[1:10])
del words[-1] #again, weird '' at end of list


print (words)


