from tictactoe import TicTacToe


def print_options() -> None:
    """Prints all the options in vertical order

    Args:
        options (list[str]): the list that contains all the options
    """

    options: list[str] = [
        "Computer(dumb) (vs) Player",
        "Computer(Smart) (vs) Player",
        "Player (vs) Player",
    ]

    for index in range(len(options)):

        print(f"[{index+1}] {options[index]}")


def get_option() -> list[bool]:
    """Gets the input from the user ranging from 1-3

    Returns:
        list: the required argument for each mode
    """

    options: dict = {
        "1": [True, True],
        "2": [True, False],
        "3": [False, True],
    }
    
    print_options()
    
    option = input("Enter your Gamemode:> ")
    
    if option in options:
        return options[option]
    



arguments: bool = get_option()
computer = arguments[0]
dumb = arguments[1]

obj = TicTacToe()
obj.MainGameLoop(computer=computer, dumb=dumb)
