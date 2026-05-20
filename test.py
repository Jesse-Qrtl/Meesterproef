from functions import *

# Lists answers and guesses
guesses = make_list(r"C:\Users\Jesse Quartel\Documents\school\Meesterproef\guesses.txt")
answers = make_list(r"C:\Users\Jesse Quartel\Documents\school\Meesterproef\answers.txt")

# VALID GUESSES TESTS
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


# WORD FEEDBACK TESTS


# WORDLE TESTS