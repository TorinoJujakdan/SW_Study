import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()

for i in range(n):
    command_list = input().split()
    command = command_list[0]
    if command == "push":
        x = int(command_list[1])
        q.append(x)
    elif command == "pop":
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif command == "back":
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)