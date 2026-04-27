from collections import deque

queue = deque()

queue.append("Хуснора")
queue.append("Карина")
queue.append("Данайя")

print("Очередь:", list(queue))

while queue:
    client = queue.popleft()
    print("Обслуживается:", client)
    print("Осталось в очереди:", list(queue))

print("Очередь пуста.")