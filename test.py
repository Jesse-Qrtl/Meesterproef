from functions import *

# Lists answers and guesses
guesses = make_list(r"C:\Users\Jesse Quartel\Documents\school\Meesterproef\guesses.txt")
answers = make_list(r"C:\Users\Jesse Quartel\Documents\school\Meesterproef\answers.txt")

# VALID GUESSES TESTS
print("VALID GUESSES TESTS")
# Test 1: valid guess
expected = True
guess = 'there'

if valid_guess(guess, guesses) == expected:
    print("\033[92mTest passed ✅\033[0m") # Green text for passed test
else:
    print("\033[91mTest failed ❌\033[0m") # Red text for failed test

# Test 2: not 5 letters unvalid guess
expected = False
guess = 'here'

if valid_guess(guess, guesses) == expected:
    print("\033[92mTest passed ✅\033[0m") # Green text for passed test
else:
    print("\033[91mTest failed ❌\033[0m") # Red text for failed test

# Test 3: not a word: unvalid guess
expected = False
guess = 'smsne'

if valid_guess(guess, guesses) == expected:
    print("\033[92mTest passed ✅\033[0m") # Green text for passed test
else:
    print("\033[91mTest failed ❌\033[0m") # Red text for failed test



# SCORE CALCULATING TESTS
print("\nSCORE CALCULATING TESTS")
# Test 1: all letters correct
expected = 10
guess = "there"
word = "there"

if calculate_score(guess, word) == expected:
    print("\033[92mTest passed ✅\033[0m")
else:
    print("\033[91mTest failed ❌\033[0m")

# Test 2: one correct letter in correct place
expected = 2
guess = "house"
word = "table"

if calculate_score(guess, word) == expected:
    print("\033[92mTest passed ✅\033[0m")
else:
    print("\033[91mTest failed ❌\033[0m")

# Test 3: no correct letters
expected = 0
guess = "quick"
word = "smart"

if calculate_score(guess, word) == expected:
    print("\033[92mTest passed ✅\033[0m")
else:
    print("\033[91mTest failed ❌\033[0m")

# guess evaluating`` tests
print("\nSCORE EVALUATING TESTS")

# Test 1: all letters are in the correct place
expected = "\033[32mt\033[32mh\033[32me\033[32mr\033[32me"
guess = "there"
word = "there"

if evaluate_guess(guess, word) == expected:
    print("\033[92mTest passed ✅\033[0m")
else:
    print("\033[91mTest failed ❌\033[0m")

# Test 2: a letter is in the word, but in the wrong place
expected = "\033[31mh\033[31mo\033[31mu\033[33ms\033[32me"
guess = "house"
word = "spear"

if evaluate_guess(guess, word) == expected:
    print("\033[92mTest passed ✅\033[0m")
else:
    print("\033[91mTest failed ❌\033[0m")

# Test 3: no letters are in the word
expected = "\033[31mq\033[31mu\033[31mi\033[31mc\033[31mk"
guess = "quick"
word = "smart"

if evaluate_guess(guess, word) == expected:
    print("\033[92mTest passed ✅\033[0m")
else:
    print("\033[91mTest failed ❌\033[0m")



# WORDLE TESTS