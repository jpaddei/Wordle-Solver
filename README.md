# Wordle Solver

## Background
In April 2024, I created the first version of my Wordle solver that runs on the command line. For each word the user types into the game, the program prompts the user with the colors of each letter and eliminates invalid words until it gets to a final word. The initial program worked well, but I wanted to advance it even further by having it interact with the website itself.

This project was ultimately a success, but in the future, I want to make a version where I can run the script on a website of a currently opened browser, rather than using Selenium WebDriver to open a browser on its own. I also want to improve the algorithm so the algorithm can find solutions more reliably, although so far, the only word that I have encountered that the program can’t solve without running out of attempts is “waste”.

## Description
The program launches an automated browser and loads wordleunlimited.org. This website was chosen because it can be played multiple times a day with different words, unlike the official Wordle by the New York Times.

It then solves the wordle by controlling the user’s mouse and keyboard to interact with the website.

The program starts with a list of all the possible final answers that a given Wordle can have. It types in a starting word (chosen by the user), then uses the results to eliminate words that aren’t compatible with those results. The next word the program chooses is the first word alphabetically out of the remaining ones.
* Green letters: All words that don’t have that letter in the exact slot are eliminated. 
* Yellow letters: Words that have that letter in the exact slot are eliminated, as well as words that don’t contain that letter at all. 
* Gray letters: Words that have that letter in the exact slot are eliminated.

If that letter appears more than once in the word, only the words with that letter in the exact slot are eliminated, since that letter could still appear elsewhere in the answer.

## Installation
```bash
pip install -r requirements.txt
```

## Running the program
You can run the program from the command line by running the following command into the directory:
```bash
wordle_solver
```
You can also execute the program from File Explorer.

While the program is running, keep your mouse idle until the wordle is solved. The program will automatically click on the website and start typing, and if you prematurely close out of the website, it will type the words somewhere else and crash the program.

## Built with
Languages: Python

Libraries: pyautogui, selenium
