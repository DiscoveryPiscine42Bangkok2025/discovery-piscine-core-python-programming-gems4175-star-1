from checkmate import checkmate

def main():
    print("--- Example 1 ---")
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1) # คาดหวังผลลัพธ์: Success (เพราะ Pawn ที่ 2,2 กิน K ที่ 1,1 ได้)

    print("\n--- Example 2 ---")
    board2 = """\
..
.K\
"""
    checkmate(board2) # คาดหวังผลลัพธ์: Fail (ไม่มีศัตรู)

    print("\n--- Custom Test (Error Handling) ---")
    board3 = """\
R...
.K..
..P.
"""
    checkmate(board3) # คาดหวังผลลัพธ์: Error (เพราะไม่ใช่จัตุรัส 3x4)

if __name__ == "__main__":
    main()