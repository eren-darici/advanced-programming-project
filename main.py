from openpyxl import Workbook
import pandas as pd
import numpy as np
import time


class App:
    def __init__(self):
        """Initialization of stuff"""
        self._ingridientDict = {}
        self._ingridients = []
        self._amount = []
        self._recipes = list()
        self._howTo = list()

        self._iDuo = list()

        file = "recipes.xlsx"
        recipeDF = pd.read_excel(file)
        for i in recipeDF.index:
            self._recipes.append([recipeDF["Recipe"][i], recipeDF["Ingridients"][i].split(",")])
            self._howTo.append(recipeDF["howTo"][i])

    def addIngridient(self, item, amount):
        """Method to add ingridient"""
        self._ingridientDict[item] = amount

    def showIngridients(self):
        """Method to show present ingridients"""
        self._ingridients = list(self._ingridientDict.keys())
        self._amount = list(self._ingridientDict.values())
        data = {'Ingridients': self._ingridients, 'Amount': self._amount}
        print(pd.DataFrame(data))

    def showAllRecipes(self):
        """Method to show all recipes"""
        for recipe in self._recipes:
            print(recipe[0])

    def recipeCheck(self):
        """Method to check recipes"""
        canDo = []
        temp = []
        pass





app = App()
app.addIngridient("elma",1)
app.addIngridient("ekmek",3)
app.showIngridients()

# while True:
#     print("Select an operation. Press q to exit.")
#     time.sleep(1)
#     print("1-) Add Ingridients")
#     print("2-) Show Ingridients")
#     print("3-) Show All Recipes")
#     userInput = input('Please select: ')
#
#     if userInput == "q":
#         break
#
#     elif userInput == "1":
#         print("******************************")
#         time.sleep(1)
#         ingridient = input("Please enter ingridient: ")
#         amount = int(input('Please enter amount of the ingridient: '))
#         app.addIngridient(ingridient, amount)
#         print("******************************")
#
#     elif userInput == "2":
#         print("******************************")
#         time.sleep(1)
#         app.showIngridients()
#         print("******************************")
#
#     elif userInput == "3":
#         print("******************************")
#         time.sleep(1)
#         app.showAllRecipes()
#         print("******************************")
#
#
#     else:
#         print("******************************")
#         print("Please select a valid operation.")
#         print("******************************")
