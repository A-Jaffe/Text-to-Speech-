import pyttsx3

# Request file name from user, open file and read contents
file_name = input("Please enter a file name:")
file = open(f"{file_name}.txt")
content = file.readlines()

# Initiate an engine object to read .txt file
engine = pyttsx3.init()

# Create list 'voices' to store engine objects voice options
voices = engine.getProperty('voices')

# Print out voice details for user to choose
for i in range(len(voices)):
    print(f"{i} -- {voices[i]}")

# Request choice as Integer from user
voice_choice = int(input("Please choose your desired voice, by number: "))

# Set voice to user choice
engine.setProperty('voice', voices[voice_choice].id)

# For each line in .txt, read outloud 
for i in content:
    engine.say(i)
    engine.runAndWait()

