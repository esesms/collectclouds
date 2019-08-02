#Sue Huang
#07/15/19
#v1.0
#This program:
#reads text from a text file
#runs regex on the sentences to extract matches

from nltk.tokenize import sent_tokenize
import re

file = open("twitter_text2.txt", "r", encoding="utf-8")

text = file.read()

sentences = []
matched_words = []

#search_words = ['Kleenex']
#search_words = ['kleenex', 'environment', 'acid rain', 'pollution', 'metallic', 'mineral']
search_words = ['rainbow', 'cotton','sunshine', 'smoke', 'sun','acid rain', 'dirty', 'air quality', 'system', 'asbestos', 'asthma', 'automobile', 'beach pollution', 'bed bugs', 'carbon footprint calculator', 'carbon monoxide', 'cars', "children's health", 'citizen science','clean air act', 'clean water act', 'cleanups', 'climate change', 'coal ash', 'coalbed mine methane', 'coastal communities and climate change', 'community environmental resources', 'air pollutants', 'drinking and ground water', 'risk assessment', 'emergency preparation', 'drinking water contaminants', 'drinking water', 'drinking water sources', 'earth day', 'emissions trading programs', 'endangered species protection', 'endocrine system disruptors', 'energy star', 'report environmental violations', 'environmental justice', 'ethylene oxide', 'everglades', 'federal green challenge', 'federal insecticide', 'fish and shellfish', 'fracking', 'freedom of information act', 'fuel economy', 'global warming', 'glyphosate', 'gold king mine spill', 'monitoring', 'greenhouse gases', 'emissions', 'hazardous air pollutants', 'hazardous waste', 'haze', 'health', 'health research', 'health topics', 'homeland security', 'hurricanes', 'vehicles', 'engines', 'indoor air quality', 'volatile organic compounds', 'vocs', 'insect repellents', 'ddt','land and waste management research', 'land revitalization program', 'landfills', 'landfill methane outreach program', 'land, waste, and cleanup topics', 'lead', 'air pollution', 'lean practices', 'air toxics standards', 'mercury', 'mining', 'mold', 'mosquitoes', 'national water program', 'natural disasters preparation and response', 'natural gas star program', 'nitrogen dioxide air pollution', 'nitrogen dioxide air designations', 'nonpoint source pollution', 'nutrient pollution', 'ocean dumping act', 'oceans and coasts', 'acidification', 'ozone', 'ozone air pollution', 'ozone air designations', 'ozone and particulate matter', 'ozone layer depletion', 'ozone pollution and health', '', 'particulate matter', 'particulate matter','pcbs', 'pest management', 'pesticides', 'advisory committees, pesticide', 'biopesticides', 'food and pesticides', 'pests and pesticides','radiation monitoring', 'radiation protection', 'radon', 'recycling', 'regulations', 'renewable energy', 'renewable fuel', 'septic tanks', 'sewage sludge', 'soak up the rain campaign', 'soil fumigants', 'sulfur dioxide', 'superfund','sustainable','tribal resources','environmental programs', 'urban air', 'motor vehicles', 'wetlands','acid', 'rain', 'exposure', 'guideline','epa', 'agricultural','air', 'monitoring', 'pollution', 'emissions','waste', 'carbon', 'footprint','monoxide', 'cars', 'science', 'chemicals','energy','contaminated','sustainable', 'cleanup', 'chemtrail','climate', 'change', 'adaptation','land-use','coal', 'ash', 'coalbed', 'mine', 'methane', 'superfund', 'hazardous', 'pollutants', 'pollutant', 'earth','greenhouse', 'gas', 'ethylene', 'oxide', 'oxygen','scientific','fracking', 'hydraulic','vehicle', 'co2', 'fuels', 'gasoline','warming','organic','natural', 'disasters', 'nitrogen', 'dioxide','ocean', 'dumping', 'oceans', 'coasts', 'acidification', 'industry', 'ozone', 'particulate', 'matter', 'pcbs', 'polychlorinated', 'biphenyls', 'polyfluoroalkyl', 'pfoa', 'pfos', 'pfass', 'pest', 'pesticide', 'analytical', 'stewardship', 'pesp', 'motor','conservation','storm','mines', 'navajo', 'urban', 'toxic', 'toxin', 'toxins', 'vapor', 'warm', 'kleenex']

#tokenizes according to sentences
tw_sentence_tokens = sent_tokenize(text)
counter = 0
#iterates through the sentence tokens
for tw_sentence in tw_sentence_tokens:

    #if any(word in tw_sentence for word in search_words):
    #match = re.search(r"[^\.\!\?\n]*(?:[Tt]aste.?\W+(?:\w+\W+){0,2}?[Ll]ike[\s][Cc]loud.?|[Cc]loud.?\W+(?:\w+\W+){0,2}?[Tt]aste.?\W+(?:\w+\W+){0,2}?[Ll]ike.?\W+(?:\w+\W+))[^\.\!\?\n]*", tw_sentence)

    #if not match:
    for word in search_words:
        tw_sentence = tw_sentence.lower()
        match = re.search(r'[^@\w+][\w+\W+]*' + word + '[^@]*', tw_sentence)
        #match = re.search(word, tw_sentence)


        if match:
            print("Match!")
            if word not in matched_words:
                matched_words.append(word)

            prev = tw_sentence_tokens[counter-1]
            prev = prev.lower()

            #next = tw_sentence_tokens[counter+1]
            #next = next.lower()

            clean_prev = re.sub('@[^\s]*|co/[^\s]*|ly/[^\s]*|#[^\s]*|http://[^\s]*|https://[^\s]*|\"[^\s]*', '', prev)
            clean_prev = clean_prev.lstrip()
            clean_match = re.sub('@[^\s]*|co/[^\s]*|ly/[^\s]*|#[^\s]*|http://[^\s]*|https://[^\s]*|\"[^\s]*', '', match.group())
            clean_match = clean_match.lstrip()
           # clean_next = re.sub('@[^\s]*|co/[^\s]*|ly/[^\s]*|#[^\s]*|http[^\s]*|\"[^\s]*', '', next)
            #clean_next = clean_next.lstrip()

            print("1: ", clean_prev)
            print("2: ", clean_match)
            #print("3: ", clean_next)
            print("\n")

    counter += 1

print(matched_words)