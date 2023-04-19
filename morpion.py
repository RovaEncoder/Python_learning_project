import random as rd

table = [
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
]

player1 = "rova"
pawn1 = " "
player2 = "pierre"
pawn2 = " "

# register of player names

liste_of_players = {
    "player1": {
        "name": player1,
        "pawn": pawn1
    },
    "player2": {
        "name": player2,
        "pawn": pawn2
    }
}


def players_input_name():
    for players in liste_of_players:
        liste_of_players[players]['name'] = input(f"Nom du joueur > ")


players_input_name()

# # Choice of pawn


def players_chosse_pawn():
    print("liste of pawn: ['#', @, $, %, *, O, X]")
    for players in liste_of_players:
        liste_of_players[players]['pawn'] = input(
            f" {liste_of_players[players]['name']} choose your pawn > ")


players_chosse_pawn()


# writing board game

def table_show():
    for i in range(3):
        for j in range(3):
            print(table[i][j], end="")
        print()


table_show()

# function to check the winner


def checkwin():
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != ' . ':
            return True

    for j in range(3):
        if table[0][j] == table[1][j] == table[2][j] != ' . ':
            return True

    if table[0][0] == table[1][1] == table[2][2] != ' . ':
        return True

    elif table[0][2] == table[1][1] == table[2][0] != ' . ':
        return True
    return False


# function to check the Draw


def checkequal():
    for i in range(3):
        for j in range(3):
            if table[i][j] == " . ":
                return False

    return True


# Random first player
alea = rd.randint(0, 1)


while True:
    start_player = liste_of_players[list(
        liste_of_players.keys())[alea]]['name']
    choice_of_case = int(
        input(f"{start_player}: enter a nomber between [0, 9] > "))
    row = (choice_of_case-1)//3
    column = (choice_of_case-1) % 3

    table[row][column] = f" {liste_of_players[f'{list(liste_of_players.keys())[alea]}']['pawn']} "
    table_show()
    # switch player :
    if alea == 1:
        start_player = liste_of_players[list(liste_of_players.keys())[alea-1]]if start_player == liste_of_players[list(
            liste_of_players.keys())[alea]] else liste_of_players[list(liste_of_players.keys())[alea]]
        alea = 0
    else:
        start_player = liste_of_players[list(liste_of_players.keys())[alea+1]] if start_player == liste_of_players[list(
            liste_of_players.keys())[alea]] else liste_of_players[list(liste_of_players.keys())[alea]]
        alea = 1

    if checkwin():
        print(f"{start_player['name']} won: congratulation !")
        break
    elif checkequal():
        print("Draw !")
        break
