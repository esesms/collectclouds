import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk import pos_tag

file = open("environment_words.txt", "r", encoding="utf-8")
text = file.read()
text = text.lstrip()
text = text.rstrip()
text = text.lower()

text = re.split("\n", text)

individual_words = []
counter = 0
for element in text:
    if element and (element != "top of page") and (len(element) > 1):
        print(str(counter) + ' ' + text[counter])
    else:
        del text[counter]
    counter = counter + 1

#print(text)

for element in text:
    tokens = word_tokenize(element)
    print(tokens)
    for word in tokens:
        if word not in text and (word is not "(" or ")") and word is not :
            text.append(word)

print(text)
#print(individual_words)
     #   text.pop(counter)
    #print(element)
    #    del text[counter]
    #elif element == "top of page":
    #    del text[counter]
    #else:
        #print(element)
    #counter += 1
#text = re.sub("top of page", '', text)
#text = re.sub("\n", '\',\'', text)

#print(text)

#with open('environment_words.txt', 'w') as w:
    #w.write(words)