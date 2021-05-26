# from bisect import bisect_left, bisect_right
#
# def range_count(array, left_value, right_value):
#     left_index = bisect_left(array,left_value)
#     right_index = bisect_right(array, right_value)
#     return right_index - left_index
#
# n = int(input())
# w_card_deck = sorted(list(map(int, input().split())))
# m = int(input())
# p_card_deck = list(map(int, input().split()))
#
# for i in p_card_deck:
#     print(range_count(w_card_deck, i, i), end = " ")

from collections import Counter

n = int(input())
w_card_deck = list(map(int, input().split()))
m = int(input())
p_card_deck = list(map(int, input().split()))
ans = Counter(w_card_deck)
for i in p_card_deck:
    print(ans[i], end=" ")
