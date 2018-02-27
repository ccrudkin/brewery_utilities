import pickle

cwd = 'C:/Users/ccrud/PycharmProjects/Brewery_Utilities'

try:
    hops_dict_file = open(cwd + '/Files/hops_dict.p', 'rb')  # open the file containing pickle data
    hops_prices = pickle.load(hops_dict_file)  # unpickle data as an object
    hops_dict_file.close()  # close file from read mode
except:
    hops_prices = {}

op = input('New hops or just checking the database? Type "new" or "check": ')

if op == 'new':
    lp = True
    while lp:
        print()
        new_hops = input('New hops type: ')
        new_hops_price = input('New hops price per pound (before shipping): ')

        hops_prices[new_hops.lower()] = round(float(new_hops_price) * 2.20462 * 1.075, 2)
        # Convert to $/kg, then add 7.5% for shipping (about $15 for a $200 order)

        hops_dict_file = open(cwd + '/Files/hops_dict.p', 'wb')  # open file again in write mode. Trouble with 'wb+'
        pickle.dump(hops_prices, hops_dict_file)  # pickle the dictionary with new entry
        hops_dict_file.close()  # always close files

        print()
        another = input('Add another type? (Type Y/N): ')
        if another.lower() == 'n':
            lp = False

print()
for entry in hops_prices:
    s = 20 - len(entry)
    print(entry.capitalize(), ' ' * s, hops_prices[entry])
