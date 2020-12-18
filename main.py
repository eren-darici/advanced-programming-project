from app import App

app = App()

while True:
    print("1-) add ingredient\n"
          "2-) show ingredients\n"
          "3-) recipe list\n"
          "4-) recipe check\n"
          "q-) exit")

    userInput = input("please select an event: ")

    if userInput == "q":
        print("exit")
        break

    elif userInput == "1":
        ingredient = input("plz enter ingredient: ").upper()
        amount = input("plz enter amount of ingredient: ")
        app.addIngredient(ingredient, amount)

    elif userInput == "2":
        print(app.showIngredients())
    elif userInput == "3":
         print(app.recipes())
    elif userInput == "4":
        print(app.recipeCheck())
    else:
        print("invalid event")
