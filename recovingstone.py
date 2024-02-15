from collections import deque

def decode_word(n):
    queue = deque([('', n)])
    while queue:
        word, num = queue.popleft()
        if len(word) == 3:
            return word
        for i in range(1, 27):
            if num - i >= 0:
                queue.append((word + chr(96 + i), num - i))

t = int(input())
for _ in range(t):
    n = int(input())
    word = decode_word(n)
    print(word)