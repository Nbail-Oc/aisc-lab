from heapq import heappush, heappop
def water_jug_astar():
    start = (0, 0)
    goal = 2
    capacity_a, capacity_b = 4, 3
    def heuristic(state):
        return abs(state[0] - goal)
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
    frontier = []
    heappush(frontier, (heuristic(start), 0, start, [start]))
    visited = set()
    while frontier:
        f, g, state, path = heappop(frontier)
        if state[0] == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heappush(frontier, (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [neighbor]))
    return None
solution = water_jug_astar()
print("Solution path:", solution)
