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
        if state.board[i][0] == state.board[i][1] == state.board[i][2] is not None:
            return state.board[i][0]
        if state.board[0][i] == state.board[1][i] == state.board[2][i] is not None:
            return state.board[0][i]
    if state.board[0][0] == state.board[1][1] == state.board[2][2] is not None:
        return state.board[0][0]
    if state.board[0][2] == state.board[1][1] == state.board[2][0] is not None:
        return state.board[0][2]
    return None
    # if "X" returned, state.player = 1
    # if "O" returned, state.player = 2

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


