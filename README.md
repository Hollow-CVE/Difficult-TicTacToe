# Difficult_TicTacToe

---

This is not any python TicTacToe. I codded my own algorithm to add hard modes. It currently Have two hard modes. Check it out and try to win against both two modes.

This is a simple TicTacToe with three modes. These modes are:

```
["Computer(dump) (vs) Player","Computer(Smart) (vs) Player",  "Player (vs) Player"]
```

1.  Player vs Player
2.  Computer(dumb)
3.  Computer(Smart)

So, i'm going to breakdown into each mode one by one.

## Player vs Player

This mode is one of the most simplest mode. This mode allows two player to play with each other. I used even and odd logic to determine the turn of each player.

## Computer(dumb)

This mode is more simpler then the Player vs Player. The logic of dumb computer is extremely simpler like very simple. It don't know about anything about tictactoe. It is brainless computer and just gives us random moves from all the available moves

## Computer(smart)

This is the mode that is smarter then the dumb computer and it might be smarter then you. Its logic is very linear. It just filter best move one by one from all the available moves. It's logic is not so great but I will try to improve it in future

## Basic Working

The dump computer just plays random moves as I discussed earlier. But the smart computer uses a little bit of strategy. The strategy that the smart computer uses is mix of offensive and deffensive strategy. Ai will use the self.wins list to for it's strategy in defensive and it will automatically detech that if the player is making nay move that is in the sellf.wins list. If player is trying to make any move then it will block it. But in the offensive strategy computer will try to make the move that are in self.wins

## Installation

Difficult-TicTacToe uses rich module for it's fancy board and also the printing of text on console.
In order to run the program you have to install rich

```bash
pip install rich
```

## Arguments Options

You can select the options using cammand line and it is much better then the interactive menu. the interactive menu is much limited. You can change many stuff using the cammand line that you can't do with the interactive menu

## To run the code in interactive module

If you want to use the interactive mode instead of cammand line you can run main.py without any args

```bash
python main.py
```

## -h argument (help)

By using -h argument or --help argument you can view all Arguments.

```bash
python main.py -h
```

## -b arguments (boring board)

If you don't prefer fancy board then you change the board to boring one.

```bash
python main.py -b
```

## boring Board layout

```bash
 1  | 2 |  3
----|---|----
 4  | 5 |  6
----|---|----
 7  | 8 |  9
```

## -c argument (corner)

Normally the smart ai choose always the centre you can prevent this by using -c argument

```bash
python mian.py -c
```

## -d argument (dumb ai)

To choose dumb ai game mode you can use -d argument

```bash
python main.py -d
```

## -s argument (smart ai)

To play against smart ai mode you can use -s argument

```bash
python main.py -s
```

## -u argument (multiplayer mode)

To play against another real player

```bash
python main.py
```

---

## Release 1.0

Fixed some bugs in TicTacToeAi.py
