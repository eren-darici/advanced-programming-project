import pandas as pd


class App:
    def __init__(self):
        """Initialization of Class with Lists"""
        self._ingridients = list()
        self._numberofPeople = int()
        self._ingridientAmount = list()
        tempList = list()
        self._finalIngrid = list()

        self._recipes = list()
        self._howTo = list()

        file = "recipes.xlsx"
        recipeDF = pd.read_excel(file)

        for i in recipeDF.index:
            self._recipes.append([recipeDF["Recipe"][i], recipeDF["Ingridients"][i].split(",")])
            self._howTo.append(recipeDF["howTo"][i])
            tempList.append(recipeDF["IngridientAmounts"][i].split(","))

        self.df = recipeDF

        for sublist in tempList:
            placeholder = []
            for item in sublist:
                placeholder.append(int(item))
            self._ingridientAmount.append(placeholder)

        del tempList

    def addIngridient(self, ingridientName, ingridientAmount):
        """Method to add Ingridients that we have"""
        temp = [ingridientName, ingridientAmount]
        self._ingridients.append(temp)

    def showIngridients(self):
        """Method to show Ingridients that we have"""
        temp1 = list()
        temp2 = list()
        for i in self._ingridients:
            temp1.append(i[0])
            temp2.append(i[1])
        out = pd.DataFrame({"Ingridients": temp1, "Amount": temp2})
        return out

    def recipes(self):
        """Recipe List"""
        return self._recipes

    def recipeCheck(self):
        """The recipes that we can make with ingridients"""
        canDo = list()
        for i in self._ingridients:
            self._finalIngrid.append(i[0])

        for i in range(len(self._recipes)):

            check = all(item in self._finalIngrid for item in self._recipes[i][1])
            # print(self._finalIngrid)
            if check is True:
                canDo.append(self._recipes[i][0])
            else:
                pass

        return canDo

    def recipeDFret(self):
        pass


app = App()
