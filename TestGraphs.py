from Graphs import Graph
import unittest

class test_Graph(unittest.TestCase):

    def setUp(self):
        """
        Builds a graph to be used for future unit tests
        """
        self.g = Graph(['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami'], 
                       [('New York', 'San Francisco', 2900), ('San Francisco', 'Los Angeles', 380), 
                        ('Los Angeles', 'Chicago', 1750), ('Chicago', 'Miami', 1375)])
    
    ''' 
    ASCII art of the graph made:
             2900 mi           1750 mi
   New York ------ San Francisco ----- Los Angeles
     |                                      |
  800 mi                                380 mi
     |                                      |
 Chicago ------------------------------ Miami

    '''


    def test_graph_vertices(self):
        '''
        tests functionality of innit method by testing if the graph vertices are added 
        '''
        self.assertCountEqual(self.g._V, ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami'])
    

    def test_graph_edges(self):
        '''
        tests functionality of innit method by testing if the graph edges are added 
        '''
        self.assertCountEqual(self.g._E, [('New York', 'San Francisco', 2900), ('San Francisco', 'Los Angeles', 380), 
                                         ('Los Angeles', 'Chicago', 1750), ('Chicago', 'Miami', 1375)])
    

    def test_add_vertex(self):
        '''
        tests functionality of the add_vertex method
        '''
        self.g.add_vertex('Seattle')
        self.assertIn('Seattle', self.g._V)


    def test_remove_vertex(self):
        '''
        tests functionality of remove_vertex method
        '''
        self.g.remove_vertex('San Francisco')
        self.assertNotIn('San Francisco', self.g._V)
        self.assertNotIn(('New York', 'San Francisco', 2900), self.g._E)
        self.assertNotIn(('San Francisco', 'Los Angeles', 380), self.g._E)

    
    def test_add_edge(self):
        self.g.add_edge('New York', 'San Francisco', 2900)
        self.assertIn(('New York', 'San Francisco', 2900), self.g._E)
    

    def test_remove_edge(self):
        '''
        tests functionality of the remove_edge method
        '''
        self.g.remove_edge('San Francisco', 2900)
        self.assertNotIn(('San Francisco', 2900), self.g._E)
    

    def test_nbrs(self):
        '''
        tests functionality of the nbrs method
        '''
        self.assertCountEqual(self.g.nbrs('New York'), ['San Francisco'])
        self.assertCountEqual(self.g.nbrs('San Francisco'), ['New York', 'Los Angeles'])
        self.assertCountEqual(self.g.nbrs('Los Angeles'), ['San Francisco', 'Chicago'])
        self.assertCountEqual(self.g.nbrs('Chicago'), ['Los Angeles', 'Miami'])
        self.assertCountEqual(self.g.nbrs('Miami'), ['Chicago'])
    


class test_GraphTraversal(unittest.TestCase):

    def setUp(self):
        """
        Builds a graph to be used for future unit tests
        """
        self.g = Graph(['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami'], 
                       [('New York', 'San Francisco', 2900), ('San Francisco', 'Los Angeles', 380), 
                        ('Los Angeles', 'Chicago', 1750), ('Chicago', 'Miami', 1375)])

    ''' 
    ASCII art of the graph made:
             2900 mi           1750 mi
   New York ------ San Francisco ----- Los Angeles
     |                                      |
  800 mi                                380 mi
     |                                      |
 Chicago ------------------------------ Miami

    '''


    # Alg: Breadth first search
    # Why: This algorithm can efficiently traverse 
    # the graph with the correct information, ideally in a queue
    def test_fewest_flights(self):
        '''
        tests functionality of fewest_flights method
        '''
        path_tree, vertex_weights = self.g.fewest_flights('New York')
        expected_weights = {'New York': 0, 'San Francisco': 1, 'Los Angeles': 2, 'Chicago': 3, 'Miami': 4}
        self.assertDictEqual(vertex_weights, expected_weights)

    
    # Alg: Dijkstra's algorithm 
    # Why: Dijkstra's algorithm is a good 
    # fit for this task because it is efficient and 
    # guarantees that it will find the shortest path in a weighted graph with non-negative edge weights
    def test_shortest_path(self):
        '''
        tests functionality of shortest_path method
        '''
        path_tree, vertex_weights = self.g.shortest_path('New York')
        expected_weights = {'New York': 0, 'San Francisco': 2900, 'Los Angeles': 3280, 'Chicago': 5030, 'Miami': 6405}
        self.assertDictEqual(vertex_weights, expected_weights)


    # Alg: Prims algorithm 
    # Why: Prims algorithm is a good 
    # fit for this task because it can efficiently find the minimum spanning tree of the graph
    def test_minimum_salt(self):
        '''
        tests functionality of minimum_salt method
        '''
        path_tree, vertex_weights = self.g.minimum_salt('New York')
        expected_weights = {'New York': 0, 'San Francisco': 2900, 'Los Angeles': 3280, 'Chicago': 5030, 'Miami': 6405}
        self.assertDictEqual(vertex_weights, expected_weights)
        
        # test that the sum of all weights is correct
        expected_sum = sum(expected_weights.values())
        actual_sum = sum(vertex_weights.values())
        self.assertEqual(actual_sum, expected_sum)



unittest.main()