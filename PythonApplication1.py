from cooking import *
searchBool = False
print("Welcome to the cooking list app!")
runing = False #Change to true for testing the base code
while(runing):
    userChoice =input("""
      1. Add Recipies 
      2. Make a comment
      3. Search
      4. Show all recipies
      5. End Program
      """)
    userInt = numberInputChecker(input)
    if userInt == 1:
         print("Please write the Date Added(x/x/xx), Link, and Recipe(no spaces)")
         print("Seperate each with a -")
         date, link, recipe = input().split('-')
         fWrite(date, link, recipe)
        # userChoice = 0
    elif userInt == 2:
          recipeC = input("What recipie are you making a comment about")
          userComment = input("Write your comment")
          commentSaver(recipeC, userComment)
          userChoice = 0
    elif userInt == 3:
          print("this input is currently not working for commented names")
          print("if sorting by name, the name must be exactly right for the code to function")
          search()
          userChoice = 0
    
         # userSearchChoice = input("press D to search by date, N to searh by name")
         # if userSearchChoice == upper(userSearchChoice):
         #     searchBool = True

    elif userInt == 4:
        showAll()
        userChoice = 0
    
    elif userInt == 5:
        runing = False

    else:
          print("Please Input a number from 1-5")
          userChoice = 0


      


"""Function versions of each of the choices """
def addRec(textToSplit):
    #print("Please write the Date Added(x/x/xx), Link, and Recipe(no spaces)")
    #print("Seperate each with a -")
    date, link, recipe = textToSplit.split('-')
    fWrite(date, link, recipe)
def commenter(rec, comm):
    #recipeC = input("What recipie are you making a comment about")
    #userComment = input("Write your comment")
    commentSaver(rec, comm)
def searchForRec():
    print("this input is currently not working for commented names")
    print("if sorting by name, the name must be exactly right for the code to function")
    search()
def showAllRecipies():
    showAll()

