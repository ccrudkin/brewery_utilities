# TODO: Update all files in working directory to reflect current recipes and generate accurate reports.

import re
import pickle
import os

filepath = 'C:/Users/ccrud/PycharmProjects/Brewery_Utilities/Files/production_recipes/'
filenames = os.listdir(filepath)

for filename in filenames:
    print()
    print('Recipe file: {}'.format(filename))
    print()
    file_locator = filepath + filename

    with open(file_locator) as file:
        recipe_text = file.read()

    grain_dict_file = open('C:/Users/ccrud/PycharmProjects/Brewery_Utilities/Files/grain_dict.p', 'rb')
    malt_types = pickle.load(grain_dict_file)  # unpickle data as a variable
    grain_dict_file.close()  # close file from read mode

    hops_dict_file = open('C:/Users/ccrud/PycharmProjects/Brewery_Utilities/Files/hops_dict.p', 'rb')
    hop_types = pickle.load(hops_dict_file)
    hops_dict_file.close()

    m_consumables = {  # Dollars per unit.
        'yeast': 25,  # per pitch
        'PBW': 3,  # per pound
        'Biofine': 16.25  # per liter
        }

    grain_re = re.compile(r'(\d+\.?\d*)(\s+)(kg|g)')
    hops_re = re.compile(r'(\d+\.?\d*)(\s+)(g)')

    lines = recipe_text.split('\n')

    malt = []
    hops = []


    def find_malt(recipe):
        for line in recipe:
            for type in malt_types:
                if type in line.lower():  # Price dictionary is all lower case, same for hops below.
                    malt.append([line, malt_types[type]])


    def find_hops(recipe):
        for line in recipe:
            for type in hop_types:
                if type in line.lower():
                    hops.append([line, hop_types[type]])


    def amount_of_ingredient(item, l):
        if l == malt:
            q = grain_re.search(item)
            if q.group(3) == 'kg':
                return float(q.group(1))
            elif q.group(3) == 'g':
                return float(q.group(1)) / 1000  # Return in kg.
        elif l == hops:
            q = hops_re.search(item)
            if q.group(3) == 'g':
                return float(q.group(1)) / 1000  # Return in kg.


    def ingredient_cost(l):
        total = 0
        for i in l:
            # print(i)
            amount = amount_of_ingredient(i[0], l)
            cost = amount * i[1]
            total += cost
        return total


    def total_cost(malt, hops):  # Returns total @ [0] and per keg @ [1] based on 5 kegs per batch.
        ingredients = ingredient_cost(malt) + ingredient_cost(hops)
        consumables = m_consumables['yeast'] + m_consumables['PBW'] * 2 + m_consumables['Biofine'] * .09
        total = ingredients + consumables
        return total, total / 5


    find_malt(lines)
    find_hops(lines)
    print('Malt cost:   ${}'.format(round(ingredient_cost(malt), 2)))
    print('Hops cost:   ${}'.format(round(ingredient_cost(hops), 2)))

    batch, keg = total_cost(malt, hops)

    print('Batch cost:  ${}'.format(round(batch, 2)))
    print('Keg cost:    ${}'.format(round(keg, 2)))
