import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

width, height = pyautogui.size()

valid_words = []
guessed_words = []

options = webdriver.ChromeOptions()
options.add_argument("--log-level=1")

driver = webdriver.Chrome(options=options)
driver.get('https://wordleunlimited.org')
driver.maximize_window()

game_app = driver.find_element(By.TAG_NAME, "game-app")
shadow_root = game_app.shadow_root
board = shadow_root.find_element(By.ID, "board")
game_rows = board.find_elements(By.CSS_SELECTOR, "game-row")

# Wait to get to wordle website
time.sleep(1)

# Load list of words
with open("answers.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    valid_words.append(line.strip())

# Initiate current guess (Enter starting word of choice here)
current_guess = "soare"

# Solve wordle
for i in range(6):
    # If there are no remaining words in the valid words list, the algorithm couldn't find the correct word
    if len(valid_words) == 0:
        print("Word not found")
        print("List of guessed words: ", guessed_words)
        break
    
    # If there is one word remaining in the valid words list, that should be the correct word 
    elif len(valid_words) == 1:
        current_guess = valid_words[0]
        print("The correct word should be", current_guess)
        pyautogui.click(width/16, height/2)
        pyautogui.write(current_guess)
        pyautogui.press("enter")
        if current_guess not in guessed_words:
            guessed_words.append(current_guess)
        print("Guessed words:", guessed_words)
        break

    # Update the current guess to be the first word in the valid words list
    if i > 0:
        current_guess = valid_words[0]

    # Add the current word to the list of guesses
    guessed_words.append(current_guess)

    # Type current word into wordle
    pyautogui.click(width/16, height/2)
    pyautogui.write(current_guess)
    pyautogui.press("enter")
    time.sleep(3)

    shadow_root = game_rows[i].shadow_root
    row = shadow_root.find_element(By.CLASS_NAME, "row")
    game_tiles = row.find_elements(By.CSS_SELECTOR, "game-tile")

    # Initialize list with all the letters in the current guess
    letters_in_guess = list(current_guess)

    # Check each letter for words to remove from the valid words list
    for letter, game_tile in enumerate(game_tiles):
        evaluation = game_tile.get_attribute("evaluation")
        kept_words = []

        # Eliminate invalid words from valid_words list
        for word in valid_words:
            if evaluation == "correct":
                if word[letter] == current_guess[letter]:
                    kept_words.append(word)
            elif evaluation == "present":
                if word[letter] != current_guess[letter] and current_guess[letter] in word:
                    kept_words.append(word)
            elif evaluation == "absent":
                if letters_in_guess.count(current_guess[letter]) > 1:
                    if word[letter] != current_guess[letter]:
                        kept_words.append(word)
                else:
                    if current_guess[letter] not in word:
                        kept_words.append(word)
                
        valid_words = kept_words

# Time (in seconds) program will run after the solver completes
time.sleep(120)