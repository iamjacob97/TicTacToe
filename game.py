from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:

    def __init__(self):
        self.board = [" " for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3 : (i+1) * 3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def view_board():
        number_board = [[str(i) for i in range(j * 3, (j+1) * 3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    
    def empty_squares(self):
        return ' ' in self.board
    
    def empty_num(self):
        return self.board.count(" ")
    
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind+1) * 3]
        if all(x == letter for x in row):
            return True
        
        col_ind = square % 3
        col = [self.board[col_ind + i*3] for i in range(3)]
        if all(x == letter for x in col):
            return True
        
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all(x == letter for x in diag1):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all(x == letter for x in diag2):
                return True
            
        return False
    

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.view_board()
    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + " makes a move to square", square) 
                game.print_board()
                print('')
                time.sleep(0.8)
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')                    
                    return letter
            letter = "O" if letter == "X" else "X"
    if print_game:
        print("It's a tie!")
             
if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    ttt = TicTacToe()
    play(ttt, x_player, o_player, print_game = True)