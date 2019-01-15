from time import sleep
from os import system


def boardInit():

    hangmanBoard = [[" " for i in range(22)] for j in range(14)]

    # over line upper
    for i in range(22):
        hangmanBoard[2][i] = u"\u203E"

    # underline down
    for i in range(5):
        hangmanBoard[13][i] = "_"
    # vertical line left
    for i in range(2, 14):
        hangmanBoard[i][1] = "|"

    # over line sit
    for i in range(16, 22):
        hangmanBoard[11][i] = u"\u203E"

    # vertical line sit left
    for i in range(11, 14):
        hangmanBoard[i][15] = "|"

    # vertical line sit Right
    for i in range(11, 14):
        hangmanBoard[i][21] = "|"

    return hangmanBoard


def drawBoard(hangmanBoard, errorNum, errorLetter=None):

    if errorLetter != None:
        hangmanBoard[0][errorNum-1] = errorLetter

    # if errorNum 1
    if errorNum >= 1:
        # underline head up
        for i in range(15, 22):
            hangmanBoard[3][i] = "_"

        # underline head down
        for i in range(15, 22):
            hangmanBoard[5][i] = u"\u203E"

        # vertical line head left
        for i in range(4, 5):
            hangmanBoard[i][15] = "|'"

        # vertical line head right
        for i in range(4, 5):
            hangmanBoard[i][19] = "'|"

        # underline lips
        # hangmanBoard[4][17] = u"\u23DC"
        hangmanBoard[4][17] = "_"
        # hangmanBoard[4][17] = u"\u23D1"

        # if errorNum 2
    if errorNum >= 2:
        # hands
        hangmanBoard[7][17] = "/"
        hangmanBoard[7][19] = "\\"
        # hangmanBoard[7][17] = "\\"
        # hangmanBoard[7][19] = "/"

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
        # vertical line right
        for i in range(2, 4):
            hangmanBoard[i][18] = "|"

        # if errorNum 6
    if errorNum >= 6:
        # over line sit
        for i in range(16, 22):
            hangmanBoard[11][i] = " "

        # vertical line sit left
        for i in range(11, 14):
            hangmanBoard[i][15] = " "

        # vertical line sit Right
        for i in range(11, 14):
            hangmanBoard[i][21] = " "

    # clear screen
    try:
        system('clear')  # for unix
    except:
        system('cls')  # for windows

    print("You are " + str(6 - errorNum) + " moves away from hanging the man!\n")
    print("Mistakes:")


    for i in hangmanBoard:

        for j in i:
            print(j, end="")

        print("")

    print("")
    print("")


gameBoard = boardInit()

# for i in range(7):
#     drawBoard(gameBoard, i)
#     sleep(1)


def gameRun():

    wordToGuess = list(input("Select your word: ").upper())
    toPrintOut = []
    errorNum = 0

    for i in range(len(wordToGuess)):
        if wordToGuess[i] is " ":
            toPrintOut.append(" ")
        else:
            toPrintOut.append("_")

        drawBoard(gameBoard, errorNum)

        for i in toPrintOut:
            print(i, end=" ")

        print("\n\n\n")

    while errorNum < 6:
        found = False
        decision = input("Enter your guess: ").upper()

        if len(decision) != 1:
            print("Please enter just one letter.")
            continue

        for i in range(len(wordToGuess)):
            if wordToGuess[i] == decision:
                toPrintOut[i] = decision
                found = True

        if not found:
            errorNum += 1

        drawBoard(gameBoard, errorNum, decision + " ")

        for i in toPrintOut:
            print(i, end=" ")

        print("\n\n\n")


gameRun()
