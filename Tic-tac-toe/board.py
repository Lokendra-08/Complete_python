class Board:
    EMPTY_CELL = 0
    def __init__(self):
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
    def print_board(self):
        print("Positions :")
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
        print()

        print("Board : ")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()
    
    def submit_move(self, player, move):

        row = move.get_row()
        col= move.get_column()
        value = self.game_board[row][col]

        if value == self.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("Position is already taken.")

    def check_game_over(self, player, last_move):
        return ((self.check_row(player, last_move)) or (self.check_column(player, last_move)) or (self.check_diagonal(player)) or (self.check_antidiagonal(player)))
    
    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]

        return board_row.count(player.marker) == 3
    
    def check_column(self, player, last_move):

        marker_count = 0
        col_index = last_move.get_column()

        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                marker_count+= 1
        return marker_count == 3
    
    def check_diagonal(self, player):
        marker_count= 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                marker_count+= 1
        return marker_count == 3
    
    def check_antidiagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                marker_count+= 1
        return marker_count == 3
    
    def check_tie(self):
        empty_count = 0
        for row in self.game_board:
            empty_count+= row.count(Board.EMPTY_CELL)
        return empty_count == 0 
    
    def reset(self):
        self.game_board= [[0,0,0],
                           [0,0,0],
                           [0,0,0]]

