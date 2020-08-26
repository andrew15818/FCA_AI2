# Lesson 2 Project: Finding the shortest paths using Djikstra's
class Graph:
    def __init__(self):
        # Store our nodes and edges here
        self.graph = {}

    def add_node(self, node):
        # Add the node if it is not in our graph
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, src, dst, weight):

        if src not in self.graph:
            print(f'{src} is not a node in our graph yet. Do add_node({src}) first')
            return
        elif dst not in self.graph:
            print(f'{dst} is not a node in our graph yet. Do add_node({dst}) first')
            return 

        # Store the node as a tuple
        self.graph[src].append((dst, weight))
        self.graph[dst].append((dst, weight))

    # Here we implement Djikstra's algorithm
    def shortest_path(self, src, dst):

        # Vertex queue
        queue = []
        # Distance to each vertex
        distance = {}
        # Parents of our nodes
        parent = {}
        for vertex in self.graph.keys():
            distance[vertex] = float('inf')
            parent[vertex] = None

        distance[src] = 0
        queue.append(src)

        while queue:
            current = queue.pop(0)
            print(f'Examining {current}')

            for edge in self.graph[current]:
                neighbor = edge[0]
                weight = edge[1]
                # See if we can find a better path
                tmp_dist = distance[current] + weight

                # Adjust the new path if we find one
                if tmp_dist < distance[neighbor]:
                    distance[neighbor] = tmp_dist
                    parent[neighbor] = current
                    

def main():
    print('-------\n'\
            'Welcome! First, we will add the cities you want.\n'\
            'Type the name of the city and press Enter.\n'\
            'Type \'continue\' to move on to next stage.\n'\
            '-------\n'
            )
    graph = Graph()
    graph.add_node('taipei')
    graph.add_node('hsinchu')
    graph.add_edge('taipei', 'hsinchu', 12)
    graph.shortest_path('taipei', 'hsinchu')
    '''
    # Get the name of cities in our graph
    cities = input('Enter the name of the cities in our map: ')
    for city in cities.split():
        graph.add_node(city)

    print('-------\n'
            'Now enter the name of the source city, destination city, and weights\n'\
            'e.g Taipei Hsinchu 12\n'\
            '--------\n'
        )
    while True:
        src, dst, weight = input('Enter source, destination, weight: ').split() 
        graph.add_edge(src, dst, weight)
        if src.lower() == 'continue':
            break

    src, dst = input('Enter the city you wish to start and end at: ').split()
    graph.shortest_path(src, dst)
    '''
if __name__=='__main__':
    main()
