import heapq
import math
from typing import List,Dict,Tuple,Optional

from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class DijkstraStrategy(PathfindingStrategy):
    """ The class Implements the Dijkstra Algorithm with 3 main staticmethods that helps
        us calculate intermediate steps.

        The Dijkstra algorithm solves the problem of min path with single source in a direct graph
        G = (V,E), where all the weights are non negative.

        Methods
        -------
            dijkstra_algorithm(grid: List[List[Node]], source: Node)
                calculate the dijkstra algorithm for all the nodes starting with the source, return the
                path and cost for each Node from the source

            find_path(grid:List[List[Node]], start:Node, end:Node)
                get the path from the start to the end Node using the dijkstra algorithm. return
                the path from start to the end, but without the source node in the list

            get_neighbors(grid: List[List[Node]], node:Node)
                Get the Adjacent Nodes from a specific node, its important during the dijkstra algorithm
                return a list of adj nodes. Imporant, here we consider the H,V,D possibilities

            calculate_distance(node1: Node, node2: Node)
                Get the Euclidian distance between two nodes using the cartesian coordinates.


    """

    @staticmethod
    def dijkstra_algorithm(grid: List[List[Node]], source: Node):
        """ Dijkstra Algorithm

            INIT-SINGLE-SOURCE(G, s):
                for v in G:
                    v.d = inf
                    v.path = NIL
            S = {}
            Q = HEAPQ([(cost,node)])
            WHILE Q != {}:
                u = EXTRACT-MIN(Q)
                S = S U {u}
                for v in G.Adj[u]:
                    if v.cost > u.cost + u.distance + u.weight:
                        v.cost = u.cost + u.distance + u.wieght
                        v.path = u.path + u

            Parameters
            ----------
                grid: List[List[Node]]
                    Our Graph representation
                source: Node
                    Vertex representation

            Return
            ------
                cost_path_dic: Dict[Node,List[float,List[Node]]]
                    A dictionary that contains each Node cost and path from the source, remember that
                    the cost and path is the min path from the source.

            Reference
            ---------
                Priority Queue Order: https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
                Algoritmos Teoria e Pratica 3ed: Thomas H Cormen, Charles E. Leiserson, Ronand L Rivest, Cliford Stein
        """
        # Initilize-single-source Cost
        cost_dict: Dict[Node,List] = {}
        for list_nodes in grid:
            for node in list_nodes:
                cost_dict[node] = [math.inf,[]]

        cost_dict[source] = [0,[]]
        S = set()
        q = [(0,source)]
        heapq.heapify(q)

        while q:
            # Extract the Min from our priority queue
            _,u = heapq.heappop(q)
            if u not in S:
                S.add(u)
                # Get the G.Adj[u]
                list_neighbors: List[Node] = __class__.get_neighbors(grid, u)
                for neighbor in list_neighbors:
                    if neighbor in S: continue
                    distance = __class__.calculate_distance(u, neighbor) + cost_dict[u][0]
                    if cost_dict[neighbor][0] > neighbor.weight + distance:
                        # Update the Cost
                        cost_dict[neighbor][0] = neighbor.weight + distance
                        # Update the Path
                        path = cost_dict[neighbor][1] + cost_dict[u][1]
                        path.append(u)
                        cost_dict[neighbor][1] = path
                        heapq.heappush(q,(cost_dict[neighbor][0],neighbor))
        return cost_dict

    @staticmethod
    def find_path(grid:List[List[Node]], start:Node, end:Node):
        """ By a Grid , Source and a target, return the Path of the source to the target
            excluding the source from the result.

            Parameters
            ----------
                grid: List[List[Node]]
                    Our Graph representation
                source: Node
                    Vertex representation
                end: Node
                    Vertex representation

            Return
            -------
                Path: List[Node]
                    The path from Source to End, but without the source (Challange rule)

            TODO.: For a improvement, you can stop the Dijsktra algorithm early when you find the Target,
                    but for debug purpose and fast prototype I added the full algorithm.

        """
        if not (isinstance(start,Node) and isinstance(end,Node)):
            raise NotImplementedError(f'Nodes must be type Node. {type(start)},{type(end)}')
        # Calculate the Dijkstra Algorithm (the algorithm calculates from all nodes)
        all_possible_paths_from_source: Dict[Node,List[int,List[Node]]] = __class__.dijkstra_algorithm(grid, start)
        # Get the path and empty if the Node to not exist in the Grid
        path = all_possible_paths_from_source.get(end,[])[-1]
        # Exclude the source and add the target to the path
        path_without_source = path[1:]
        path_without_source.append(end)

        return path_without_source

    @staticmethod
    def get_neighbors(grid: List[List[Node]], node:Node) -> List[Node]:
        """ Neighbors is a Vector of Nodes defined mathematically by G.Adj[u]
            where G is the Grid and u is the Node we are considering as our source.

            If the G.Adj[u] is empty the Node is isolated, and all the calculation is the
            equal as the start condition.

            Parameters
            ----------
                grid: List[List[Node]]
                    Is our graph representation. Here we use the matrix notation
                node: Node
                    Is the node we consider as the source and all the calculation are from
                    that node

            Returns
            -------
                G.Adj[u]: List[Node]
                    Is our Neighbors from the node (source). It could be empty if we consider
                    isolated vertex

            Mathematically notation: G.Adj[u] we use during the algorithm, the value of the
        """
        # Check condition
        if not (isinstance(node,Node)):
            raise NotImplementedError(f'Nodes must be type Node. {type(node)},{type(grid)}')
        # Start condition
        grid_width = len(grid)
        grid_height = len(grid[0])
        neighbors: List[Node] = []
        cardinal_directions = [
            Position(-1, -1),
            Position(-1, 0),
            Position(-1, 1),
            Position(0, -1),
            Position(0, 1),
            Position(1, -1),
            Position(1, 0),
            Position(1, 1)
        ]

        for index_pos in cardinal_directions:
            neighbor_white: Position = node.position + index_pos
            if neighbor_white.x >= 0 and neighbor_white.y >= 0:
                if neighbor_white.x < grid_width and neighbor_white.y < grid_height:
                    neighbors.append(
                        grid[neighbor_white.x][neighbor_white.y]
                    )

        return neighbors

    @staticmethod
    def calculate_distance(node1: Node, node2: Node) -> float:
        """ Calculate the euclidian distance between two Nodes in our cartesian space.

            Parameters
            ----------
                node1: Node
                    Node in our cartesian space with predefined position
                node2: Node
                    Node in our cartesian space with predefined position

            Returns
            -------
                euclidian distance: float
                    sqrt( (x2-x1)^2 + (y2-y1)^2) )
        """
        if isinstance(node1,Node) and isinstance(node2,Node):
            return math.sqrt(
                (node1.position.x - node2.position.x)**2 + \
                (node1.position.y - node2.position.y)**2
            )
        raise NotImplementedError(f'Nodes must be type Node. {type(node1)},{type(node2)}')
