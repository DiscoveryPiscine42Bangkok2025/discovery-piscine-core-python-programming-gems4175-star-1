def checkmate(board: str):
    # จัดการ String ของกระดาน
    lines = board.split('\n')
    # ลบบรรทัดว่างที่อาจเกิดจากการพิมพ์ """
    rows = [line.replace('\\', '') for line in lines if line]
    
    if not rows:
        return

    height = len(rows)
    # ตรวจสอบว่าเป็นสี่เหลี่ยมจัตุรัสหรือไม่
    if any(len(row) != height for row in rows):
        print("Error")
        return

    # หาพิกัดของ King
    k_pos = None
    k_count = 0
    for r in range(height):
        for c in range(height):
            if rows[r][c] == 'K':
                k_pos = (r, c)
                k_count += 1
                
    # ต้องมี King แค่ตัวเดียวเท่านั้น
    if k_count != 1 or k_pos is None:
        print("Error")
        return

    k_r, k_c = k_pos
    
    # หมากศัตรูตาม Pattern ในรูปภาพ
    valid_pieces = ['P', 'B', 'R', 'Q']

    # ฟังก์ชันสำหรับจำลองการยิง Ray (เส้นสายตา) ออกจาก King ไปยังทิศต่างๆ
    def is_attacked_from(dr, dc, enemies):
        r, c = k_r + dr, k_c + dc
        while 0 <= r < height and 0 <= c < height:
            piece = rows[r][c]
            if piece in valid_pieces:
                if piece in enemies:
                    return True # โดนหมากศัตรูที่กินในทิศนี้ได้
                else:
                    return False # มีหมากตัวอื่นบังอยู่
            # ถ้าเป็นตัวอักษรอื่นถือว่าเป็นช่องว่าง ให้ทะลุผ่านไปเช็คช่องถัดไป
            r += dr
            c += dc
        return False

    # 1. เช็ค Rook และ Queen (ทิศตรง: บน, ล่าง, ซ้าย, ขวา)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if is_attacked_from(dr, dc, ['R', 'Q']):
            print("Success")
            return

    # 2. เช็ค Bishop และ Queen (ทิศทแยง: 4 มุม)
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if is_attacked_from(dr, dc, ['B', 'Q']):
            print("Success")
            return

    # 3. เช็ค Pawn (P)
    # ตามภาพ Pattern ของ Pawn: ทิศทางการกินคือแนวทแยงขึ้น (Row ลดลง 1, Col +/- 1)
    # ดังนั้นเมื่อมองจากมุม King, Pawn ที่จะมากินได้จะต้องอยู่ด้านล่างของ King (Row + 1)
    for dc in [-1, 1]:
        pawn_r, pawn_c = k_r + 1, k_c + dc
        if 0 <= pawn_r < height and 0 <= pawn_c < height:
            if rows[pawn_r][pawn_c] == 'P':
                print("Success")
                return

    # หากรอดจากทุกเงื่อนไข แปลว่าไม่ถูก Check
    print("Fail")
