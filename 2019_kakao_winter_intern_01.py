def solution(board, moves):
    answer = 0
    bag = []
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                bag.append(board[row][move-1])
                board[row][move-1] = 0
                break

        if len(bag) >= 2:
            if bag[-1] == bag[-2]:
                bag.pop()
                bag.pop()
                answer += 2

    return answer
