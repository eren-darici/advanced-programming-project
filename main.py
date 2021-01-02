from app import App

app = App()

while True:
    print("1-) Add ingredient\n"
          "2-) Show ingredients\n"
          "3-) Recipe list\n"
          "4-) Recipe check\n"
          "q-) Exit")

    print("********************")

    userInput = input("please select an event: ")

    print("********************")

    if userInput == "q":
        print("Exit")
        print("********************")
        break

    elif userInput == "1":
        print("**Add Ingredient**")
        ingredient = input("Please enter ingredient: ").upper()
        amount = input("Please enter the amount of ingredient: ")
        app.addIngredient(ingredient, int(amount))
        print("********************")


    elif userInput == "2":
        print("*Show Ingredients*")
        print(app.showIngredients())
        print("********************")

    elif userInput == "3":
        print("**Show All Recipes**")
        print(app.recipes())
        print("********************")

    elif userInput == "4":
        print("***Check Recipess***")
        numberOfPeople = input("Please enter the number of people: ")
        print(app.recipeCheck(int(numberOfPeople)))
        print("********************")

    else:
        print("Invalid event.")
        print("********************")
