

def shortener(string, amount):
   # print(string)
    newString = ""
    runner = 0
    #print(amount)
    #print(newString)
    while runner != amount:
        newString = newString + string[runner]
        runner += 1
    
    return newString
        
def checkSpace(string):
  runner = 0
  forRunner = 0
  newString = ""
  while string[runner].isalpha() == False: 
      runner += 1
  while runner < len(string):
       newString += string[runner]
       runner += 1
  return newString

def numberInputChecker(input):
     while isinstance(input, int) == False:
         print("Please enter the a number input")
     int(input)
     return input



def dataSaver():
    f = open('dates.txt', 'r')
    lines = f.readlines()
    return lines


def fWrite(date, link, recipe) :   #Used in the first function
    lines = dataSaver()
    with open('dates.txt', 'a') as f:
       # f.write("{lines} \n")
        f.write(f"{date} * {link} * {recipe} \n") 
        f.close
def search(userinput):
    #searchFor = input("Date or Name(x/x/xx):")
    searchFor = userinput
    searchResults = ""
    f = open('dates.txt', 'r')
    if searchFor[0].isalpha(): 
       #print("Searching in alphabet mode, feature may not work as intended, use date for safer results")
       lenOfInput = len(searchFor)
       for line in f:
        date, link, recipe = line.split('*')
        recipe = checkSpace(recipe)
        shortRec = shortener(recipe, lenOfInput)
      #  print(f"shortRec has {shortRec}, while seach for has {searchFor}")
        if shortRec == searchFor:
            print(f"{recipe}: {link}")
            searchResults = f"{recipe}: {link}"
    else:
       for line in f:
        date, link, recipe = line.split('*')
        if date.strip() == searchFor.strip():
          print(f"{recipe}: {link}")
          searchResults = f"{recipe}: {link}"
    print(searchResults)
    return searchResults


def showAll():
    f = open('dates.txt', 'r')
    c = open('comments.txt', 'r')
    tempG = f.readlines()
    tempC = c.readlines()
    f.close()
    c.close()
    return f'''
    General:
    {tempG}
    Comments:
    {tempC}
             '''


def commentSaver(recipe, comment):
    with open('comments.txt', 'a') as f:
       f.write(f"{recipe}:  {comment}")
       f.close

