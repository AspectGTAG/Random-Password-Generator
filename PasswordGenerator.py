import json # import json for loading json files
import random # import random for to get random letters for the password
import os.path # import os for managing files and os-related stuff

# Create new settings file if current folder doesn't create one
if os.path.exists("settings.json") != True:
    f = open("settings.json", "w")
    f.write('{ "LETTERS": "abcdefghijklmnopqrstuvwxyz1234567890", "LENGTH": 8 }')
    quit(0)

# Open file
f = open("settings.json")

# Get data from json file
data = json.load(f)

# Get data from json data
letters = data["LETTERS"]
length = data["LENGTH"]

# Create password
password = ""
for x in range(length):
    password += letters[random.randint(-1, len(letters)-1)]

# Log password to .txt file
writer = open("password.txt", "w")
writer.write(password)

# Close json file
f.close()