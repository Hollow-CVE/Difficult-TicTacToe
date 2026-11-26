import argparse

from tictactoe import TicTacToe

# This is very important it helps both in displaying the options and also in the get_args function
MODES = {
    "1": ("Computer (dumb) vs Player", [True, True]),
    "2": ("Computer (smart) vs Player", [True, False]),
    "3": ("Player vs Player", [False, True]),
}


def get_args() -> argparse.Namespace:
    """Get the command line arguments. If user don't like the interactive menu the user can user this instead."""

    # So, i'm using this apprach because the user can select one mode at a time and

    parser = argparse.ArgumentParser(description="Tic Tac Toe Game")
    parser.add_argument(
        "-b",
        "--boring",
        action="store_true",
        help="Use the boring board instead of the boring one",
    )
    
    parser.add_argument(
            "-c",
            "--corner",
            action="store_true",
            help="don't let the smart computer to always select the center of the board",
        )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-d",
        "--dumb",
        action="store_const",
        dest="mode",
        const="1",
        help="Play against the dumb computer",
    )
    group.add_argument(
        "-s",
        "--smart",
        action="store_const",
        dest="mode",
        const="2",
        help="Play against the smart computer",
    )
    group.add_argument(
        "-u",
        "--user",
        action="store_const",
        dest="mode",
        const="3",
        help="Play against another user",
    )

    return parser.parse_args()


def get_option() -> list[bool]:
    """Ask the user to pick a game mode (1-3) and return [computer, dumb]."""

    # this looks a little bit complex but it is just displaying the options
    for key, (label, _) in MODES.items():
        print(f"[{key}] {label}")

    while True:
        try:
            option = input("Enter your Gamemode:> ").strip()
        except KeyboardInterrupt:
            exit(0)

        
        
        if option in MODES:
            return MODES[option][1]
        print("Invalid option, please try again!")


def main() -> None:
    args = get_args()

    # if the user has inputed the value using thet cammand line
    if args.mode is not None:
        computer, dumb = MODES[args.mode][1]
        
    # if not then we will provide an interactive menu for the user
    else:
        computer, dumb = get_option()

    TicTacToe().MainGameLoop(computer=computer, dumb=dumb, boring=args.boring, corner=args.corner)


if __name__ == "__main__":
    main()
