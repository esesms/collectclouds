#Sue Huang
#03/15/19
#This program:
#reads text from a text file
#runs sentence tokenization on the text file
#runs regex on the sentences to extract matches
#runs word tokenization on the matches
#prints the sections that contain food words from the database

#INSTALL: https://likegeeks.com/nlp-tutorial-using-python-nltk/

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tokenize import MWETokenizer
from itertools import permutations #to iterate through lists in permutations and combinations

import re
import food



file = open("twitter_text.txt", "r")
#print(file.read())

text = file.read()
list_of_report = food.get_reports()

for food in list_of_report:
    description = food["Description"].lower() #converts everything to lower case
    tokens = word_tokenize(description)
    words = [word for word in tokens if word.isalpha() and word != "dry" and word != "mix" and word != "reg" and word != "prep"] #removes commas
    #do a replacement of abbreviations with full words for example inst with instant and whl with whole
    #print(words)

    #iterates through the food descriptions
    for word in words:

        #if food description contains cottons generate permutations of the description and append to the list
        if word == "pudding":
            min_perm = 1
            max_perm = 3
            wd_permutations = []
            for x in range(min_perm, max_perm):
                for foods in permutations(words, x):
                    wd_permutations.append(foods)
            #wd_permutations = permutations(words, 2)
            list_wd_permutations = list(wd_permutations)
            #print(list_wd_permutations)

            #make a list to hold the joined strings of permutated foods
            list_join_wd_permutations = []

            #join tuples back together into a string and append them to the new list
            for list_wd_permutation in list_wd_permutations:

                join_wd_permutations = (' '.join(list_wd_permutation))
                list_join_wd_permutations.append(join_wd_permutations)

                print(list_join_wd_permutations)
                #print(type(list_join_wd_permutations))

print("\n+++++++++++\n")

mwe_tokenizer = MWETokenizer(list_wd_permutations, separator=' ')

#tokenizes according to words
#print(word_tokenize(text))

#tokenizes according to sentences
tw_sentence_tokens = sent_tokenize(text)
#print(tw_sentence_tokens)

#tests variable typeR
#print(isinstance(tw_sentence_tokens, list))

#iterates through the sentence tokens
for tw_sentence in tw_sentence_tokens:
    #print(tw_sentence, "\n---")

    #test variable type
    #print(isinstance(tw_sentence, str))

    #use https://regex101.com/ for regular expression tests
    #use re.search to find things inside the string and re.match to start at beginning of string

    #food = "cotton candy"
    #regex to match whole phrases up to period boundaries that contain near terms taste(s) and cloud(sd)
    match = re.search(r"[^\.]*(?:taste.?\W+(?:\w+\W+){1,6}?cloud.?|cloud.?\W+(?:\w+\W+){1,6}?taste.?)[^\.]*", tw_sentence) #only output sentences that have the phrase clouds taste like <food from database>

    #exception handling
    try:
        phrase = match.group()
    except:
        phrase = None

    if phrase:
        phrase = phrase.lower()
        ph_tokens = word_tokenize(phrase)
        mwe_tokens = mwe_tokenizer.tokenize((phrase).split())
        #print(mwe_tokens)

        for mwe_token in mwe_tokens:
            #print(mwe_token)
            #print(type(mwe_token))
            for list_join_wd_permutation in list_join_wd_permutations:
                #print(list_join_wd_permutation)
                #print(type(joined_list_wd_permutation))
                if mwe_token == list_join_wd_permutation:
                    print(mwe_tokens)
        #ph_pos_tokens = nltk.pos_tag(ph_tokens) #list of tuples
        #print(ph_pos_tokens)
        #print(ph_pos_tokens, "\n-")
        #print(type(ph_pos_tokens))
        #for ph_pos_token in ph_pos_tokens:
            #print(ph_pos_token, "\n--")
            #print(type(ph_pos_token)) #tuples
            #if ph_pos_token[1] == "JJ" or (ph_pos_token[1] == "NN" and ph_pos_token[0] != "clouds"): #tests if word preceding clouds is a noun or adjective
                #print(ph_pos_tokens, "\n++")
                #print(ph_tokens, "\n++")


    #if(re.search("^c", "tw_sentence")):
        #print(tw_sentence)

