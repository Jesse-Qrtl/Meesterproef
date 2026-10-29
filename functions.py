import random

def make_list(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    result = ""

    for i in range(len(word)):
        if guess[i] == word[i]:
            result += "\033[32m" + guess[i] # groen
        elif guess[i] in word:
            result += "\033[33m" + guess[i] # geel
        else:
            result += "\033[31m" + guess[i] # rood
            
    return result

def calculate_score(guess, word):
    score = 0
    counted_letters = set()

    for i in range(len(word)):
        if guess[i] == word[i] and guess[i] not in counted_letters: # groen
            score += 2
            counted_letters.add(guess[i])
    
    return score

def wordle(guesses, answers):
    print("Welcome to Wordle! Get 6 chances to guess a 5 letter word.")
    secret_word = random.choice(answers).lower()

    attempts = 0
    max_attempts = 5
    total_score = 0

    while attempts <= max_attempts:
        guess = input("Enter Guess " + str(attempts) + ": ").lower()
        
        if not valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            attempts = 0
            break

        attempts += 1
        round_score = calculate_score(guess, secret_word)
        total_score += round_score
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

def bingo_ball_amount():
    pass

def bingo_ball_numbers():
    pass        

def bingo_cart():
    pass