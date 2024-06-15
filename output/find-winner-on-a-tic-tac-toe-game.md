



# Find Winner on a Tic Tac Toe Game

## Link
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/

## Where
Leetcode

## Difficulty
Easy

## Description
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

## Solution Main Idea
Solution 1 is to brute force check all cells after each move
Solution 2 is to treat "A" as adding 1, "B" as removing 1 to each row,col it affects. -3 means all "B", 3 means all "A"



## Code

```python
class Solution:
    def checkWin(self,grid):
        checks = [
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)], 
            [(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)]
        ]
        for check in checks:
            if all([grid[row][col] == "A" for row,col in check]):
                return "A"
            if all([grid[row][col] == "B" for row,col in check]):
                return 'B'
        return None
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[-1] * 3 for i in range(3)]
        turn = "A"
        for move in moves:
            row = move[0]
            col = move[1]
            grid[row][col] = turn
            result = self.checkWin(grid)
            if result is not None:
                return result
            turn = "A" if turn =="B" else "B"
        if len(moves) < 9:
            return "Pending"
        return "Draw"
    

class Solution:
    def checkWin(self,rows, cols, diag, antiDiag):
        def determineWinner(val):
            if val == 3:
                return "A"
            elif val == -3:
                return "B"
            return None

        for row in rows:
            winner = determineWinner(row)
            if winner:
                return winner

        for col in cols:
            winner = determineWinner(col)
            if winner:
                return winner

        winner = determineWinner(diag)
        if winner:
            return winner
        winner = determineWinner(antiDiag)
        if winner:
            return winner

        return None



    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        antiDiag = 0

        turn = "A"

        for move in moves:
            row = move[0]
            col = move[1]
            if turn == "A":
                rows[row] += 1
            else:
                rows[row] -= 1
            
            if turn == "A":
                cols[col] += 1
            else:
                cols[col] -= 1
            
            if row == col:
                if turn == "A":
                    diag += 1
                else:
                    diag -= 1
            
            if row == 2 - col:
                if turn == "A":
                    antiDiag += 1
                else:
                    antiDiag -= 1

            result = self.checkWin(rows,cols,diag,antiDiag)
            if result is not None:
                return result
            turn = "A" if turn == "B" else "B"
        
        if len(moves) < 9:
            return "Pending"
        return "Draw"








```
