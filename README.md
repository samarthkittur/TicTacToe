# TicTacToe
A minimal terminal Tic-Tac-Toe Approach
First:
```
git clone https://github.com/samarthkittur/TicTacToe
cd TicTacToe
```
To make into a terminal application, follow these bash commands:
```
$chmod +x tictactoe.py

```
Then in tictactoe.py: 
```
#!/usr/bin/env python3
```
Shell:
```
mv tictactoe.py tictactoe
mkdir -p ~/bin
cp tictactoe ~/bin
export PATH=$PATH":$HOME/bin"
```
To test it out:
```
tictactoe
```
