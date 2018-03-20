import re
import string
import operator
frequency = {}
text = "Dandelion | Define Dandelion at Dictionary.comdandelion Meaning in the Cambridge English DictionaryVisually similar imagesTaraxacum - WikipediaAutosomal DNA, Ancient Ancestors, Ethnicity and the Dandelion ...Common Dandelion - Taraxacum tenejapense A.J. Richards - Details ...Adrenals Burned Out? Try Dandelion Coffee - Healthy Home EconomistCommon Dandelion"
text_string = text.lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string) #setting the parameter
# finding the most repeated word
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1    
frequency_list = frequency.keys()
#printing the word with most frequency
print(max(frequency.keys(), key=(lambda k: frequency[k])))