import nltk 
import requests
from nltk.corpus import wordnet
import re

wnid = []

local_wnid = []
children_wnid = []

def toString(list):
    string = "\n".join(list)
    return string

def get_wnid(query):
     get_local_wnid(query)
     for id in local_wnid[1:10]: 
         get_children_wnid(id)
     wnid = local_wnid + children_wnid
     return wnid

def get_local_wnid(query):
    #human readable query -> wnid
    synset = open("words.txt","r", 1) #searching from words.txt
    synset.seek(0)
    for line in synset:
        if (query.lower() in line.lower()):
            id = line[0:9]
            local_wnid.append(id)
    synset.close()

def get_children_wnid(wnid):
    #get children wnid
    payload = {'full': '1', 'wnid': wnid}
    r = requests.get('http://www.image-net.org/api/text/wordnet.structure.hyponym', params = payload)
    page_contents = r.text #string
    page_contents_to_list = re.split(r'[\n\r]\s*', page_contents)
    #append to list
    children_wnid.append(page_contents_to_list[0]) #html page formatted weird
    for id in page_contents_to_list[1:]:
        children_wnid.append(id[1:10])
    del children_wnid[-1] #again, weird '' at end of list


def main():
     query = input("Enter your search query: ")
     print(get_wnid(query))


if __name__ == "__main__":
    main()




