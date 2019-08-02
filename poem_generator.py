import random
import pyphen
from nltk.corpus import cmudict
from nltk.tokenize import sent_tokenize, word_tokenize
import time


#Modifiers to describe clouds: cloud_mods
cloud_mods = ['lemonade clouds', 'New York City clouds', 'unicorn clouds', 'fall clouds', 'absorbing the dew clouds', 'strawberry clouds', 'howdy clouds', 'azure clouds', 'chocolate fudge clouds', 'fluffy clouds', 'marshmallow clouds', 'rain clouds', 'warm sugar clouds', 'dream clouds', 'puffy clouds', 'divine clouds', 'mini clouds', 'little sweet clouds', 'spicy clouds', 'pink clouds', 'emperor\'s clouds', 'chocolate covered clouds', 'sick clouds', 'mint-flavored clouds', 'space clouds', 'rain clouds', 'violet storm clouds', 'dirty clouds', 'little peppermint clouds', 'sunset clouds', 'pillow clouds', 'magical banana clouds', 'silver lining of clouds', 'chocolate clouds', 'clouds of disappointment', 'honey suckle heaven clouds', 'arnold palmer flavored clouds', 'salty clouds', 'mushroom clouds', 'dark clouds', 'caramelized clouds', 'angel clouds', 'sea clouds', 'delicious puffy clouds', 'purple clouds', 'dust clouds in space clouds', 'them long leg amazon clouds', 'white clouds', 'fart clouds', 'smiley clouds', 'succulent rainbow clouds', 'flat clouds', 'clouds of goodness', 'delicious sun cotton clouds', 'crispy clouds', 'white syrup clouds', 'grey clouds', 'big, billowy, soupy clouds', 'wispy clouds', 'storm clouds', 'sugar coated clouds', 'buttery clouds', 'spinach clouds', 'hot clouds', 'cloud of obligation', 'crispy clouds', 'non-acid rain clouds', 'aha clouds', 'evening clouds', 'stormy clouds', 'low cumulus nimbus kind of clouds', 'iron colored clouds', 'clouds of webbed memories', 'inhaled clouds', 'the dust cloud at the center of the galaxy', 'galactic dust clouds', 'white', 'grey', 'pink', 'salty', 'crispy']

#Modifiers to describe tastes: taste_mods (taste)
taste_mods = ['delicious', 'frosted', 'satanic', 'sweet, yet tasteless', 'metallic', 'salty', 'acrid', 'dirty', 'disappointing', 'sweet', 'sour', 'yummy', 'light', 'fluffy', 'really sweet', 'sour', 'cold and juicy', 'stormy', 'crystalline', 'a little dusty']

#Taste nouns: taste_nouns (taste like)
taste_nouns = ['sunlight', 'wonders of words n truth', 'little bit of heaven', 'sugar cookies', 'cotton candy', 'whipped cream', 'vanilla ice cream', 'tinfoil', 'Jesus', 'nothing', 'meat', 'purple grape jolly ranchers', 'potatoes', 'mashed potatoes', 'Milano cookies', 'giant marshmallow peeps', 'marshmallows', 'Airhead mystery flavor', 'love', 'ambrosial atmosphere', 'an air of awe', 'elf spit', 'burnt sugar', 'wire made of nothing at all', 'water', 'cakes', 'cheesecake bars', 'Starbucks eggs', 'Denny\'s flapjacks', 'fart flavored candy floss', 'cherries', 'air', 'water', 'sewage water', 'nazi tears', 'water', 'evaporated words', 'ristretto', 'spring water', 'cotton', 'sourdough cinnamon rolls', 'pb n creme puffers', 'Uncrustables', 'fog tea lattes', 'krispy kreme donuts', 'rice cakes', 'smores', 'silverware', 'silverfish', 'cold bran flakes', 'rain', 'moonbeams dipped in liquid confections', 'raspberry beignets', 'blue curacao', 'vanilla', 'Kit Kats', 'Kleenex', 'Halloween candy', 'lakes', 'dental floss', 'CO2', 'peaches', 'a nice glass of chocolate milk', 'snow cones', 'ice green tea', 'mommies', 'not Katy Perry', 'raspberry rum', 'air', 'strawberry cream savers', 'clotted cream flavored ice cream', 'tea', 'shaved ice', 'icing', 'homemade vanilla marshmallows', 'sour cream', 'angeled eggs', 'candy cane viva puffs', 'hot chocolate', 'cinnamon', 'rice krispy treats',  'original glazed donuts', 'strawberry cupcakes', 'blueberry flavored water', 'coconuts', 'acidic water', 'smoke', 'pudding', 'blossom rolls', 'french vanilla', 'farts from God', 'snowballs', 'smog', 'meringues', 'sno-cones', 'pillows', 'butter', 'lucky charms', 'peas', 'rainbows dipped in ethereal chocolate dreams', 'Trader Joe\'s pomegranate Pop Tarts', 'double-whipped cream cheese', 'honey', 'Twinkies', 'oily joosey succulent beef patties', 'pancakes', 'marshmallow fluff', 'macarons', 'Pureau', 'avocados', 'tap water', 'Fiji water', 'Jake\'s Chinese Buffet rolls', 'Buvette\'s steamed eggs', 'cookies from the Netherlands', 'cotton balls', 'freezing cotton candy', 'circus peanuts', 'ham', 'Cheesecake Factory mashed potatoes', 'pink n white marshmallows', 'dominoes', 'tissues', 'ketchup', 'wedding meringues', 'miso soup', 'fairy floss', 'potato cakes', 'cool, cool taste of Laramie cigarettes', 'roast potatoes', 'fresh bread', 'vanilla frosty\'s', 'her lips', 'pumpkin butter pancakes', 'her pussy', 'wonka\'s millionaire shortbread', 'bar dumplings', 'crescent rolls', 'garlic butter in mashed taters', 'unicorns', 'voss water', 'mama waz\'s homemade mashed potatoes', 'chicken', 'Cassie\'s coochie', 'whips yogurt', 'quaker rice crackers', 'Nutella', 'milk', 'jello', 'coconut gelato', 'snow', 'snails', 'Magnum ice cream', 'turnips', 'fried apples', 'toilet tissue', 'Hawaiian sweet rolls', 'mini powdered donuts', 'fresh mozzarella', 'kolaches from Shipley\'s', 'skittles', 'lemons and sugar', 'smart water', 'mist', 'acid rain', 'a sultry yellow flavor', 'with a smell like birch','Oreos with pink frosting', 'fried Oreos', 'McDonald\'s ice cream', 'floss marshmallows', 'fancy-pants chocolate', 'with blueberries and sea salt embedded', 'water vapour', 'roasted red potatoes', 'limes', 'salt', 'pillsbury cookies', 'clementines', 'heaven', 'fluffy deliciousness', 'Dr. Pepper', 'scrambled eggs cooked on low heat with milk and butter', 'pina colada', 'vanilla beans', 'salt', 'oyster sauce', 'napkins', 'her skin', 'mints', 'grapes', 'steam from a moroccan bath', 'lemon flavored cotton candy', 'white hot chocolate', 'Cold Stone', 'M&M\'s', 'holiday pie at McDonald\'s', 'buttercream cupcakes', 'soft ice', 'clean-ex', 'lollipops', 'the tobacco from France', 'glorious cigarettes', 'fresh vanilla', 'burnt Demerara sugar', 'shit', 'zebra cakes', 'airplane engine oil', 'cigarette smoke', 'the brownies my aunt\'s boyfriend makes', 'cotton candy Dippin Dots', 'cotton candy ponies', 'rainbows', 'unicorns', 'elves', 'chocolate rain', 'ponies', 'whipahol', 'spagbol', 'maple nut Cliff bars', 'cheese', 'the angels cry sprite', 'icing sugar', 'red lobster biscuits', 'fruit', 'cobwebs', 'mangos', 'the past', 'hot fudge sundae', 'maple cream cheese frosting', 'sugar', 'white cake mix cookies', 'grape icees', 'nestle pure life water', 'elemental', 'chips', 'porridge', 'ice cream', 'not eggs', 'pitas at Pita Pit', 'that thang', 'vitamin water', 'lee pound cakes', 'bubble gum', 'wine', 'wet dog', 'strawberry Jello/Cool Whip combo', 'popcorn', 'donuts', 'white cheddar corn puffs', 'sheep', 'Reese\'s cups', 'watermelon Arizona', 'a hint of pollution', 'blue moon ice cream', 'soft lettuce', 'dirty water', 'Beyonce\'s bath water', 'fairy floss grace', 'foam', 'my vegan dumplings', 'flan', 'rain', 'drinking a puddle', 'candies', 'cream puffs', 'Ramos gin fizz', 'pumpkin chocolate chip cookies', 'cocktails', '3 Musketeers bars', 'mercury', 'rice', 'chipmunks', 'scrambled eggs', 'gold clouds served on a plate full of ecstasy', 'cold & flu tablets', 'pseudoephedrine', 'morphine', 'strawberry marshmallows', 'rose and dat diamond of bottle ace shit', 'watermelon', 'good looking Japanese girls', 'Ciroc', 'damp sky', 'pierogis', 'snow', 'da production of rain', 'Kool-Aid', 'lemons', 'sweeties', 'cousin vinny\'s breadsticks', 'the new Flintstone\'s cupcake cereal', 'Cool Whip', 'milk candy floss', 'kush', 'sprite', 'Sara Lee soft bread', 'pao queijou from rotiboy', 'metal', 'medicine', 'peanut butter', 'Madagascar vanilla', 'ros\xe9', 'almonds', 'happiness', 'joy', 'cherry bubblegum', 'God beer', 'angel wings', 'fuzz', 'butter', 'tears', 'salt', 'cucumber', 'cool well water on a hot summer day', 'a little contaminated but refreshing', 'tuna casserole', 'dirrrrty particles of water', 'triple cream brie', 'funfetti cupcakes', 'gnocchi', 'omelets', 'blobby sloppy snowflakes', 'whipped rain', 'scrambled egg whites', 'jerk chicken', 'potato salad', 'hotcakes', 'lime skittles', 'steamed pork buns', 'steamed shrimp buns', 'Mya pussy', 'Ri Ri pussy']

#Extra phrases:
extras = ['i tasted \'em', 'out the window', 'take a spoon', 'taste these silky peaks', 'crackle on your tongue', 'like ozone', 'out the plane windows', 'chew on tissues', 'clouds like couches', 'I want to fly', 'and then i cry', 'i will never know', 'i wish i could fly', 'fly like Peter Pan', 'so i could lie down on clouds and taste them', 'fly higher then james will lick the clouds', 'lick the plane\'s window', 'lick the clouds Jamesy', 'looking out the window', 'get in my belly!', 'airline trip side venture', 'high mercury levels', 'the silver lining', 'butterflies laughing', 'clouds', 'like','that ish is delicious', 'mmmm', 'look', 'head so high', 'wow!', 'lick']

#Questions:
questions = ['clouds', 'oh clouds', 'about clouds', 'wonder', 'not clowns', 'just like','clouds taste like', 'these clouds taste like', 'what do clouds taste like?', 'what do they taste like?']


p = pyphen.Pyphen(lang='en_US')
d = cmudict.dict()
cloud_mods_dict = {}
taste_mods_dict = {}
taste_nouns_dict = {}
extras_dict = {}
questions_dict = {}
poem_counter = 0


def syllable_counter(content):
    counter = 0

    content = content.replace("-", " ")
    #content = content.replace("\'", "")
    content = content.replace(",", "")
    content = content.replace("?", "")
    #print("\n" + content)

    word_list = word_tokenize(content)

    for word in word_list:
        try:
            if "\'s" in word:
                counter -= 1
            lower_word = d[word.lower()]
            for phonemes in lower_word[0]:
                for phoneme in phonemes:
                    if any(x.isdigit() for x in phoneme):
                        counter += 1
            if word == 'mmmm':
                syllables = 1
                counter = syllables
            elif word == "Dr.":
                syllables = 2
                counter = syllables
        except KeyError:
            if word == "CO2":
                syllables = 3
            elif word == "Nutella":
                syllables = 3
            elif word == "gelato":
                syllables = 3
            elif word == "coconut":
                syllables = 3
            elif word == "miso":
                syllables = 2
            elif word == "icees":
                syllables = 2
            elif word == "pseudoephedrine":
                syllables = 5
            else:
                syllables = len(p.positions(word)) + 1
            #print(word, syllables)
            counter = counter + syllables

    return counter

for content in cloud_mods:
    counter = syllable_counter(content)
    cloud_mods_dict[content] = counter
    #print(counter, "syllables")

print(cloud_mods_dict)

for content in taste_mods:
    counter = syllable_counter(content)
    taste_mods_dict[content] = counter

print(taste_mods_dict)

for content in taste_nouns:
    counter = syllable_counter(content)
    taste_nouns_dict[content] = counter

print(taste_nouns_dict)

for content in extras:
    counter = syllable_counter(content)
    extras_dict[content] = counter

print(extras_dict)

for content in questions:
    counter = syllable_counter(content)
    questions_dict[content] = counter

print(questions_dict)

"""
while ln1_remainder > 0:
    random_key = random.choice(list(questions_dict.keys()))
    #print(random_key)

    if questions_dict[random_key] <= ln1_remainder:
        haikuA = random_key
        if "?" in random_key:
            if questions_dict[random_key] == ln1_remainder:
                print(haikuA)
            else:
                print(haikuA, end=" ")
        else:
            if questions_dict[random_key] == ln1_remainder:
                print(haikuA)
            else:
                print(haikuA + ",", end=" ")
        ln1_remainder = ln1_remainder - questions_dict[random_key]
        #print(remainder)
    else:
        ln1_remainder = ln1_remainder
"""
file = open("poems.txt", "a")

while poem_counter < 3:
    rand = random.randint(1,3)
    print("Rand", str(rand), "\n")

    haikuA_sum = ''
    haikuB_sum = ''
    haikuC_sum = ''

    ln1_remainder = 5
    ln2_remainder = 7
    ln3_remainder = 5

    while ln1_remainder > 0 and rand is 1:
        random_key = random.choice(list(questions_dict.keys()))
        if questions_dict[random_key] <= ln1_remainder:
            haikuA = random_key

            if "?" in random_key:
                if questions_dict[random_key] == ln1_remainder:
                    print(haikuA)
                    haikuA_sum = haikuA_sum + " " + haikuA
                else:
                    print(haikuA, end=" ")
                    haikuA_sum = haikuA_sum + " " + haikuA
            else:
                if questions_dict[random_key] == ln1_remainder:
                    print(haikuA)
                    haikuA_sum = haikuA_sum + " " + haikuA
                else:
                    haikuA = haikuA + ","
                    print(haikuA, end = " ")
                    haikuA_sum = haikuA_sum + " " + haikuA
            ln1_remainder = ln1_remainder - questions_dict[random_key]
            #print(remainder)
        else:
            ln1_remainder = ln1_remainder


    while ln1_remainder > 0 and rand is 2:
        random_key = random.choice(list(extras_dict.keys()))
        if extras_dict[random_key] <= ln1_remainder:
            haikuA = random_key
            if "?" in random_key or "!" in random_key:
                if extras_dict[random_key] == ln1_remainder:
                    print(haikuA)
                    haikuA_sum = haikuA_sum + " " + haikuA
                else:
                    print(haikuA, end=" ")
                    haikuA_sum = haikuA_sum + " " + haikuA
            else:
                if extras_dict[random_key] == ln1_remainder:
                    print(haikuA)
                    haikuA_sum = haikuA_sum + " " + haikuA
                else:
                    haikuA = haikuA + ","
                    print(haikuA, end=" ")
                    haikuA_sum = haikuA_sum + " " + haikuA
            ln1_remainder = ln1_remainder - extras_dict[random_key]
            #print(remainder)
        else:
            ln1_remainder = ln1_remainder


    while ln1_remainder > 0 and rand is 3:
        random_key = random.choice(list(cloud_mods_dict.keys()))
        if cloud_mods_dict[random_key] <= ln1_remainder:
            haikuA = random_key
            if "?" in random_key:
                if cloud_mods_dict[random_key] == ln1_remainder:
                    print(haikuA)
                    haikuA_sum = haikuA_sum + " " + haikuA
                else:
                    print(haikuA, end=" ")
                    haikuA_sum = haikuA_sum + " " + haikuA
            else:
                if cloud_mods_dict[random_key] == ln1_remainder:
                    print(haikuA)
                    haikuA_sum = haikuA_sum + " " + haikuA
                else:
                    haikuA = haikuA + ","
                    print(haikuA, end=" ")
                    haikuA_sum = haikuA_sum + " " + haikuA
            ln1_remainder = ln1_remainder - cloud_mods_dict[random_key]
            #print(remainder)
        else:
            ln1_remainder = ln1_remainder


    rand2 = random.randint(1,2)

    while ln2_remainder > 0 and rand is not 3:
        if ln2_remainder == 7 and rand2 == 1:
            haikuB_lead = "taste like"
            print(haikuB_lead, end = " ")
            haikuB_sum = haikuB_lead
            ln2_remainder = 5
        random_key = random.choice(list(taste_nouns_dict.keys()))
        if taste_nouns_dict[random_key] <= ln2_remainder:
            haikuB = random_key
            if taste_nouns_dict[random_key] == ln2_remainder:
                print(haikuB)
                haikuB_sum = haikuB_sum + " " + haikuB
            else:
                haikuB = haikuB + ","
                print(haikuB, end=" ")
                haikuB_sum = haikuB_sum + " " + haikuB
            ln2_remainder = ln2_remainder - taste_nouns_dict[random_key]
            #print(remainder)
        else:
            ln2_remainder = ln2_remainder


    while ln2_remainder > 0 and rand is 3:
        if ln2_remainder == 7 and rand2 == 1:
            haikuB_lead = "these clouds taste like"
            print(haikuB_lead, end = " ")
            haikuB_sum = haikuB_lead
            ln2_remainder = 3
        elif ln2_remainder == 7 and rand2 == 2:
            haikuB_lead = "they taste like"
            print(haikuB_lead, end=" ")
            haikuB_sum = haikuB_lead
            ln2_remainder = 4
        random_key = random.choice(list(taste_nouns_dict.keys()))
        if taste_nouns_dict[random_key] <= ln2_remainder:
            haikuB = random_key
            if "?" in random_key:
                if taste_nouns_dict[random_key] == ln2_remainder:
                    print(haikuB)
                    haikuB_sum = haikuB_sum + " " + haikuB
                else:
                    print(haikuB, end=" ")
                    haikuB_sum = haikuB_sum + " " + haikuB
            else:
                if taste_nouns_dict[random_key] == ln2_remainder:
                    print(haikuB)
                    haikuB_sum = haikuB_sum + " " + haikuB
                else:
                    haikuB = haikuB + ","
                    print(haikuB, end=" ")
                    haikuB_sum = haikuB_sum + " " + haikuB
            ln2_remainder = ln2_remainder - taste_nouns_dict[random_key]
            #print(remainder)
        else:
            ln2_remainder = ln2_remainder


    while ln3_remainder > 0 and rand is not 3:
        random_key = random.choice(list(taste_nouns_dict.keys()))
        if taste_nouns_dict[random_key] <= ln3_remainder:
            haikuC = random_key
            if taste_nouns_dict[random_key] == ln3_remainder:
                print(haikuC)
                haikuC_sum = haikuC_sum + " " + haikuC
            else:
                haikuC = haikuC + ","
                print(haikuC, end=" ")
                haikuC_sum = haikuC_sum + " " + haikuC
            ln3_remainder = ln3_remainder - taste_nouns_dict[random_key]
            #print(ln3_remainder)
        else:
            ln3_remainder = ln3_remainder

    rand3 = random.randint(1,3)

    while ln3_remainder > 0 and rand is 3:
        if ln3_remainder == 5 and rand3 == 1:
            haikuC_lead = "they taste"
            print(haikuC_lead, end = " ")
            haikuC_sum = haikuC_lead
            ln3_remainder = 3
        elif ln3_remainder == 5 and rand3 == 2:
            haikuC_lead = "taste"
            print(haikuC_lead, end=" ")
            haikuC_sum = haikuC_lead
            ln3_remainder = 4
        random_key = random.choice(list(taste_mods_dict.keys()))
        if taste_mods_dict[random_key] <= ln3_remainder:
            haikuC = random_key
            if "?" in random_key:
                if taste_mods_dict[random_key] == ln3_remainder:
                    print(haikuC)
                    haikuC_sum = haikuC_sum + " " + haikuC
                else:
                    print(haikuC, end=" ")
                    haikuC_sum = haikuC_sum + " " + haikuC
            else:
                if taste_mods_dict[random_key] == ln3_remainder:
                    print(haikuC)
                    haikuC_sum = haikuC_sum + " " + haikuC
                else:
                    haikuC = haikuC + ","
                    print(haikuC, end=" ")
                    haikuC_sum = haikuC_sum + " " + haikuC
            ln3_remainder = ln3_remainder - taste_mods_dict[random_key]
            #print(remainder)
        else:
            ln3_remainder = ln3_remainder

    #clean white spaces
    haikuA_sum = haikuA_sum.lstrip()
    haikuB_sum = haikuB_sum.lstrip()
    haikuC_sum = haikuC_sum.lstrip()

    haiku_sum = haikuA_sum + "\n" + haikuB_sum + "\n" + haikuC_sum
    file.write(haiku_sum + "\n\n")
    #file.write(str((tweets[1]).all_text))

    poem_counter = poem_counter + 1
    print(poem_counter)

    time.sleep(2)

file.close()

