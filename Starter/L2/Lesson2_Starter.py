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
            self.graph[src] = [] 
        if dst not in self.graph: 
            self.graph[dst] = []


        # Store the node as a tuple 
        self.graph[src].append((dst, weight))
        self.graph[dst].append((src, weight))
        

    # Here we implement Djikstra's algorithm
    def shortest_path(self, src, dst):

        # TODO: Create vertex list 

        # TODO: Make a dictionary containing the shortest distance to each city

        # TODO: Store the parents of each node in a dictionary

    
        for vertex in self.graph.keys():
            # TODO: set all the distances to infinity

            # TODO: set all the parents to None

            # Add all the nodes to our initial list


        # TODO: set the distance to the initial node to 0



        while queue:
            # TODO: Pop the first node
            current = queue.pop(0)


            for edge in self.graph[current]:
                neighbor = edge[0]
                weight = edge[1]
                # TODO: See if we can find a path to neighbor with lower cost


                # Adjust the new path if we find one
                if tmp_dist < self.distance[neighbor]:
                    # TODO: Set the distance to the neighbor to a lower value if we find one

                    # TODO: Set the parent of the neighbor to the current node


        self.print_path(dst)
        print('\n')

        return self.distance[dst]

                    
    def print_path(self, node):
        if node == None:
            print('\nThe shortest path is: ', end=' ')
            return
        self.print_path(self.parent[node])
        print(f'{node} ', end=' ')
        

def main():
    print('\n-------\n'
        'Welcome, first we will add the edges in our graph\n'\
        'Input a source city, a target city, and the length between them.\n'
        'To move to next stage, type \'continue\'. \n'\
        '-------\n'
        )


    while True:
        graph = Graph()
        while True:
            src = input('\nSource city: ').lower()
            if src == 'continue':
                break
            dst = input('Destination city: ').lower()
            if dst == 'continue':
                break

            try:
                weight = int(input('Weight: '))
            except:
                print('Remember that the weight should be an integer! Start over')
                continue

            # TODO: add the edge between the two cities in our graph

        print('\nNow choose the cities to find the shortest path.\n')
        src = input('Source city: ').lower()
        dst = input('End city: ').lower()

        # Calculate the shortest path
        path = graph.shortest_path(src, dst)

        print(f'\nThe shortest path between {src} and {dst} takes {path}.') 

        cont = input('Play again?[y/n]: ').lower()
        if cont == 'n':
            break

if __name__=='__main__':
    main()
