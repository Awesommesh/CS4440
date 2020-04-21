import nltk 
import requests
from nltk.corpus import wordnet
import re
import random

<<<<<<< HEAD
=======
wnid = set()
local_wnid = set()
children_wnid = set()

>>>>>>> 7afb4b4a8960ee4e473b0dae8bf90627422537c4
def toString(list):
    string = "\n".join(list)
    return string

def get_wnid(query):
<<<<<<< HEAD
     wnid = []
     local_wnid = []
     children_wnid = []
     get_local_wnid(query, local_wnid)
     for id in local_wnid: 
         get_children_wnid(id, children_wnid)
     wnid = local_wnid + children_wnid
     return toString(wnid)
=======
     local_wnid.clear()
     children_wnid.clear()
     get_local_wnid(query)
     for id in local_wnid: 
         get_children_wnid(id)
     wnid = local_wnid | children_wnid
     wnid = clean_wnid(wnid)
     return toString(list(filter(None,(list(wnid)))))
>>>>>>> 7afb4b4a8960ee4e473b0dae8bf90627422537c4

def get_local_wnid(query, local_wnid):
    #human readable query -> wnid
    synset = open('words.txt',"r", 1)
    synset.seek(0)
    string_length = len(query) + 0
    query_revised = query.ljust(string_length)
    for line in synset:
        # pattern = r"[\t]"+ re.escape(query_revised) + r"[\n]" 
        # if re.search(pattern, line, re.IGNORECASE):
        if (query_revised.lower() in line.lower()):
            id = line[0:9]
            local_wnid.add(id)
    synset.close()

def get_children_wnid(wnid, children_wnid):
    #get children wnid
    payload = {'full': '1', 'wnid': wnid}
    r = requests.get('http://www.image-net.org/api/text/wordnet.structure.hyponym', params = payload)
    page_contents = r.text #string
    page_contents_to_list = re.split(r'[\n\r]\s*', page_contents)
    #add to set
    children_wnid.add(page_contents_to_list[0]) #html page formatted weird
    for id in page_contents_to_list[1:]:
        children_wnid.add(id[1:10])
    #del children_wnid[-1] #again, weird '' at end of list

def clean_wnid(wnid):
    checker = set()
    synset = open("wnid_classes.txt","r", 1)
    synset.seek(0)
    if len(wnid):
        for line in synset:
            for ele in wnid:
                if ele in line[0:9]:
                    checker.add(ele)
    return checker
    synset.close()
    

def main():
     query = input("Enter your search query: ")
     print(get_wnid(query))


if __name__ == "__main__":
    main()




