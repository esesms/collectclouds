#Sue Huang
#03/13/19
#uses the food python library
#drag the .py and .db files into env/lib/PythonX/site-packages/
#https://think.cs.vt.edu/corgis/python/food/food.html




import food
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

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
    print(words)


#we will search for what "clouds taste like" in the twitter data and if something in the string is equivalent to portions of string from description, then we will count that as an ingredient for the ice cream