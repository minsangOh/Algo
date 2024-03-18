import sys, math
input = sys.stdin.readline()

H, W, N, M = map(int, input.split())

print(math.ceil(W/(1+M)) * math.ceil(H/(1+N)))