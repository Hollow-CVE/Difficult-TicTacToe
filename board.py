from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text


class GameBoard():
    '''This class is responsible for the board ui'''


    
    def PrintBoard_boring(self, board: list[int]) -> None:
        """Just prints the boring board"""

        print(f" {board[0]}  | {board[1]} |  {board[2]}")
        print(f"----|---|----")
        print(f" {board[3]}  | {board[4]} |  {board[5]}")
        print(f"----|---|----")
        print(f" {board[6]}  | {board[7]} |  {board[8]}")



    # I used help creating this board because i'm not good at designing UIs
    def PrintBoard_rich(self, board: list) -> None:
        """Prints a minimalist board using the rich module"""

        console = Console()

        table = Table(
            show_header=False,
            show_lines=True,
            box=box.MINIMAL,            
            border_style="grey37",
            # you can adjust the padding
            padding=(1, 3),              
        )

        for _ in range(3):
            table.add_column(justify="center", no_wrap=True)

        def style_cell(value, index: int) -> Text:
            if value == "X":
                return Text("X", style="bold red")
            if value == "O":
                return Text("O", style="bold blue")
            return Text(str(index + 1), style="grey35")

        for row in range(3):
            cells = [style_cell(board[row * 3 + col], row * 3 + col) for col in range(3)]
            table.add_row(*cells)

        console.print()
        console.print(table, justify="center")
        console.print()
        
        
        
    