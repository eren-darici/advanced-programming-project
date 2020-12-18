import pandas as pd


class App:
    def __init__(self):
        """Initialization of Class with Lists"""
        self._ingredients = list()
        self._numberofPeople = int()
        self._ingredientAmount = list()
        tempList = list()
        self._finalIngred = list()

        self._recipes = list()
        self._howTo = list()

        file = "recipes.xlsx"
        recipeDF = pd.read_excel(file)

        for i in recipeDF.index:
            self._recipes.append([recipeDF["Recipe"][i], recipeDF["Ingredients"][i].split(",")])
            self._howTo.append(recipeDF["howTo"][i])
            tempList.append(recipeDF["IngredientAmounts"][i].split(","))

        self.df = recipeDF

        for sublist in tempList:
            placeholder = []
            for item in sublist:
                placeholder.append(int(item))
            self._ingredientAmount.append(placeholder)

        del tempList

    def addIngredient(self, ingredientName, ingredientAmount):
        """Method to add Ingredients that we have"""
        temp = [ingredientName, ingredientAmount]
        self._ingredients.append(temp)

    def showIngredients(self):
        """Method to show Ingredients that we have"""
        temp1 = list()
        temp2 = list()
        for i in self._ingredients:
            temp1.append(i[0])
            temp2.append(i[1])
        out = pd.DataFrame({"Ingredients": temp1, "Amount": temp2})
        return out

    def recipes(self):
        """Recipe List"""
        return self._recipes

    def recipeCheck(self):
        """The recipes that we can make with ingredients"""
        canDo = list()
        for i in self._ingredients:
            self._finalIngred.append(i[0])

        for i in range(len(self._recipes)):

            check = all(item in self._finalIngred for item in self._recipes[i][1])
            # print(self._finalIngred)
            if check is True:
                canDo.append(self._recipes[i][0])
            else:
                pass

        return canDo

    def recipeDFret(self):
        pass


app = App()
