def letter_in_word(letter, word, i):
    if letter in word and letter == word[i]:
        return "^"
    elif letter in word:
        return "!"
    else:
        return "x"
    
def guess_vs_word(guess, word):
    status = ""
    for i in range(5):
        status += letter_in_word(guess[i],word,i)
    return status

def interface():
    #request player 1 to enter a 5-letter word
    player_1 = input("Please enter a 5-letter word: ")
    #convert to upper case
    player_1.upper()
    #player 1 re-enters word when previous word not exactly 5 letters
    while len(player_1)!= 5 and not word.isalpha():
        print("Invalid word entered. Please enter a 5-letter word.")
        player_1 = input("Please re-enter a 5-letter word: ")

    count = choice()
    #On 6 seperate occassions
    for i in range(count):
        #request player 2 to enter a 5-letter word to guess
        player_2 = input("Please enter a 5-letter word to guess: ")
        #convert to upper case
        player_2.upper()
        #player 2 re-enters word when the word not exactly 5 letters
        while len(player_2)!= 5 and not word.isalpha():
            print("Invalid word entered. Please enter a 5-letter word to guess.")
            player_2 = input("Please re-enter a 5-letter word to guess: ")
    
        #output the guess on one line, followed by the status on another line.
        #The status should show whether each letter from guess is found in word.
        print("\n" + player_2)
        print(guess_vs_word(player_2, player_1))
        #output when player 2 guess correctly
        if player_2 == player_1:
            print("You guess the word correctly after {} attempt(s)!".format(i+1))
            break
        #output the number of attempts left after each failed attempt
        else:
            print("You have {} attempt(s) left!".format(count-1-i))
        #output when player 2 exhausted all attempts
        if i == 5:
            print("You have exhausted all your attempts. Word entered by Player 1: {}".format(player_1))

def choice():
    print("Difficulty level of play")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    level = int(input("Player 2! Please select the difficulty level: "))
    if level == 1:
        count = 8
    elif level == 2:
        count = 6
    else:
        count = 4
    return count

interface()
            
