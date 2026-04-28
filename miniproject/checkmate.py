def checkmate(board: str):
    
    lines = board.split('\n')
    
    rows = [line.replace('\\', '') for line in lines if line]
    
    if not rows:
        return

    height = len(rows)
    
    if any(len(row) != height for row in rows):
        print("Error")
        return

    
    k_pos = None
    k_count = 0
    for r in range(height):
        for c in range(height):
            if rows[r][c] == 'K':
                k_pos = (r, c)
                k_count += 1
                
    
    if k_count != 1 or k_pos is None:
        print("Error")
        return

    k_r, k_c = k_pos
    
    
    valid_pieces = ['P', 'B', 'R', 'Q']

    
    def is_attacked_from(dr, dc, enemies):
        r, c = k_r + dr, k_c + dc
        while 0 <= r < height and 0 <= c < height:
            piece = rows[r][c]
            if piece in valid_pieces:
                if piece in enemies:
                    return True 
                else:
                    return False 
            
            r += dr
            c += dc
        return False

    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if is_attacked_from(dr, dc, ['R', 'Q']):
            print("Success")
            return

    
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if is_attacked_from(dr, dc, ['B', 'Q']):
            print("Success")
            return

   
    for dc in [-1, 1]:
        pawn_r, pawn_c = k_r + 1, k_c + dc
        if 0 <= pawn_r < height and 0 <= pawn_c < height:
            if rows[pawn_r][pawn_c] == 'P':
                print("Success")
                return

    
    print("Fail")
