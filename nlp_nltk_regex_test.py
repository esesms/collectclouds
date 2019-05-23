#Sue Huang
#03/15/19
#v2.2
#This program:
#reads text from a text file
#runs sentence tokenization on the text file
#runs regex on the sentences to extract matches
#runs word tokenization on the matches
#prints the matches which contain an adjective or noun and then the word 'clouds'

#INSTALL: https://likegeegks.com/nlp-tutorial-using-python-nltk/

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tokenize import MWETokenizer
from itertools import permutations
from prettytable import PrettyTable

import re
import food



file = open("twitter_text.txt", "r", encoding="utf-8")
#print(file.read())

text = file.read()
list_of_report = food.get_reports()

#make set of joined word permutations - changed from list to set to ensure only one instance per food
list_join_wd_permutations = set()

#make list of mwe tokenizers joined by space
mwe_tokenizer = MWETokenizer(separator=' ')

#dictionary to count the food words
counter = dict()

#total food count
total = 0

#smallword_list = ['of', 'the', 'and', 'out', 'na', 'vit', 'n']
stopwords = set(stopwords.words('english'))

#add more words to stopwords list
stopwords.update(['n', 'na', 'new', 'vit', 'style', 'low', 'sprd', 'it\'s', 'dried', 'fungi'])

for food in list_of_report:
    description = food["Description"].lower() #converts everything to lower case
    tokens = word_tokenize(description)
    words = [word for word in tokens if word.isalpha() and word not in stopwords]


    #iterates through the food descriptions
    for word in words:

        #if food description contains certain words generate permutations of the description and append to the list

        #COMMENT OR UNCOMMENT BELOW AND CHANGE FOOD HERE TO LIMIT SEARCH IN DATABASE
        if word == "peanut" or word == "cotton":
            min_perm = 1
            max_perm = 3
            wd_permutations = []
            for x in range(min_perm, max_perm):
                for foods in permutations(words, x):
                    wd_permutations.append(foods)
            #wd_permutations = permutations(words, 2)
            list_wd_permutations = list(wd_permutations)

            #join tuples back together into a string and append them to the new list
            for list_wd_permutation in list_wd_permutations:

                join_wd_permutations = (' '.join(list_wd_permutation))
                list_join_wd_permutations.add(join_wd_permutations)

                #if the number of words is more than 1, then add it to the list of mwe
                if (len(list_wd_permutation) > 1):
                    mwe_tokenizer.add_mwe(list_wd_permutation)


print("\n+++++++++++\n")

print("Complete list of permutations:")
print(list_join_wd_permutations)

print("\n+++++++++++\n")


print("Complete list of multi-word expressions:")
print(mwe_tokenizer._mwes)

print("\n+++++++++++\n")

#tokenizes according to sentences
tw_sentence_tokens = sent_tokenize(text)

#iterates through the sentence tokens
for tw_sentence in tw_sentence_tokens:

    #use https://regex101.com/ for regular expression tests
    #use re.search to find things inside the string and re.match to start at beginning of string

    #food = "cotton candy"
    #regex to match whole phrases up to period boundaries that contain near terms taste(s) and cloud(sd)
    match = re.search(r"[^\.\!\?\n]*(?:[Tt]aste.?\W+(?:\w+\W+){0,4}?[Cc]loud.?|[Cc]loud.?\W+(?:\w+\W+){0,4}?[Tt]aste.?)[^\.\!\?\n]*", tw_sentence) #only output sentences that have the phrase clouds taste like <food from database>

    #exception handling
    try:
        phrase = match.group()
    except:
        phrase = None

    if phrase:
        phrase = phrase.lower()
        ph_tokens = word_tokenize(phrase)
        mwe_tokens = mwe_tokenizer.tokenize((phrase).split())

        for mwe_token in mwe_tokens:
            for list_join_wd_permutation in list_join_wd_permutations:
                if mwe_token == list_join_wd_permutation:
                    print(mwe_tokens)

                    if not list_join_wd_permutation in counter:
                        print('Adding new food to dictionary...')
                        counter[list_join_wd_permutation] = 1
                    else:
                        print('Incrementing existing food in dictionary...')
                        counter[list_join_wd_permutation] += 1
                    print("Dictionary is: ", counter)
                    print('---')
                    break
#

print("List of all the foods in the dictionary are:")

for food, count in counter.items():
     print(food + ", " + str(count))

print('---')
print("Sum total of all the foods in the dictionary is:")

for count in counter.values():
    total = total + count

print(total)

print('---')
print("Percentage value of each food in the dictionary is:")

table = PrettyTable(['Food', 'Count', 'Percent'])

for food, count in counter.items():
     percent = (count/total) * 100
     table.add_row([food, str(count), str(percent) + "%"])

table.sortby = "Percent"
print(table)
