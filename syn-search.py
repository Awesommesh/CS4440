import nltk 
from nltk.corpus import wordnet 

query = input("Enter your search query: ")

#searching from wordnet 
syn = wordnet.synsets(query) 
print(nltk.word_tokenize(syn[0].definition()))

words = []
#searching from synset.txt
synset = open("synset.txt","r", 1)
for line in synset:
    stripped_line = line.strip()
    if (query.lower() in stripped_line.lower()):
        words += stripped_line.split(",")
        break
synset.close()
print (words)

#rough
# synset = open("synset.txt","r", 1)
# x = synset.read().find(query) #gives starting index, without newlines

# synset.seek(0)
# c = synset.read().count('\n', 0, x) #counting newlines

# synset.seek(x+c-10, 0)  
# line = synset.readline(100)
# words = line.split(",")   
# # words = nltk.word_tokenize(line)
# print (words)

# synset.close()

# print("For: ", query) 