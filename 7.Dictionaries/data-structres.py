def validateGame(board, player) :
    if board['top-L']==player and board['top-M']==player and board['top-R']==player or \
        board['mid-L']==player and board['mid-M']==player and board['mid-R']==player or \
        board['low-L']==player and board['low-M']==player and board['low-R']==player :
        return 'win'
    if board['top-L']==player and board['mid-M']==player and board['low-R']==player or \
        board['top-R']==player and board['mid-M']==player and board['low-L']==player or \
        board['top-M']==player and board['mid-M']==player and board['low-M']==player :
        return 'win'
    if board['top-L']==player and board['mid-L']==player and board['low-L']==player or \
        board['top-M']==player and board['mid-M']==player and board['low-M']==player or \
        board['top-R']==player and board['mid-R']==player and board['low-R']==player :
        return 'win'

def prints(board) :
    print('----------')
    print('|', board['top-L'], '|', board['top-M'], '|', board['top-R'], '|')
    print('----------')
    print('|', board['mid-L'], '|', board['mid-M'], '|', board['mid-R'], '|')
    print('----------')
    print('|', board['low-L'], '|', board['low-M'], '|', board['low-R'], '|')
    print('----------')

board = {'top-L':'', 'top-M':'', 'top-R':'',
    'mid-L':'', 'mid-M':'', 'mid-R':'',
    'low-L':'', 'low-M':'', 'low-R':''
    }

player = 'X'
old_player = player
decision = ''
while True :
    prints(board)
    if decision == 'win' :
        print('Player ', old_player, 'won')
        break
    print('Player ', player , 'move : ')
    move = input()
    if board[move] == '' :
        board[move] = player
        decision = validateGame(board, player)
        old_player = player
        player = 'X' if player == 'O' else 'O'


