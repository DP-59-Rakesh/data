from collections import deque


q=deque()
q.append(10)
q.append(20)
q.append(30)
q.append(40)
print(q)
q.popleft()
q.popleft()

print(q)

print(q)