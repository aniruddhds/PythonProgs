def validate_board(boardDict):
    # check for one black and one white king
    if "bking" not in boardDict.values() or "wking" not in boardDict.values():
        return False

    # check for a maximum of 16 pieces per player
    black_pieces = 0
    white_pieces = 0
    for colour in boardDict.values():
        if colour[0] == "b":
            black_pieces += 1
        elif colour[0] == "w":
            white_pieces += 1
    if black_pieces >= 17 or white_pieces >= 17:
        return False
    # check for at most 8 pawns per player
    bpawn_count = 0
    wpawn_count = 0

    for piece in boardDict.values():
        if piece == "bpawn":
            bpawn_count += 1
        elif piece == "wpawn":
            wpawn_count += 1

    if bpawn_count >= 9 or wpawn_count >= 9:
        return False
        
    # check for a valid location
    board_keys = []
    for k in boardDict.keys():
        board_keys.append(k)  # create list of dictionary keys. 
    y = ["1", "2", "3", "4", "5", "6", "7", "8"]
    board_y = [s[:1] for s in board_keys]  # removes letters from list.
    for elem in board_y:
        if elem not in y:
            return False

    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board_x = [s[1:] for s in board_keys]  # removes numbers from list. eg: ['h', 'c', 'g', 'h', 'e']
    if not all(elem in x for elem in board_x):  # checks if all values from board_x are in the x-list
        return False

    # check if the name starts with a "w" or "b"
    for pieces in boardDict.values():
        if pieces[0] != "b" and pieces[0] != "w":
            return False

    # check if the piece name is valid
    piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for names in boardDict.values():
        if names[1:] not in piece_names:
            return False
    return True

testBoard={"1h": "bking", "6": "wqueen", "1h": "bbishop", "6h": "bqueen", "3e": "wking"}
print(f"Board for testing: {testBoard}")
print(validate_board(testBoard))
