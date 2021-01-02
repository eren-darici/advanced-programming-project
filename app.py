import pandas as pd


class App:

    def __init__(self):
        self._foodDict = dict()

        self._recipes = list()

        self._df = pd.read_excel("recipes.xlsx")

        for i in self._df.index:
            recipeDict = {}
            foodList = []
            amountList = []
            foodList.append(self._df["Ingredients"][i].split(","))
            amountList.append(self._df["IngredientAmounts"][i].split(","))
            for i in foodList[0]:
                recipeDict[i] = int(amountList[0][foodList[0].index(i)])
            self._recipes.append(recipeDict)

    def addIngredient(self, ingredientName, ingredientAmount):
        if ingredientAmount > 0:
            self._foodDict[ingredientName] = ingredientAmount

    def showIngredients(self):
        IngredData = {"Ingredient": self._foodDict.keys(), "Amount": self._foodDict.values()}
        return pd.DataFrame(data=IngredData)

    def recipes(self):
        df = self._df.copy()
        df.pop("IngredientAmounts")
        return df

    def recipeCheck(self, numberofPeople=1):
        foodNames = [x for x in self._df["Recipe"]]
        checkList = []
        for i in self._recipes:
            lenFood = len(i)
            tempList = []
            for j in i.keys():
                if j in self._foodDict.keys():
                    if self._foodDict[j] >= i[j] * numberofPeople:
                        tempList.append(foodNames[self._recipes.index(i)])
                if len(tempList) == lenFood:
                    for x in list(set(tempList)):
                        checkList.append(x)
        return checkList


app = App()
