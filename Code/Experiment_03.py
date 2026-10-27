from collections import deque

def water_jug_bfs():
    start = (0, 0)
    goal = 2
    capacity_a, capacity_b = 4, 3

    def get_neighbors(state):
        x, y = state
        neighbors = []
        # Fill Jug A
        neighbors.append((capacity_a, y))
        # Fill Jug B
        neighbors.append((x, capacity_b))
        # Empty Jug A
        neighbors.append((0, y))
        # Empty Jug B
        neighbors.append((x, 0))
        # Pour A -> B
        transfer = min(x, capacity_b - y)
        neighbors.append((x - transfer, y + transfer))
        # Pour B -> A
        transfer = min(y, capacity_a - x)
        neighbors.append((x + transfer, y - transfer))
        return neighbors

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        
        if state[0] == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None

solution = water_jug_bfs()
print("Solution path:", solution)
