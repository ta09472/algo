n = int(input())
words = []
for i in range(n):
    word = input()
    words.append((word, len(word)))
words = list(set(words))
words = sorted(words, key = lambda words: (words[1], words[0]))
for l in words:
    print(l[0])
