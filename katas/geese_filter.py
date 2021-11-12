# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python

"""
Write a function, gooseFilter / goose-filter / goose_filter / GooseFilter, 
that takes an array of strings as an argument and returns a filtered array 
containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:
 goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
 goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]),["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
 goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]),[])
"""

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    salida = []
    for ave in birds:
        if not ave in geese:
            salida.append(ave)
    return salida

