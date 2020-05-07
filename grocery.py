import pandas as pd
import xlrd
import sys
import random
from collections import defaultdict
from random import randint

xl = pd.ExcelFile("/Users/eberman/projects/meal_shuffle.xlsx")

#opens workbook and specific worksheet
workbook = xlrd.open_workbook("/Users/eberman/projects/meal_shuffle.xlsx")
worksheet = workbook.sheet_by_name(workbook.sheet_names()[0])
recipe_num = randint(1,15)

def displayData():

    #default list created via collections library
    result = defaultdict(list)

    #opens meal_shuffle data workbook
    workbook = xlrd.open_workbook("/Users/eberman/projects/meal_shuffle.xlsx")
    #opens/reads the first sheet on the workbook
    worksheet = workbook.sheet_by_name(workbook.sheet_names()[0])
    #indicates the header row
    headers = worksheet.row(0)
    #indicates index column
    index = worksheet.col(0)

    for index, header in enumerate(headers):
        if index == 0:
            pass
        else:
            print(str(index) + ". " + header.value)


def pullRecipe():

    #prompt user input for which recipe they would like to see
    d_recipe = input("\nPlease select a recipe you would like to view (1 to 15): ")
    print("\nRecipe Ingredients: ")

    #finds the proper column regarding the user specified entry
    recipe = worksheet.col(int(d_recipe))

    #iterate through the ingredients on the recipe
    for items in recipe:
        #ignores the first row in the spreadsheet which lists the recipe name
        if items == recipe[0]:
            print(" ")
        else:
            # prints ingredients (.value is needed here since we need the value of the cell)
            items = items.value
            if items == "":
                pass
            else:
                print(items)
                
    print("\n")


def randomizeRecipe():

    active = True
    while active:
        prompt = input("Let's have some fun! Since nobody can choose what to have for dinner, let's roll the dice! ('r' to roll for a recipe, 'q' to quit): ")
        if prompt == 'q':
            active = False
        elif prompt == 'r':
            #same looping as in the pullRecipe method, but does not include user input and uses a randint to select a recipe
            recipe_num = randint(1,15)
            recipe = worksheet.col(int(recipe_num))
            for items in recipe:
            #ignores the first row in the spreadsheet which lists the recipe name
                if items == recipe[0]:
                    print(" ")
                else:
                    # prints ingredients (.value is needed here since we need the value of the cell)
                    items = items.value
                    if items == "":
                        pass
                    else:
                        print(items)
    print("\n")

            
            
        


print("Welcome to Meal Shuffle! Would you like to view a recipe, or have one selected at random?: \n"
      "1. Individual Recipe\n"
      "2. Meal Shuffle!\n")
active = True
while active:
    recipe_prompt = input("Please input the number 1 for an individual recipe, 2 for meal shuffle, or 'q' to quit: ")
    if recipe_prompt == 'q':
        active = False
    elif recipe_prompt == '1':
        displayData()
        pullRecipe()
    elif recipe_prompt == '2':
        randomizeRecipe()

