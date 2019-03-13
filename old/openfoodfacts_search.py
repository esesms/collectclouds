#Sue Huang
#03/08/19
#go to https://ndb.nal.usda.gov/ndb/doc/# and apply for API key

#from usda import UsdaClient
#client = UsdaClient('9MIxZYmEic0aFcWRDwM5AWuejcy2sJU1hOqQKOXS')

#foods_list = client.list_foods(5)
#for _ in range(5):
 #   food_item = next(foods_list)
 #   print(food_item.name)

#run install according to https://github.com/openfoodfacts/openfoodfacts-python
#references here https://github.com/openfoodfacts/openfoodfacts-python/blob/master/docs/Usage.md
import openfoodfacts


#allergens option
#allergens = openfoodfacts.facets.get_allergens()

#returns milk
#print(allergens[0]) 


#categories = openfoodfacts.facets.get_categories()

#accesses dictionary categories, key url
#print(categories[0])

#for category in categories:
#    for key, value in category:
#        print(key + value)

#print(isinstance(categories,list))
#print(isinstance(categories,tuple))
#print(isinstance(categories,dict))

#for a list of dictionaries, print the name in each category list item
#for category in categories:
    #name = category['name']
    #print(name)
    #print only the english categories
    #if(name.startswith("en:")):
        #en_cat = name
        #print(en_cat)
    #if not name.startswith("fr:") and not name.startswith("ru:") and not name.startswith("pt:") and not name.startswith("es:"):
    #if not ":" in name:
        #en_cat = name
        #print(en_cat)
        #if "marshmallow" in en_cat:
            #print(en_cat)

ingredients = openfoodfacts.facets.get_ingredients()
#print(isinstance(ingredients,list))
#print(isinstance(ingredients[0],dict))

for ingredient in ingredients:
    print(ingredient)
    

#if(ingredients[0]["languages_tags"] == "en:english")
#   print("true")
#search if language is in english
#for key in ingredients[0]["languages_tags"]:
    #print(key)
    #if(key == "en:english"):
        #print("This contains english")

#categories = openfoodfacts.facets.get_categories()