import os
import pandas as pd
import json

cwd = os.getcwd()
print(cwd)
os.chdir(cwd)

# reading BDO recipes .CSV file that contains the ingredients required for every recipe
file = pd.read_csv('recipes.csv')

recipes = {}

for i, row in file.iterrows():
    # each row is a recipe, making a list of each row and iterating through the contents of that row to get the ingredients.
    row_list = []
    for col in row:
        row_list.append(col)

    print(row_list)
    
    # I know the variable declarations are not necessary but it's for readbility.
    name = row_list[0]
    level = row_list[1]
    ing1 = row_list[2]
    ing1_amnt = row_list[3]
    ing2 = row_list [4]
    ing2_amnt = row_list[5]
    ing3 = row_list[6]
    ing3_amnt = row_list[7]
    # checking to see if ingredients exist past this point because not all recipes have this many ingredients.
    if row_list[8]:
        ing4 = row_list[8]
        ing4_amnt = row_list[9]
    if row_list[10]:
        ing5 = row_list[10]
        ing5_amnt = row_list[11]

    recipe = {
        'levelReq': level,
        ing1: ing1_amnt,
        ing2: ing2_amnt,
        ing3: ing3_amnt
    }
    if ing4:
        recipe[ing4] = ing4_amnt
    if ing5:
        recipe[ing5] = ing5_amnt

    if i != 0:
        recipes[name] = recipe
    
# print(recipes)

with open('recipes.json', 'w') as file:
    json.dump(recipes, file, indent=4)
    


