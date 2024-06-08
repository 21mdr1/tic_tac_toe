import random

class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.mode = 1
        self.turn = 1
        self.winner = 0
    
    def make_move(self):

        if self.turn == 2 and self.mode == 2:
            self.computer_move()
            return

        self.print_board()

        column_key = {
            '1': 0,
            '2': 1,
            '3': 2
        }

        row_key = {
            'a': 0,
            'b': 1,
            'c': 2
        }

        while True:
            if self.mode == 1:
                move = ''.join(input(f"Player {self.turn}, what is your move? (Type help or h for a list of moves)\n").strip().lower().split())
            else:
                move = ''.join(input(f"What is your move? (Type help or h for a list of moves)\n").strip().lower().split())

            if move == "help" or move == 'h':
                self.print_help_text()
                continue
            if len(move) != 2 or move[0] not in row_key or move[1] not in column_key:
                print('That is not a valid move.\n')
                continue
            
            row = row_key[move[0]]
            column = column_key[move[1]]

            if self.board[row][column] > 0:
                print('That space is already occupied.\n')
                continue

            self.board[row][column] = self.turn

            if self.turn == 1:
                self.turn = 2
            else: self.turn = 1

            break

    def computer_move(self):

        key = {
            0: lambda x: (0, x),
            1: lambda x: (1, x),
            2: lambda x: (2, x),
            3: lambda x: (x, 0),
            4: lambda x: (x, 1),
            5: lambda x: (x, 2),
            6: lambda x: (x, x),
            7: lambda x: (x, 2 - x),
        }

        notLosingMoves = []
        okMoves = []

        rows = \
            self.board + \
            [[row[i] for row in self.board] for i in range(3)] + \
            [[self.board[i][i] for i in range(3)]] + \
            [[self.board[i][2-i] for i in range(3)]]

        for i, row in enumerate(rows):
            if 0 not in row or sum(row) == 0:
                continue
            
            if sum(row) == 4:
                position = -1
                for j in range(3):
                    if row[j] == 0:
                        position = j
                        break
                # we prioritize winning moves
                x, y = key[i](position)
                self.board[x][y] = 2
                self.turn = 1
                return

            if sum(row) == 2 and (row[1] == 1 or row[2] == 1):
                # we save notLosing moves
                position = -1
                for j in range(3):
                    if row[j] == 0:
                        position = j
                        break
                notLosingMoves.append(key[i](position))
                continue
            
            if sum(row) == 2:
                # we try to move towards three in a row
                position = -1
                for j in range(3):
                    if row[j] == 0:
                        position = j
                        break

                okMoves.append(key[i](position))
                continue 
        
        if len(notLosingMoves) > 0:
            x, y = notLosingMoves[0]
            self.board[x][y] = 2
            self.turn = 1
            return

        if len(okMoves) > 0:
            x, y = random.choice[okMoves]
            self.board[x][y] = 2
            self.turn = 1
            return

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.board[x][y] == 0:
                self.board[x][y] = 2
                self.turn = 1
                return


    def play_game(self):
        self.intro()

        while not self.game_is_over():
            self.make_move()

        self.outro()

    def intro(self):
        print('Welcome to TIC TAC TOE!')
        while True:
            print((
                'Would you like to play:\n'
                '   [1] With a friend\n'
                '   [2] Against the computer\n'
            ))
            mode = input('Your choice: ').strip().lower()

            if mode not in ["1", "2"]:
                print("That is not a valid choice.\n")
                continue
            
            self.mode = int(mode)
            break
    
    def outro(self):
        self.print_board()

        if self.winner == 3:
            win_line = 'It was a tie!'
        elif self.mode == 2:
            if self.winner == 1:
                win_line = 'You won!'
            else:
                win_line = 'The computer won!'
        else:
            win_line = f'Player {self.winner} won!'


        print((
            '----- GAME OVER -----\n'
            '' + win_line + '\n'
            'Good game! Come back to play any time\n'
        ))

    def game_is_over(self):
        # we're only checking the player who just moved, 
        # since they're the only ones who could have won
        # self.turn is set to the next player

        its_a_tie = True
        if self.turn == 1:
            player = 2
        else: player = 1

        rows = \
            self.board + \
            [[row[i] for row in self.board] for i in range(3)] + \
            [[self.board[i][i] for i in range(3)]] + \
            [[self.board[i][2-i] for i in range(3)]]

        for row in rows:
            if 0 in row:
                its_a_tie = False
                continue
            elif self.turn not in row:
                self.winner = player
                return True
        
        if its_a_tie:
            self.winner = 3
            return True

        return False

    def print_help_text(self):
        print((
        f' A1 | A2 | A3 \n'
         '---- ---- ----\n'
        f' B1 | B2 | B3 \n'
         '---- ---- ----\n'
        f' C1 | C2 | C3 \n'
        ))

    def print_board(self):
        key = [' ', 'O', 'X']

        print((
        f' {key[self.board[0][0]]} | {key[self.board[0][1]]} | {key[self.board[0][2]]}\n'
        '--- --- ---\n'
        f' {key[self.board[1][0]]} | {key[self.board[1][1]]} | {key[self.board[1][2]]}\n'
        '--- --- ---\n'
        f' {key[self.board[2][0]]} | {key[self.board[2][1]]} | {key[self.board[2][2]]}\n'
        ))


game = Game()
game.play_game()