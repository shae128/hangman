# import required modules
from time import sleep
from os import system
from random import choice


# Ask player to select playing mode
def multiPlayer():

    desicion = input(
        " To play against Computer Press \'1\' \n To play in \'2-Player\' mode press \'2\' \n "
    )

    if desicion == "1":
        return False
    elif desicion == "2":
        return True
    else:
        print("\nPlease just enter 1 or 2! \n")
        return multiPlayer()


# In case the player wants
# to play against computer
# this function will be called
# and a word list will be created
def defineWordList():

    # initialize an empty list
    wordsList = []

    # opens words file in read-only mode
    with open("words.txt") as words:
        # read file line by line
        word = words.readline()
        while word != "":
            # append each line word list without
            # newline character
            wordsList.append(word.rstrip())
            word = words.readline()

    return wordsList


# This function will initialize
# game board to be used later on
def boardInit():

    # matrix with 13 rows and 21 columns
    hangmanBoard = [[" " for i in range(22)] for j in range(14)]

    # from this line to the end of the function,
    # the matrix cells will fill with some character
    #to help drawing hangman

    # horizontal underline, down left
    for i in range(5):
        hangmanBoard[13][i] = "_"

    # vertical lines, left
    for i in range(2, 14):
        hangmanBoard[i][1] = "|"

    # horizontal over lines, top
    for i in range(22):
        hangmanBoard[2][i] = u"\u203E"

    # horizontal over lines, base
    for i in range(16, 22):
        hangmanBoard[11][i] = u"\u203E"

    # vertical line, base left
    for i in range(11, 14):
        hangmanBoard[i][15] = "|"

    # vertical lines, base Right
    for i in range(11, 14):
        hangmanBoard[i][21] = "|"

    return hangmanBoard


# This function will draw hangman
# based on current state of the game
# higher error, more completed hangman
def drawBoard(hangmanBoard, errorNum, errorLetter=None, win=False):

    # if there is a wrong letter so put it
    # to first row of matrix to show it to user
    if errorLetter != None:
        hangmanBoard[0][errorNum - 1] = errorLetter

    # errorNum shows player wrong desicion

    # if errorNum 1
    if errorNum >= 1:
        # drawing hangman head

        # underlines head top
        for i in range(15, 22):
            hangmanBoard[3][i] = "_"

        # underlines head down
        for i in range(15, 22):
            hangmanBoard[5][i] = u"\u203E"

        # vertical line head left
        for i in range(4, 5):
            hangmanBoard[i][15] = "|'"

        # vertical line head right
        for i in range(4, 5):
            hangmanBoard[i][19] = "'|"

        # if player wins, the hangman will
        # have a tiny smile
        if win:
            hangmanBoard[4][17] = u"\u23D1"
        # if player loose, the hangman will
        # be sad
        elif win == False and errorNum == 6:
            hangmanBoard[4][17] = u"\u23DC"
        # during game hangman has normal face
        else:
            hangmanBoard[4][17] = "_"

    # if errorNum 2
    if errorNum >= 2:
        # HANDS

        # if player wins, the hangman will
        # raise his hands
        if win:
            hangmanBoard[7][17] = "\\"
            hangmanBoard[7][19] = "/"
        # otherwise his hands are down
        else:
            hangmanBoard[7][17] = "/"
            hangmanBoard[7][19] = "\\"

    # if errorNum 3
    if errorNum >= 3:
        # legs
        hangmanBoard[10][17] = "/"
        hangmanBoard[10][19] = "\\"

        # if errorNum 4
    if errorNum >= 4:
        # vertical line body
        for i in range(5, 10):
            hangmanBoard[i][18] = "|"

        # if errorNum 5
    if errorNum >= 5:
        # vertical line right, top
        for i in range(2, 4):
            hangmanBoard[i][18] = "|"

    # if errorNum 6
    if errorNum >= 6:
        # if errorNum in greater or equal
        # to six, it means the player has
        # lost the game some all base parts
        # which is under hangman legs will
        # be replace with empty string
        # so the base will be removed!
        # and the man will be hanged :(

        # over line base
        for i in range(16, 22):
            hangmanBoard[11][i] = " "

        # vertical line base, left
        for i in range(11, 14):
            hangmanBoard[i][15] = " "

        # vertical line base Right
        for i in range(11, 14):
            hangmanBoard[i][21] = " "

    # clear screen
    try:
        system('clear')  # for unix
    except:
        system('cls')  # for windows

    # print number of remaining moves
    if not win:
        print("You are " + str(6 - errorNum) +
              " moves away from hanging the man!\n")
    else:
        print("\n")

    # print a line to show wrong letters
    print("Wrong Letters:")

    # every time print out hole matrix
    for i in hangmanBoard:
        for j in i:
            print(j, end="")
        print("")
    print("")
    print("")


# This function plays the game
def gameRun(gameBoard):

    # initialize the list which will
    # be shown to player
    toPrintOut = []
    # counts wrong decisions
    errorNum = 0
    # initialize win by True
    win = True

    # call multiPlayer function to check
    # if player wants to play multiPlayer
    # mode or wants to player against computer
    if multiPlayer():
        # if multiPlayer mode, then first player
        # should pick up word, by then the screen
        # will be clear to starts playing
        while True:
            wordToGuess = input("Select your word: ").upper()

            # if the word picked up by first player
            # has less than three letter, the player
            # will be asked to pick up another word
            if len(wordToGuess) < 3:
                print("The word must contain at least 3 letters!")
            else:
                break

    # if player wants to play against computer
    # then the defineWordList function will be
    # called to make a word list
    else:
        wordList = defineWordList()
        wordToGuess = choice(wordList).upper()

    # initialize a list as big as
    # selected word, to show to user
    # number of letters and etc.
    for i in range(len(wordToGuess)):
        if wordToGuess[i] is " ":
            toPrintOut.append(" ")
        else:
            toPrintOut.append("_")

    # call drawBoard to draw game board
    # in current state
    drawBoard(gameBoard, errorNum)

    # print out current state of
    # game via a list
    for i in toPrintOut:
        print(i, end=" ")

    print("\n")

    # until player does not make
    # more than six mistakes the game
    # will goes on
    while errorNum < 6:

        # found variable will be used to
        # find white space or empty cells
        # if so, then player has not won yet
        found = False

        # take player guess
        decision = input("Enter your guess: ").upper()

        # if player enter more than a letter
        # or an empty string, he/she will be
        # prompt to enter just a letter or string
        if len(decision) == 0:
            print("Please enter a letter!")
            continue
        elif len(decision) != 1:
            print("Please enter just one letter!")
            continue

        # if entered letter is equal to
        # any letter of wordToGuess, then
        # put that letter to toPrintOut list
        # correspond cell
        for i in range(len(wordToGuess)):
            if wordToGuess[i] == decision:
                toPrintOut[i] = decision
                found = True

        # if the code doesn't find
        # entered letter in wordToGuess
        # so the player has made a wrong
        # guess
        if not found:
            errorNum += 1
            drawBoard(gameBoard, errorNum, decision + " ")
        else:
            drawBoard(gameBoard, errorNum)

        # print out current state of
        # toPrintOut list
        for i in toPrintOut:
            print(i, end=" ")

        print("\n")

        # if all cells of wordToGuess and
        # toPrintOut lists are the same
        # so the player wins
        for i in range(len(toPrintOut)):
            if toPrintOut[i] != wordToGuess[i]:
                win = False
                break
            else:
                win = True

        # if player wins, the recall drawBoard
        # function with no errorLetter and with
        # errorNum equal to 4 to let the drawBoard
        # function, draws all parts of the man with
        # raised hands and smile on the face
        if win:
            drawBoard(gameBoard, 4, None, True)
            for i in toPrintOut:
                print(i, end=" ")

            print("\n")

            # Winning message
            print("Good Job, you saved me!\n")

            # terminate function and game
            return True
    # if wrong guesses are greater than
    # or equal to 6, the player will lose
    # and game will end with this message
    else:
        print("OoOoOops, The word was", wordToGuess, "\n")


# let play!!!
gameRun(boardInit())
