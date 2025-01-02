from player import Player
from board import Board


class Game:

    def start(self):
        print("**********************")
        print("Welcome to Tic-Tac-Toe")
        print("**********************")
        print()

        board=Board()
        human= Player()
        computer= Player(False)

        board.print_board()

        while True:     
            s=set()
            while True:     
                human_move = human.get_move()
                while human_move.value in s:
                    print("Position is already occupied. Enter again")
                    human_move=human.get_move()
                else:
                    s.add(human_move.value)
                    board.submit_move(human, human_move)
                    board.print_board()
                if board.check_game_over(human, human_move):
                    print("Congratulations! YOU WON THE GAME")
                    break
                elif board.check_tie():
                    print("It's a tie. Please try again!")
                    break
                else:
                    computer_move = computer.get_move()
                    while computer_move.value in s:
                        computer_move=computer.get_move()     
                    else:
                        s.add(computer_move.value)
                        board.submit_move(computer, computer_move)
                        board.print_board()
                    if board.check_game_over(computer, computer_move):
                        print("Oops.. The computer won. Try again")
                        break

            play_again = input("Would you like to play again ? \n Press Y for yes or N for no.").upper()

            if play_again == "N":
                print("Bye bye")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Invalid input")

    def start_new_round(self, board):
        print("**********")
        print("     New Round    ")
        print("**********")
        board.reset()
        board.print_board()

game= Game()
game.start()