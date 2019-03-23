#Sue Huang
#03/13/19
#uses the food python library USDA
#searches the food library for all descriptions
#makes them lowercase and word tokenizes them


#drag the .py and .db files into env/lib/PythonX/site-packages/
#https://think.cs.vt.edu/corgis/python/food/food.html
#download sqlite browser to view db of food




import food
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from itertools import permutations #to iterate through lists in permutations and combinations

#list_of_report is a list of dictionaries
list_of_report = food.get_reports()

#for key in list_of_report:
    #print(key)
#print(isinstance(list_of_report,list))
#print(isinstance(list_of_report[0],dict))

#for food in list_of_report:
    #category = food["Category"]
    #print(category)
        
for food in list_of_report:
    description = food["Description"].lower() #converts everything to lower case
    tokens = word_tokenize(description)
    words = [word for word in tokens if word.isalpha()] #removes commas
    #do a replacement of abbreviations with full words for example inst with instant and whl with whole
    #print(words)
    for word in words:
        if word == "pudding":
            min_perm = 1
            max_perm = 3
            wd_permutations = []
            for x in range(min_perm, max_perm):
                for y in permutations(words, x):
                    wd_permutations.append(y)
            #wd_permutations = permutations(words, 2)
            wd_permutation_list = list(wd_permutations)
            print(wd_permutation_list)
            #print(type(wd_permutation_list))


#we will search for what "clouds taste like" in the twitter data and if something in the string is equivalent to portions of string from description, then we will count that as an ingredient for the ice cream