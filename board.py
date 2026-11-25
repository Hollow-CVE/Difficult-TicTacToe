



class GameBoard():
    '''This class is responsible for the board ui'''
    
    
    def PrintBoard_boring(self, board: list[int]) -> None:
            """Just prints the boring board"""
    
            print(f" {board[0]}  | {board[1]} |  {board[2]}")
            print(f"----|---|----")
            print(f" {board[3]}  | {board[4]} |  {board[5]}")
            print(f"----|---|----")
            print(f" {board[6]}  | {board[7]} |  {board[8]}")
            
            
            
