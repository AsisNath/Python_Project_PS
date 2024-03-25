# use of dictionary {key, value} and list
# dictionary is multiple list or list of list
# it can be useful where you don't need to track based on array/list index
# in this case index is key which is human-readable can be meaningfully name instead of index 0123..
menus = {'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
         'Launch': ['BLT', 'PB&J', 'Turkey Sandwich'],
         'Dinner': ['Soup', 'Salad', 'Taco']}

print("List of food in the manus:")
for name, food in menus.items():
    print(name, ":", food)
