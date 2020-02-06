from person import Person
import time

if __name__ == "__main__": #proper naming
  personList = []
  #random list of people
  personList.append(Person('Gregory',27,'eggs','writer')) #instantiate class
  personList.append(Person('Raymond',20,'chipotle','student'))
  personList.append(Person('Salika',53,'beans','veterinarian'))
  personList.append(Person('Chubs',7,'hot dogs','student'))
  personList.append(Person('Rebecca',21,'pasta','singer'))
  personList.append(Person('Ben',21,'sushi','singer'))
  personList.append(Person('Martin',34,'pie','doctor'))

  print("Welcome to Esfera Academy! Here are a few people that come to our school.")
  print()
  collegeAged = [] #list comprehension below to determine if college-aged
  collegeAged = [Person for Person in personList if Person.age >= 18 and Person.age < 22]

  i = 0
  while i < len(collegeAged): #print college aged students, looping structure
    collegeAged[i].introduction() #invoke method from class
    i += 1

  print()
  name = input("Please enter your name: ") #name input with try/catch for improper input, input structure
  try: #try and catch structure
    val = int(name)
    print("Incorrect input int, please put a String")
  except ValueError:
    try:
      val = float(name)
      print("Incorrect input float, please put a String")
    except ValueError:
      print("Hi "+name+"! Pleasure to meet you.")
  
  print()
  gpa = input("Enter your GPA as a decimal: ") #gpa input with try/catch for improper input
  try:
    val = int(gpa)
    print("Incorrect input Int, please put a Float!")
  except ValueError:
    try:
      val = float(gpa)
      gpa = val
      if val >= 3.5:
        print("Wow, amazing job!")
      else:
        if val >= 2.75:
          print("Good job!")
        else:
          if val >= 2.25:
            print ("Not bad.")
          else:
            print("You might not be a good fit to apply here, but GPA isn't everything.")
    except ValueError:
      print("Incorrect input type!")
  
  print()
  essay = input("Please tell us why you want to go to Esfera Academy: ")
  print()
  if len(essay) < 150:
    print("That's... a little short, don't you think?")
  time.sleep(2)

  score = 0 #score is calculated by the user's essay containing certain buzzwords
  wordScoring = { #dictionary comprehension
  'dedicat': 2, 
  'motivat': 4, 
  'inspir': 3, 
  'curio': 2, 
  'commit': 5, 
  'passion': 7, 
  'success': 6,
  'enthus': 3,
  'team': 1,
  'imaginat': 2,
  'reliab': 4,
  'skill': 1,
  'optimis': 5,
  'intell': 6,
  'extraordinar': 4,
  'creativ': 4,
  'potent': 7,
  'talent': 2,
  'invent': 3,
  'achieve': 6,
  }

  for key in wordScoring: #calculate score by finding key in essay
    if key in essay:
         score = score + (wordScoring[key])
  print("You earned a score of:",score)
  time.sleep(3)
  #ADMISSION
  admission = False #default

  if gpa >= 4.0:
    admission = True #these factors determine if they are admitted
  else:
    if gpa > 3.0 and score > 15:
      admission = True
    else: 
      if gpa > 2.0 and score > 30:
        admission = True
      else:
        if score > 50:
          admission = True
  print()
  print("Thank you for your submission!")
  print()
  print("Calculating your results...")
  print()
  time.sleep(3)

  print("You are...")
  time.sleep(1)

  if admission: #if admission = true
    print ("ACCEPTED into Esfera academy, congratulations! Welcome to your new home. Enjoy your 4 years here!")
  else:
    print ("REJECTED from Esfera academy. Sorry, better luck next time!")
