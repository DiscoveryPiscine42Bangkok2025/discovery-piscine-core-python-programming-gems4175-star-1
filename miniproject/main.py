from miniproject.checkmate import checkmate #turn in to working machine (can play)

def main():
    print("--- Example 1 ---")
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1) 

    print("\n--- Example 2 ---")
    board2 = """\
..
.K\
"""
    checkmate(board2) 

    print("\n--- Custom Test (Error Handling) ---")
    board3 = """\
R...
.K..
..P.
"""
    checkmate(board3) 

if __name__ == "__main__":
    main()