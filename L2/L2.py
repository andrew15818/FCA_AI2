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
    def shortest_path(src, dst):

def main():
    print('-------\n'\
            'Welcome! First, we will add the cities you want.\n'\
            'Type the name of the city and press Enter.\n'\
            'Type \'continue\' to move on to next stage.\n'\
            '-------\n'
            )
    graph = Graph()
    while True:
        city = input('Enter name of city: ')

        if city.lower() == 'continue':
            break
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
if __name__=='__main__':
    main()
