from app import App

app = App()

while True:
    print("1-) add ingridient\n"
          "2-) show ingridients\n"
          "3-) recipe list\n"
          "4-) recipe check\n"
          "q-) exit")

    userInput = input("please select an event: ")

    if userInput == "q":
        print("exit")
        break

    elif userInput == "1":
        ingridient = input("plz enter ingridient: ").upper()
        amount = input("plz enter amount of ingridient: ")
        app.addIngridient(ingridient, amount)

    elif userInput == "2":
        print(app.showIngridients())
    elif userInput == "3":
         print(app.recipes())
    elif userInput == "4":
        print(app.recipeCheck())
    else:
        print("invalid event")
