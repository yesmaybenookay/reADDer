import os
import random

# Sets the directory reADDer will use
path = "/YOUR/PATH/HERE/reADDer/text/"

# Creates a list of files in path
files = os.listdir(path)

# Randomly selects a file from files
chosenfile = open(f"{path}{files[random.randint(0, len(files) - 1)]}", "rt")

# Saves the text from chosenfile as text
text = chosenfile.read()

# Closes chosenfile since it is not needed
chosenfile.close()

# Prints text
print(text)
