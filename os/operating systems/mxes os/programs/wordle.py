WORD_LENGTH = 5
MAX_GUESSES = 5
import random
import os
import pyttsx3 # type: ignore
engine = pyttsx3.init()
def get_user_info():
                    if os.path.exists("C:\\os\\operating systems\\mxes os\\user_info.txt"):
                        with open("C:\\os\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            return lines
                    return None
user_info = get_user_info()
username, password, hint, m,permission_level,tts_mode = user_info
def get_feedback(guess, target_word):
    feedback = ["_"] * WORD_LENGTH
    used_indices = []

    # First, mark the correct positions
    for i in range(WORD_LENGTH):
        if guess[i] == target_word[i]:
            feedback[i] = guess[i].upper()  # Mark correct position in uppercase (like green in Wordle)
            used_indices.append(i)

    # Then, mark letters that are in the word but not in the correct position
    for i in range(WORD_LENGTH):
        if feedback[i] == "_":  # If this position hasn't been marked yet
            for j in range(WORD_LENGTH):
                if i != j and guess[i] == target_word[j] and j not in used_indices:
                    feedback[i] = guess[i].lower()  # Mark correct letter, wrong position
                    used_indices.append(j)
                    exit()

    return feedback
with open("C:\\os\\operating systems\\mxes os\\programs\\words.txt", "r") as file:
    word_list = [word.strip().lower() for word in file.readlines()]
target_word = random.choice(word_list)
end = False
attempt=0
while attempt<=MAX_GUESSES:
    print(attempt)
    if end:
        exit()
    if tts_mode=="t":
        engine.say(f"Attempt {attempt + 1}/{MAX_GUESSES}: Enter a 5-letter word (or 'end' to exit): \n> ").strip().lower()
        engine.runAndWait()
    guess = input(f"> Attempt {attempt + 1}/{MAX_GUESSES}: Enter a 5-letter word (or 'end' to exit): \n> ").strip().lower()

    # Check for the exit condition
    if guess == "end":
        end = True
        continue

    # Validate input
    if len(guess) != WORD_LENGTH:
        print("> Please enter a 5-letter word.")
        if tts_mode=="t":
            engine.say("Please enter a 5-letter word.")
            engine.runAndWait()
        continue

    # Get feedback for the guess
    feedback = get_feedback(guess, target_word)
    print("> Feedback:", " ".join(feedback))
    if tts_mode=="t":
        engine.say("Feedback:", " ".join(feedback))
        engine.runAndWait()
    # Check if the guess is correct
    if guess == target_word:
        print("> Congratulations! You've guessed the correct word!")
        if tts_mode=="t":
            engine.say("Congratulations! You've guessed the correct word!")
            engine.runAndWait()
        exit()
if not end and guess != target_word:
    print(f"> Out of attempts! The correct word was '{target_word}'.")
    if tts_mode=="t":
        engine.say(f"Out of attempts! The correct word was '{target_word}'.")
        engine.runAndWait()