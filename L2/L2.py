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

        # TODO: Create vertex list 
        queue = []
        # TODO: Make a dictionary containing the shortest distance to each city
        self.distance = {}
        # TODO: Store the parents of each node in a dictionary
        self.parent = {}
    
        for vertex in self.graph.keys():
            # TODO: set all the distances to infinity
            self.distance[vertex] = float('inf')
            # TODO: set all the parents to None
            self.parent[vertex] = None
            # Add all the nodes to our initial list
            queue.append(vertex)

        # TODO: set the distance to the initial node to 0
        self.distance[src] = 0


        while queue:
            # TODO: Pop the first node
            current = queue.pop(0)


            for edge in self.graph[current]:
                neighbor = edge[0]
                weight = edge[1]
                # TODO: See if we can find a path to neighbor with lower cost
                tmp_dist = self.distance[current] + weight

                # Adjust the new path if we find one
                if tmp_dist < self.distance[neighbor]:
                    # TODO: Set the distance to the neighbor to a lower value if we find one
                    self.distance[neighbor] = tmp_dist
                    # TODO: Set the parent of the neighbor to the current node
                    self.parent[neighbor] = current

        self.print_path(dst)
        print('\n')


                    
    def print_path(self, node):
        if node == None:
            return
        self.print_path(self.parent[node])
        print(f'{node} ', end=' ')
        

def main():
    print('-------\n'\
            'Welcome! First, we will add the cities you want.\n'\
            'Type the name of the city and press Enter.\n'\
            'Type \'continue\' to move on to next stage.\n'\
            '-------\n'
            )
    graph = Graph() 
    # Get the name of cities in our graph
    cities = input('Enter the name of the cities in our map: ')
    for city in cities.split():
        # TODO: Add the node to the graph
        graph.add_node(city)

    print('-------\n'
            'Now enter the name of the source city, destination city, and weights\n'\
            'e.g Taipei Hsinchu 12\n'\
            '--------\n'
        )
    while True:
        src, dst, weight = input('Enter source, destination, weight: ').split() 
        src = src.lower()
        dst = dst.lower()
        weight = int(weight)

        # TODO: Add the edge between the source and destination with given weight
        graph.add_edge(src, dst, weight)
        
        # break from the loop
        if src.lower() == 'continue':
            break

    src, dst = input('Enter the city you wish to start and end at: ').split()
    graph.shortest_path(src, dst)
    
if __name__=='__main__':
    main()
