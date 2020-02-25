import pandas as pd
import xlrd
import sys
import random
from collections import defaultdict

xl = pd.ExcelFile("/Users/eberman/projects/meal_shuffle.xlsx")

def displayData():

    #default list created via default library
    result = defaultdict(list)

    #opens meal_shuffle data workbook
    workbook = xlrd.open_workbook("/Users/eberman/projects/meal_shuffle.xlsx")
    #opens/reads the sheet on the workbook
    worksheet = workbook.sheet_by_name(workbook.sheet_names()[0])
    #indicates the header row
    headers = worksheet.row(0)
    index = worksheet.col(0)

    for index, header in enumerate(headers):
        if index == 0:
            pass
        else:
            print(str(index) + ". " + header.value)

    # #in the first sheet of the workbook
    # for index in range(worksheet.nrows)[1:]:
    #     #iterate through headers/columns in worksheet
    #     for header, col in zip(headers, worksheet.row(index)):
    #         #appends header/column value
    #         result[header.value].append(col.value)
       
    #formats data with pandas library
    # df = xl.parse(xl.sheet_names[0])

    # print (df)

def pullRecipe():

    #opens workbook and specific worksheet
    workbook = xlrd.open_workbook("/Users/eberman/projects/meal_shuffle.xlsx")
    worksheet = workbook.sheet_by_name(workbook.sheet_names()[0])

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
            print(items)

#def randomizeRecipe(pullRecipe):


displayData()
pullRecipe()