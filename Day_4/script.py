import numpy as np

with open('input.txt', 'r') as f:
    draws = np.loadtxt(f,delimiter=',',max_rows=1, dtype='uint8')
    boards = np.loadtxt(f, skiprows=1, dtype='uint8')

boardSize = boards.shape[1]
nbBoards = boards.shape[0]/boardSize
# Second argument is the number of arrays we want extracted from boards
boards = np.array_split(boards,nbBoards)
# Turn the list of 100 5*5 arrays to a 5*5*100 array 
boards = np.stack(boards,axis=2)
# This array will store wether the case at the (i,j,k) position has been marked before
boardsMarked = np.zeros(boards.shape,dtype=bool)

# =============================================================================
# PART 1
# =============================================================================

def isBoardWin(boardMarked):
    
    # Check horizontal lines
    for i in range(boardMarked.shape[0]):
        if np.sum(boardMarked[i,:]) == boardMarked.shape[0]:
            return True
        
    # Check vertical lines
    for i in range(boardMarked.shape[1]):
        if np.sum(boardMarked[:,i]) == boardMarked.shape[1]:
            return True

    return False

# directly modifies boardMarked, so no return
def markBoard(numberToMark,board,boardMarked):
    
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i,j] == numberToMark:
                boardMarked[i,j] = True

    
winningBoard = -1
winningBoardMarked = -1
won = False
for idx,draw in enumerate(draws):
    # Check if we already drew this number
    if draw in draws[:idx]:
        continue
    
    # If not, iterate on the depth (aka on the boards)
    for k in range(boardsMarked.shape[2]):
        
        board = boards[:,:,k]
        boardMarked = boardsMarked[:,:,k]
        
        markBoard(draw,board,boardMarked)
        # No need to check if the number of draws so far is 4 or less
        # Could be optimized by separating the loop on the draws in two loops
        # (from 0 to boardSize-1) and (from boardSize-1 to the end)
        # => no calls to isBoardWin in the first, and no check if idx >= boardSize-1
        # in the second one, but lets keep this simple
        if idx >= boardSize-1 and isBoardWin(boardMarked):
            winningBoard = board
            winningBoardMarked = boardMarked
            won = True
            break
    
    if won:
        sumUnmarked = sum(winningBoard[np.invert(winningBoardMarked)])
        score = draw * sumUnmarked
        print(score) # 67,716
        break

# =============================================================================
# PART 2
# =============================================================================
