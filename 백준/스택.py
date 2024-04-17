n = int(input())

stack = []
for _ in range(n):
    command = input().split()
    c = command[0]
    if c == 'push':
        stack.append(command[1])
    elif c == "pop":
        if len(stack) != 0:
            print(int(stack.pop()))
        else:
            print(-1)
    elif c == "size":
        print(len(stack))
    elif c == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c == "top":
        if len(stack) != 0:
            print(int(stack[-1]))
        else:
            print(-1)
        