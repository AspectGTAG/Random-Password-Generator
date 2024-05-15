import json # for loading json files
import random # for to get random letters for the password
import os.path # for managing files and os-related stuff
import os # for clearing the console

def exit_with_delay(exit_message, exit_delay = 3, exit_code = 0):
    import time # for setting delay

    # output exit message
    print(exit_message)

    # exit after 3 sec
    time.sleep(exit_delay)
    quit(exit_code)

# Create new settings file if current folder doesn't create one
if os.path.exists("settings.json") != True:
    f = open("settings.json", "w")
    f.write('{ "LETTERS": "abcdefghijklmnopqrstuvwxyz1234567890", "LENGTH": 8, "PERFORMANCE": false }')
    exit_with_delay("'settings.json' wasn't found so a new one was created, restart to use new 'settings.json', exiting now...") # exit with message and delay

# Open file
f = open("settings.json")

# Get data from json file
data = json.load(f)

# Get data from json data
letters = data["LETTERS"]
length = data["LENGTH"]
performance = data["PERFORMANCE"]

# Create password
password = ""
procent = 0
for x in range(length):
    password += letters[random.randint(-1, len(letters)-1)] # add letter to new password

    # Make loading bar
    if procent < int(x/length*100):
        if performance == False:
            os.system("cls") # Clear console
            print(f"[{('#'*int(x/length*10))+('*'*(10-int(x/length*10)))}] {int(x/length*100)}%") # Output bar
        else:
            print(f"{int(x/length*100)}%")
        procent = int(x/length*100) # set new procent

# Log password to .txt file
writer = open("password.txt", "w")
writer.write(password)

# Close json file
f.close()

# Send exit message and exit console
os.system("cls") # clear console
if performance == False: print(f"[{'#'*10}] 100%") # display that it is at 100%
else: print(f"100%")
exit_with_delay("DONE, exiting now...") # exit with message and delay