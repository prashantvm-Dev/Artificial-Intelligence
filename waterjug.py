from collections import deque
def water_jug(capacity_a, capacity_b, target):
    queue = deque()
    visited = set()
    parent = {}

    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()
        a, b = current

        # Check whether target is reached
        if a == target or b == target:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Solution path:")
            for state in path:
                print(state)

            return

        # Generate possible states
        states = [
            (capacity_a, b),  # Fill jug A
            (a, capacity_b),  # Fill jug B
            (0, b),           # Empty jug A
            (a, 0),           # Empty jug B
        ]
        # Pour A -> B
        amount = min(a, capacity_b - b)
        states.append((a - amount, b + amount))

        # Pour B -> A
        amount = min(b, capacity_a - a)
        states.append((a + amount, b - amount))

        # Add unvisited states
        for new_state in states:
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)
                parent[new_state] = current

    print("No solution exists.")


capacity_a = 4
capacity_b = 3
target = 2

water_jug(capacity_a, capacity_b, target)
