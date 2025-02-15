from terminaltexteffects.effects.effect_vhstape import VHSTape
import os
import random 
import time


# this effect will display the text "YourTextHere" in a VHS tape style
# but actually im going to load a bunch text ascii art from a folder randomly each time the while loop runs
# and display it in a VHS tape style, the ascii files are named 1.txt to 13.txt
# the ascii art is from a steam group "asciiartamalgamation", the category is anime various artists made them
# i will add the ascii art files to the folder "animuwhemen" in the root of the project
MAXFILES = 13

# get the current working directory
cwd = os.getcwd()
# get the path to the folder with the ascii art
ascii_folder = os.path.join(cwd, "animuwhemen")
# iterate tru random files in the folder and make into a string to add the effect
def get_random_ascii():
    random_file = random.randint(1, MAXFILES)
    file_path = os.path.join(ascii_folder, f"{random_file}.txt")
#    print(f"Reading file: {file_path}")  # Debug print
    with open(file_path, "r") as file:
        ascii_art = file.read()
#    print(f"ASCII Art: {ascii_art}")  # Debug print
    return ascii_art



def main():
    print("Welcome to pyAnimu!")
    while True:
        effect = VHSTape(get_random_ascii())
        with effect.terminal_output() as terminal:
            for frame in effect:
                terminal.print(frame)
        
        # sleep for 1 second
        time.sleep(5)
        
        #clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
