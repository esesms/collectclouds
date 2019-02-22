# Sue Huang
# 01/12/2019
# Searches twitter results file for foods


import re
#contents = file.read() #read the file into a string variable

search = input("Enter foods you want to search for (separate with commas): ")
search = [word.strip(' ') for word in search.lower().split(",")]

count = dict.fromkeys(search, 0)

file = open("twitter_text.txt", "rt") #reading text
#for line in file:
#    for word in line.lower().split():
#       if word in count:
#           count[word] += 1
contents = file.read()

print(contents)

for word in count:
    phrase = word #set each word in the count dictionary to phrase
    print(phrase) #print out the phrase
    
    result = re.findall(r'\b' + phrase + 's?', contents, re.IGNORECASE) #search for phrase in the content string
    print(result) #print out result each time phrase is found
    
    #should add something to ignore results that are preceded by "don't taste like"
    
    result_count = len(result) #get number of times phrase is found
    count[word] = result_count #set each word being searched for to the number of times it is found
            
file.close() #close the file
print(count)


#for large files, read in line by line
#with open('twitter_text.txt', 'rt') as file:
#    for line in file:
#        print (line)
