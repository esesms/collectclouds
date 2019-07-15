import inflect

inflect = inflect.engine()

foods = ["strawberries", "apple", "banana pancake", "pineapple"]

for food in foods:
    if inflect.singular_noun(food) is False:
        food = inflect.plural(food)
        print(food)
    else:
        print(food)

