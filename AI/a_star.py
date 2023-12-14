class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
 
    def get_neighbors(self, v):
        return self.adjacency_list[v]
 
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }

        return H[n]
 
    def a_star_algorithm(self, start_node, stop_node) -> list:
        open_list = set([start_node])
        closed_list = set([])

        g_score = {}
        g_score[start_node] = 0

        parent = {}
        parent[start_node] = start_node

        while open_list:
            n = None
            print(f'Open list :{open_list} \nclosed_list:{closed_list}\n')

            # check for smallest "g(n) + h(n)" in open list
            for node in open_list:
                if n == None or (g_score[node] + self.h(node) < g_score[n] + self.h(n)):
                    n = node

            #no match
            if n == None:
                print('Path does not exist!')
                return None
            
            # match
            if n == stop_node:
                open_list.remove(n)
                closed_list.add(n)
                print(f'Open list :{open_list} \nclosed_list:{closed_list}\n')
                reconst_path = []

                while parent[n] != n:
                    reconst_path.append(n)
                    n = parent[n]
                reconst_path.append(start_node)
                reconst_path.reverse()

                return reconst_path

            # add neighnors in lists
            # check for smallest "g(n) + h(n)" in list
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    g_score[m] = g_score[n] + weight
                    parent[m] = n
                else:
                    if g_score[m] > g_score[n] + weight:
                        g_score[m] = g_score[n] + weight
                        parent[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            closed_list.add(m)
            
            open_list.remove(n)
            closed_list.add(n)
 
        print('Path does not exist!')
        return None
        
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
graph1 = Graph(adjacency_list)
print(graph1.a_star_algorithm('A', 'D'))