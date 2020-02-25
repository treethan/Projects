import xlrd

loc = ("/Users/eberman/projects/meal_shuffle.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

#pulls data from recipe row
for i in range(sheet.ncols):
    if i != 0:
        print(str(i) + ': ' + sheet.cell_value(0, i))
    else: 
        pass

nums = input("Pick the corresponding recipe number (1 to 15): ")

for num in range(sheet.ncols):
    recipe_name = sheet.cell_value(0, num)
    print(f"The ingredients for {recipe_name} are... ")

#    for i in range(sheet.nrows):
#        print(sheet.cell_value(i, prompt))