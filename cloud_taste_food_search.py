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
import inflect

file = open("twitter_text2.txt", "r", encoding="utf-8")
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
stopwords.update(['n', 'na', 'new', 'vit', 'style', 'low', 'sprd', 'it\'s', 'dried', 'fungi', 'wonder', 'one', 'tongue', 'flavor', 'flavors', 'w', 'always', 'made', 'vegan', 'white', 'good', 'little', 'go', 'eye', 'end', 'delight', 'cloud', 'blue', 'back', 'without', 'warm', 'stuff', 'skin', 'right', 'real', 'past', 'outside', 'next', 'morning', 'hi', 'heart', 'head', 'gold', 'general', 'fr', 'eat', 'drink', 'big', 'baby', 'way', 'use', 'ultra', 'super', 'sub', 'start', 'soft', 'si', 'shaped', 'power', 'plus', 'part', 'old', 'november', 'mixed', 'meal', 'less', 'late', 'kit', 'game', 'kit', 'friends', 'eight', 'dog', 'deep', 'de', 'combination', 'blends', 'bear', 'animal', 'add', 'ear', 'kid', 'boy', 'oh', 'top', 'tree', 'side', 'shapes', 'prior', 'neck', 'mix', 'french', 'food', 'balls', 'young', 'wld', 'wash', 'user', 'types', 'type', 'store', 'southern', 'smart', 'slices', 'pods', 'plate', 'party', 'ones', 'lunch', 'leg', 'label', 'jo', 'item', 'inch', 'iced', 'higher', 'half', 'giant', 'g', 'foods', 'filling', 'filled', 'family', 'eyes', 'es', 'energy', 'dove', 'dogs', 'cup', 'cubes', 'cooking', 'child', 'christmas', 'character', 'ch', 'box', 'bowl', 'boo', 'black', 'bite', 'bar', 'b', 'arizona', 'rl', 'r', 'butt', 'mr', 'mt', 'pm', 'post', 'ross', 'x', 'touch', 'well', 'life', 'long', 'great', 'covered', 'year', 'spread', 'mini', 'straight', 'feet', 'weed', 'sea', 'sweet', 'fluffy', 'healthy', 'treats', 'light', 'snacks', 'fat', 'pink', 'cool', 'sunshine', 'rainbow', 'rolled', 'louis', 'sun', 'ground', 'mixture', 'home', 'full', 'summer', 'stars', 'star', 'recipe', 'la', 'ocean', 'hawaiian', 'chick', 'bright', 'blood', 'bit', 'bamboo', 'yellow', 'wrapped', 'women', 'winter', 'whole', 'vitamin', 'thick', 'smoked', 'slip', 'slice', 'silver', 'silk', 'serving', 'seeded', 'savory', 'restaurant', 'red', 'quick', 'quarters', 'proof', 'pound', 'popeyes', 'pockets', 'pillow', 'oscar', 'original', 'non', 'necks', 'moist', 'mediterranean', 'japanese', 'inside', 'includes', 'heat', 'hand', 'green', 'fun', 'form', 'done', 'art', 'adventure','break','beach','base','balance', 'brisk', 'baking'])

#stopwords below that are words part of multi word foods, stops only the individual words, not the multi word
stopwords2 = ['mashed', 'mash', 'colada', 'hot', 'whipped', 'whip', 'cold', 'fresh', 'vanilla ice', 'purple', 'moose', 'fried', 'edible', 'roll', 'rolls', 'wedding', 'soy', 'peanut', 'pop', 'homemade', 'blueberry', 'almond', 'vegetable', 'tap', 'tuna', 'sugared', 'straw', 'stone', 'spring', 'shake', 'sauce', 'rose', 'roasted', 'ricotta', 'puffed', 'powdered', 'pina', 'olive', 'oil', 'oat', 'mineral', 'maple', 'liquid', 'joy', 'grilled', 'greens', 'golden', 'goddess', 'glazed', 'frosted', 'fiji', 'dry', 'drop', 'double', 'dinner', 'desser', 'dark', 'cut', 'crunchy', 'crunch', 'crisp', 'chinese', 'chews', 'cheesy', 'buttery', 'bright', 'brand', 'bliss', 'apple', 'alcoholic','wasabi', 'cotton', 'lucky', 'seeds', 'flakes', 'tropical','chicken','drops', 'buds', 'bud', 'bakery', 'bites', 'cliff', 'coconut cotton', 'breakfast']

for food in list_of_report:
    description = food["Description"].lower() #converts everything to lower case
    tokens = word_tokenize(description)
    words = [word for word in tokens if word.isalpha() and word not in stopwords]


    #iterates through the food descriptions
    for word in words:

        #if food description contains certain words generate permutations of the description and append to the list

        #COMMENT OR UNCOMMENT BELOW AND CHANGE FOOD HERE TO LIMIT SEARCH IN DATABASE
        #if word == "peanut" or word == "cotton":
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

    #different regexes

    #broad search: regex to match whole phrases up to period boundaries that contain near terms taste(s) and cloud(sd)
    #match = re.search(r"[^\.\!\?\n]*(?:[Tt]aste.?\W+(?:\w+\W+){0,4}?[Cc]loud.?|[Cc]loud.?\W+(?:\w+\W+){0,4}?[Tt]aste.?)[^\.\!\?\n]*", tw_sentence) #only output sentences that have the phrase clouds taste like <food from database>

    #basic search: searches for food words within tw_sentence
    #match = re.search(r"[Cc]loud.?\W+(?:\w+\W+){0,4}?[Tt]aste.?(?:\w+\W+){0,4}?[Ll]ike[^.](?:\w+\W+)[^.]*", tw_sentence)

    # basic2 search: searches for food words within tw_sentence in two directions
    match = re.search(r"[^\.\!\?\n]*(?:[Tt]aste.?\W+(?:\w+\W+){0,2}?[Ll]ike[\s][Cc]loud.?|[Cc]loud.?\W+(?:\w+\W+){0,2}?[Tt]aste.?\W+(?:\w+\W+){0,2}?[Ll]ike.?\W+(?:\w+\W+))[^\.\!\?\n]*", tw_sentence) #only output sentences that have the phrase clouds taste like <food from database>

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

#get rid of words in the stopwords2 list
for word in stopwords2:
    if word in counter:
        del counter[word]

inflect = inflect.engine()

#for food in counter:
    #test if you can make the food singular, if it is already singular, will return false
    #if inflect.singular_noun(food) is False:
        #food = inflect.plural(food)
        #print(food)

pluralize_words = ["cocktail", "cookie", "strawberry", "raspberry", "grape", "cherry", "brownie", "tortilla", "sundae", "starburst", "peach", "oyster", "mushroom", "mashed potato", "jolly rancher", "hazelnut", "burrito", "banana"]

for word in pluralize_words:
    #if there is already a plural version of the word in the dictionary, get the value of the singular word and add it to the value of the plural word
    if inflect.plural(word) in counter.keys():
        counter[inflect.plural(word)] = counter[word] + counter[inflect.plural(word)]
        del counter[word]
    else:
        counter[inflect.plural(word)] = counter.pop(word)

counter["whipped cream"] = counter["whip cream"] + counter["whipped cream"]
del counter["whip cream"]


    #for food, count in counter.items():
        #if food == word:
            #counter[inflect.plural(word)] = counter.pop(food)

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
     percent = round(percent, 2)
     table.add_row([food, count, percent])

table.sortby = "Percent"
table.reversesort = True
print(table)

with open('taste_food_results_basic_2.txt', 'w') as w:
    w.write(str(table))