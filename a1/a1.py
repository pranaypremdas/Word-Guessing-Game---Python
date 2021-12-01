"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Pranay Premdas}} ({{s4644467}})"
__email__ = "p.premdas@uqconnect.edu.au"
__date__ = "4/09/2020"


# Write your code here (i.e. functions)

# Beginning of the game


# Main Code
def main():
    """
    Handles top-level interaction with user.
    """
    # Write the code for your main function here
    print(WELCOME)
    b = True
    while b == True:
        action = str(input(INPUT_ACTION))
        if action == 's':
            start_game()
            b = False
        elif action == 'h':
            print(HELP)
            start_game()
            b = False
        elif action == 'q':
            b = False
        else:
            print(INVALID)

def start_game():
    """
    Handles top-level interaction with user.
    """
    word_select = str(input("Do you want a 'FIXED' or 'ARBITRARY' length word?: "))
    print('Now try and guess the word, step by step!!')
    word = select_word_at_random(word_select)
    word_length = len(word)
    guess_count = word_length
    guess = ''
    guess_no = 1
    scores = ()
    """loops until number of guesses run out"""
    while guess_count != 0:
        letter_tuple = GUESS_INDEX_TUPLE[word_length - 6]
        new_tuple = letter_tuple[guess_no -1]
        x, y = new_tuple
        start_index = x
        end_index = y
        difference = y - x
        if guess_no <= word_length -1:
            create_guess_line(guess_no, word_length)
            display_guess_matrix(guess_no, word_length, scores)
            while True:
                guess_input = 'Now enter Guess' + ' ' + str(guess_no) + ':' + ' '
                guess = input(guess_input)
                if len(guess) == difference + 1:
                    a = compute_value_for_guess(word, start_index, end_index, guess)
                    scores += (a,)
                    guess_no += 1
                    guess_count -= 1
                    break
                else:
                    continue

                """Programs for last guess of the game."""
        else:
            guess_no = word_length
            create_guess_line(guess_no, word_length)
            display_guess_matrix(guess_no, word_length, scores)
            final_guess = input('Now enter your final guess. i.e. guess the whole word: ')
            if final_guess == word:
                print("You have guessed the word correctly. Congratulations.")
                return None
            else:
                print('Your guess was wrong. The correct word was "{}"'.format(word))
                return None

def select_word_at_random(word_select):
    """
    Function: Programs for the word to be chosen. This is decided by the
    previous choice of FIXED or ARBITRARY.
    
    Returns: random fixed or arbitrary word (str). If invalid choice made
    returns none.
    """
    if word_select == 'FIXED' or word_select == 'ARBITRARY':
        random_word = load_words(word_select)
        random_number = random_index(load_words(word_select))
        word = (random_word[random_number])
        return word
    else:
        return None

def create_guess_line(guess_no, word_length):
    """
    Function: This function returns the string representing the display
    corresponding to the guess number integer, guess no.

    Parameters: guess_no ->> int , word_length ->> int

    Preconditions = 9 >=guess_no>= 0 and word_length <= 9.

    """
    letter_tuple = GUESS_INDEX_TUPLE[word_length-6]
    string_guess_no = str(guess_no)
    guess_line = ('Guess' + ' ' +  string_guess_no + WALL_VERTICAL)
    new_tuple = letter_tuple[guess_no - 1]
    x, y = new_tuple
    for i in range(word_length):
        if x <= i <= y:
            guess_line += ' * ' + WALL_VERTICAL
        else:
            guess_line += ' ' + WALL_HORIZONTAL + ' ' + WALL_VERTICAL
    return guess_line

def display_guess_matrix(guess_no, word_length, scores):
    """
    Function: Prints the progress of the game. Displays line strings for guesses
    up to guess no with their corresponding scores (a tuple containing all
    previous scores), and the line string for guess no (without a score).

    Parameters: guess_no ->> int, word_length ->> int, scores->> tuple
    """
    """loops to print the top part of the display guess matrix (numbers) depending on
    word_length"""
    final_print = ('       |')
    count_down = word_length
    count_up = 1
    while count_down != 0:
        count_up_str = str(count_up)
        final_print += (' ' + count_up_str + ' |')
        count_up += 1
        count_down -= 1

    print(final_print)
    print(WALL_HORIZONTAL * (9 + 4 * word_length))

    count = 1
    score_count = 0
    line_count = str(word_length - 6)
    """loops to print the progress of game after attempt at guessing"""
    while True:
        if count < guess_no and score_count != guess_no:
            sub_scores = scores[score_count]
            sub_scores_str = str(sub_scores)
            print (create_guess_line(count, word_length) + '   ' + sub_scores_str + ' Points')
            print(WALL_HORIZONTAL * (9 + 4 * word_length))
            count += 1
            score_count += 1
        else:
            print (create_guess_line(count, word_length))
            print(WALL_HORIZONTAL * (9 + 4 * word_length))
            return None

def compute_value_for_guess(word, start_index, end_index, guess):
    """
    Function: Return the score, an integer, the player is awarded for a
    specific guess.

    Preconditions: word->> str, start_index--> int, end_index->> int, guess--> int

    Parameters 6 >=len(word)<= 9

    Returns: scores(int)

    """
    scores = 0
    word_break_down = word[start_index:end_index + 1]

    for i in word_break_down:
        if i in guess:
            scores += 5
            if word_break_down.index(i) == guess.index(i):
                if i in VOWELS:
                    scores += 9
                elif i in CONSONANTS:
                    scores += 7
    return scores

if __name__ == "__main__":
    main()
