import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if 'value' is between 'min_value' and 'max_value',
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    
    ## making sure value is between min_balue and max_value
    return value <= max_value and value >= min_value
        

def game_board_full(game_board):
    
    """(str) -> bool
    
    Return True if and only if the 'game_board' is full, which means that
    the string arugument for the paramater does not contain '-'
    
    >>> game_board_full("XOXOOXXXO")
    True
    >>> game_board_full("XOX-OX-XO")
    False
    """
    
    if game_board.find(EMPTY) == -1:      ## -1 means that EMPTY is not found
        return True
    else:
        return False

def get_board_size(game_board):
    
    """(str) -> int

    Precondition: the board must be perfect size (so the string argument must
    be an interger when square rooted
    
    Return the side length of the board based on the given string parameter 
    "game_board"
    
    >>>get_board_size("---------")
    3
    >>>get_board_size("X--XX--O--OO---X")
    4
    """
    
    ## Using int() is a lazy way to change the float type result 
    ##from math.sqrt() to int type
    return int(math.sqrt(len(game_board)))  

def make_empty_board(board_size):
    
    """(int) -> str
    
    Return a string value that represent an empty game board based on 
    the board size given in the parameter
    
    >>>make_empty_board(3)
    ---------
    >>>make_empty_board(5)
    -------------------------    
    """
    
    return "-" * board_size * board_size
    
def get_position(row,column,board_size):
    
    """(int,int,int) -> int
    
    Return an index of the string that represent the position on a game board
    given parameters 'row' and 'column' number and 'board_size'
    
    >>>get_position(3,3,6)
    14
    >>>get_position(1,2,4)
    1
    """
    
    return (row - 1) * board_size + column - 1

def make_move(symbol, row, column, game_board):
    
    """(str,int,int,str) -> str
    
    Return an updated string representing the 'game_board' after 
    inserting the 'symbo'l into the designated position on the board determined
    by 'row' and 'column'
    
    >>>make_move("X",2,4,"X--O-----------X")
    X--O---X-------X
    
    >>>make_move("O",3,3,"OXX-OX---")
    OXX-OX--O
    """
    
    length_of_game_board = len(game_board)

    position = get_position(row , column , get_board_size(game_board))
    
    ##return the new game board after making a move
    return game_board[0:position] + symbol + game_board[position + 1 :
                                                        len(game_board)]

def extract_line(game_board, line,line_number):
    
    """(str,str,int) -> str
    
    Return the line that is being extracted as a string, the 'line' is 
    determined by the arugument for line which is described by 'down', 
    'across', 'down_diagonal' or 'up_diagonal', 'down' and 'across' is
    accompanied with a 'line_number' that tells which row or column
    that is to be extracted.
    
    >>> extract_line("-O-X-O--X-", "across", 2)
    X-O
    >>>extract_line("XO---XXO---OX---","down_diagonal", 0)
    XX--
    """
    
    board_size = get_board_size(game_board)
    
    if line == "across":
        ## extract a row by using a start index for the first string in the row
        start_index = board_size * (line_number-1)
        return game_board[start_index : start_index + board_size]
    
    elif line == "down":
        return game_board[line_number - 1 : len(game_board) : board_size]
    
    elif line == 'down_diagonal':
        return game_board[: len(game_board) : board_size + 1]
    
    elif line == 'up_diagonal':
        x = board_size
        y = 1
        up_diagonal_line = ''
        ##extract the up diagonal line using x and y co-ordinates
        while x > 0:
            up_diagonal_line += game_board[get_position(x , y , 
                                                   get_board_size(game_board))]
            x -= 1
            y += 1
        return up_diagonal_line