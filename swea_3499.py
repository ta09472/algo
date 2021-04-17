t = int(input())
for i in range(1,t+1):
    n = int(input())
    deck_list = list(input().split())
    result = []
    top_card = 0
    middle_card = (n+1) // 2
    for k in range(n//2):
        result.append(deck_list[top_card])
        result.append(deck_list[middle_card])
        top_card, middle_card = top_card + 1, middle_card + 1
    if n % 2:
        result.append(deck_list[n//2])

    print(f"#{i}", *result, sep = " ")
