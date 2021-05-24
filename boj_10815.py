n = int(input())
p_card_deck = set(list(map(int, input().split())))
m = int(input())
w_card_deck = set(list(map(int, input().split())))

for i in w_card_deck:
    if i in p_card_deck:
        print(1, end = " ")
    else:
        print(0, end = " ")
