import pickle

cwd = 'C:/Users/ccrud/PycharmProjects/Brewery_Utilities'

try:
    grain_dict_file = open(cwd + '/Files/grain_dict.p', 'rb')  # open the file containing pickle data
    grain_prices = pickle.load(grain_dict_file)  # unpickle data as a variable
    grain_dict_file.close()  # close file from read mode
except:
    grain_prices = {}

op = input('New grain or just checking the dictionary? Type "new" or "check": ')

if op == 'new':
    lp = True
    while lp:
        print()
        new_grain = input('New grain type: ')
        new_grain_price = input('New grain price per pound (before milling or shipping): ')

        grain_prices[new_grain.lower()] = round((float(new_grain_price) + .05) * 2.20462 * 1.1, 2)
        # $.05 for milling, then convert to $/kg, then add 10% for shipping (about $150 for a $1500 order)

        grain_dict_file = open(cwd + '/Files/grain_dict.p', 'wb')  # open file again in write mode. Trouble with 'wb+'
        pickle.dump(grain_prices, grain_dict_file)  # pickle the dictionary with new entry
        grain_dict_file.close()  # always close files

        print()
        another = input('Add another type? (Type Y/N): ')
        if another.lower() == 'n':
            lp = False

print()
for entry in grain_prices:
    s = 20 - len(entry)
    print(entry.capitalize(), ' ' * s, grain_prices[entry])
