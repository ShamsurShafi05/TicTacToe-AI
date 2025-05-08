from Board import GenerateBoard
# player, actions, result, winner, terminal, utility, and minimax.

def Player(state):
    return state.player_move
    
def Actions(state):
    list1 = []
    for i in range(len(state.board)):
        for j in range(len(state.board)):
            if state.board[i][j] is None:
                list1.append((i, j))
    return list1

def Result(state, action):
    new_state = GenerateBoard(state.size)
    new_state.board = [row.copy() for row in state.board]
    new_state.player = 2 if state.player == 1 else 1  # Switch player
    new_state.player_move = "O" if state.player_move == "X" else "X"  # Switch move symbol
    i, j = action
    new_state.board[i][j] = state.player_move
    return new_state

def Winner(state):
    for i in range(state.size):
        for j in range(state.size):
            if state.board[i][j] is not None:
                # Check horizontal
                if j + 3 < state.size and all(state.board[i][j] == state.board[i][j+k] for k in range(4)):
                    return state.board[i][j]
                # Check vertical
                if i + 3 < state.size and all(state.board[i][j] == state.board[i+k][j] for k in range(4)):
                    return state.board[i][j]
                # Check diagonal (top-left to bottom-right)
                if i + 3 < state.size and j + 3 < state.size and all(state.board[i][j] == state.board[i+k][j+k] for k in range(4)):
                    return state.board[i][j]
                # Check diagonal (bottom-left to top-right)
                if i - 3 >= 0 and j + 3 < state.size and all(state.board[i][j] == state.board[i-k][j+k] for k in range(4)):
                    return state.board[i][j]
    return None

def Terminal(state):
    if Winner(state) is not None:
        return True
    for row in state.board:
        if None in row:
            return False
    return True

def Utility(state):
    if Winner(state) == "X":
        return 1
    elif Winner(state) == "O":
        return -1
    else:
        return 0

def Minimax(state):
    if Terminal(state):
        return Utility(state), None

    if state.player == 1:           # Maximizing player (X)
        max_eval = float('-inf')
        best_move = None
        for action in Actions(state):
            eval_score, _ = Minimax(Result(state, action))
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = action
        return max_eval, best_move
    else:                           # Minimizing player (O)
        min_eval = float('inf')
        best_move = None
        for action in Actions(state):
            eval_score, _ = Minimax(Result(state, action))
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = action
        return min_eval, best_move


