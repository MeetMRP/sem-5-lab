def get_neighbors(current, graph, n):
    return [i for i in range(n) if i != current and graph[current][i] != None]

def goal_test(current, goal):
    return current == goal

def print_step_info(step, current, open_list, closed_list, goal_reached):
    print(f"\nStep {step}: Current Node - {current}")
    print("Open List:", open_list)
    print("Closed List:", closed_list)
    print("Goal Test:", goal_reached)

def hillclimb(start, goal, graph, n, mapping, h):
    open_list = [(start, h[start])]
    closed_list = set()
    step = 1

    while open_list:
        current, _ = open_list.pop(0)
        closed_list.add(current)
        
        goal_reached = goal_test(current, goal)
        print_step_info(step, current, open_list, closed_list, goal_reached)
        step += 1

        if goal_reached:
            print("\nPath found:", ' -> '.join(mapping[node] for node in closed_list))
            return

        neighbors = get_neighbors(current, graph, n)

        for neighbor in neighbors:
            if neighbor not in closed_list:
                cost = graph[current][neighbor] + h[neighbor]
                open_list.append((neighbor, cost))

        open_list.sort(key=lambda x: x[1])

    print("\nPath not found")

h = [14, 12, 11, 6, 4, 11, 0]
graph = [
    [0, 4, 3, None, None, None, None],
    [None, 0, None, None, 12, 5, None],
    [None, None, 0, 7, 10, None, None],
    [None, None, None, 0, 2, None, None],
    [None, None, None, None, 0, None, 5],
    [None, None, None, None, 0, 0, 16],
    [None, None, None, None, None, 0, 0]
]
mapping = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

start = input("Enter Start point: ")
goal = input("Enter Goal point: ")
start = mapping.index(start)
goal = mapping.index(goal)

hillclimb(start, goal, graph, 7, mapping, h)
