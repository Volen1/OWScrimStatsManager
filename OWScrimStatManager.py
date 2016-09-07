# Name the Database File
dbFileName = input("Please name your stats File: ")

# Create the Database file for storing the Stats information.
statsDB = open(dbFileName, "w")

# Loop to continue asking until user says no.
ans = 'n'
while ans == 'n':
    # Get the Game Number. aka Game 1 -> Game 2 -> Game 3 etc..
    gameNumber = (input("Please enter the game number:  "))
    statsDB.write("Game Number: " + gameNumber + "\n" )

    # Get all of the Values associated with that number.
    eliminations = input("Please enter your amount of Eliminations ")
    statsDB.write("Eliminations: " + eliminations + "\n")

    dmgDone = input("Please enter your amount of Damage Done ")
    statsDB.write("Damage Done: " + dmgDone + "\n")

    healingDone = input("Please enter the amount of healing you have done ")
    statsDB.write("Healing Done: " + healingDone + "\n")

    objKills = input("Please enter the amount of Objective Kills you had ")
    statsDB.write("Objective Kills: " + objKills + "\n")

    objTime = input("Please enter the amount of time you spent on the Objective ")
    statsDB.write("Amount of time spent on the Objective in SECONDS: " + objTime + "\n")

    deaths = input("Please enter the amount of Deaths you had ")
    statsDB.write("Deaths accumulated: " + deaths + "\n")

    statsDB.write("===================================================================================================")

    ans = input("Would you like to Terminate the program now? (y/n)").lower()



