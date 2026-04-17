import sys


input = sys.stdin.readline
N = int(input().strip())


words = [input().strip() for _ in range(N)]


words = list(set(words))
words.sort()

count = 0
M = len(words) 


for i in range(M - 1):
    if not words[i+1].startswith(words[i]):
        count += 1


if M > 0:
    count += 1


print(count)