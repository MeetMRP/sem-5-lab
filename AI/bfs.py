graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = []


def bfs(graph, start_node, goal):
    visited = []
    closed_list = []
    queue = []
    path = {}
    route = []

    visited.append(start_node)
    path[start_node] = start_node
    queue.append(start_node)
    print(f"Open List: {queue}\nClosed list: {closed_list}\n ")

    while queue:
        next_node = queue.pop(0)
        closed_list.append(next_node)
        print(f"Open List: {queue}\nClosed list: {closed_list}\n ")

        # check if next_node is the goal
        if next_node == goal:
            while path[next_node] != next_node:
                route.append(next_node)
                next_node = path[next_node]
            
            route.append(next_node)
            route.reverse()
            return route

        # find next nodes
        for neighbour in graph[next_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                path[neighbour] = next_node
        print(f'Open List: {queue}\nClosed List: {closed_list}\n')
    
    return None

print("Following is the Breadth-First Search") 
route = bfs (
    graph=graph,
    start_node='5',
    goal='4'
)
print(f'Route: {route}')