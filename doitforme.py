# Using this to load in data, and put it in fields for me cause I refuse to do it manually.
from json import load
try:
    from keyboard import write, press_and_release, wait
except ImportError:
    print("You need the Keyboard module to use this program. Install using `pip install keyboard`")
    raise SystemExit
from time import sleep

def rest():
    """Pauses the program for 0.25 seconds"""
    sleep(0.25)

def prompt():
    """Pauses the program until the user presses the tilde key."""
    wait("`")
    press_and_release("backspace")

with open("./data.json", encoding="utf-8") as fp:
    data = load(fp)
 
movies = data["movies"]

current_movie = 1
print("Press ` to begin!")
prompt()
while current_movie <= len(movies):
    for key, value in movies[str(current_movie)].items():
        print(key)
        write(key)
        press_and_release("tab")
        rest()
        press_and_release("tab")
        rest()
        write(value)
        press_and_release("tab")
        rest()
        press_and_release("tab")
        rest()
    
    current_movie += 1
    prompt()