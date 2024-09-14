import os, time, typewriter, random
#from pyautogui import alert
screen1 = ["1","2","3",
          "4","5","6",
          "7","8","9",]
settings = {
    "test_setting": True,
    "experimental_bot": False
}

menu_1 = """
*   Tic-Tac-Toe      
*   1. Player vs Player
*   2. Player vs Bot(experimental)
*   3. Exit
*   4. Settings"""


def who_starts():
    players = ["O", "X"]
    return random.choice(players)

def render_screen(s):
    print(s[0], s[1], s[2])
    print(s[3], s[4], s[5])
    print(s[6], s[7], s[8])

def check_winner(board):
    # Check rows
    for row in board:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)):
        return 'O'
    
    if all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    return None  # No winner yet


def set_pixel(scree , val, setable):
    if setable == "X":
        if scree[val - 1] == "O":
            #alert(text="Yritit huijata! Menetit vuoron!")
            return "Yritit huijata! Menetit vuoron!"
        else:
             scree[val - 1] = setable
    else:
        if scree[val - 1] == "X":
            #alert(text="Yritit huijata! Menetit vuoron!")
            return "Yritit huijata! Menetit vuoron!"
        else:
             scree[val - 1] = setable

def check_if_valid(arg):
    try:
        int(arg)
    except ValueError:
        return False
    return True
   
def pvp_game(xname = "X", oname = "O"):
    board = [screen1[i:i + 3] for i in range(0, 9, 3)]
    winner = check_winner(board)
    if winner:
        print(f'Voittaja on: {winner}')
        exit()
    clear()
    render_screen(screen1)
    xinput = input("Player X:")
    if check_if_valid(xinput):
        set_pixel(screen1, int(xinput), "X")
    clear()
    render_screen(screen1)
    oinput = input("Player O:")
    if check_if_valid(oinput):
        set_pixel(screen1, int(oinput), "O")

def ai_game():
    board = [screen1[i:i + 3] for i in range(0, 9, 3)]
    winner = check_winner(board)
    if winner:
        if winner == "O":
            print("AI won")
        elif winner == "X":
            print("You won!")
        exit()
    clear()
    render_screen(screen1)
    xinput = input("Player X:")
    if check_if_valid(xinput):
        set_pixel(screen1, int(xinput), "X")
    
    set_pixel(screen1, int(bot_choice(screen1)), "O")
    clear()


def randomboard(board):
    return random.choice(board)

def bot_choice(board):

    bord = randomboard(board)
    if bord == "X" or bord == "O":
        bot_choice(board)
    return bord

    
    
    



    

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def settings_menu():
    clear()
    for y in settings:
        print(y + " set to " +  str(settings[y]))
    i = input("->")
    i = i.split("=")
    for x in settings:
        if x == i[0]:
            settings[i[0]] = i[1]
            print("succesfully set to " + i[1])
    time.sleep(4)

def menu(startmsg = ""):
    clear()
    typewriter.write(startmsg+menu_1, 0.01)
    selection = input("> ")
    if selection == "1":
        while True:
            pvp_game()
    elif selection == "2":
        if not settings["experimental_bot"]:
            menu("not available")
        elif settings["experimental_bot"]:
            while True:
                ai_game()
    elif selection == "3":
        quit()
    elif selection == "4":
        settings_menu()
        

#for i in range(9):
#    for x in range(9):
#        time.sleep(0.1)
#        os.system("clear")
#        set_pixel(screen1, i + 1, x + 1)
#        
#        render_screen(screen1)

while True:
    menu()

