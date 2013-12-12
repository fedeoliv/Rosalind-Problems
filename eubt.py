# http://rosalind.info/problems/eubt/

class Node():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return "internal_{}".format(id(self))

class Edge():
    def __init__(self, node1, node2):
        self.nodes = [node1, node2]

    def __str__(self):
        return "{}--{}".format(*self.nodes)

class Tree():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def __str__(self):
        return "tree_{} edges: {}".format(id(self), [str(x) for x in self.edges])

    def copy(self):
        node_conversion = {node: Node(node.name) for node in self.nodes}
        new_nodes = list(node_conversion.values())
        new_edges = [Edge(node_conversion[edge.nodes[0]], node_conversion[edge.nodes[1]]) for edge in self.edges]

        new_tree = Tree(new_nodes, new_edges)
        return new_tree


def enumerate_trees(leaves):
    assert(len(leaves) > 1)
    
    if len(leaves) == 2:
        n1, n2 = leaves
        t = Tree()
        t.nodes = [Node(n1), Node(n2)]
        t.edges = [Edge(t.nodes[0], t.nodes[1])]
        return [t]
    elif len(leaves) > 2:
        # get the smaller tree first
        old_trees = enumerate_trees(leaves[:-1])
        new_leaf_name = leaves[-1]
        new_trees = []

        # find the ways to add the new leaf
        for old_tree in old_trees:
            for i in range(len(old_tree.edges)):
                new_tree = old_tree.copy()
                edge_to_split = new_tree.edges[i]
                old_node1, old_node2 = edge_to_split.nodes

                # get rid of the old edge
                new_tree.edges.remove(edge_to_split)

                # add a new internal node
                internal = Node(None)
                new_tree.nodes.append(internal)

                # add the new leaf
                new_leaf = Node(new_leaf_name)
                new_tree.nodes.append(new_leaf)

                # make the three new edges
                new_tree.edges.append(Edge(old_node1, internal))
                new_tree.edges.append(Edge(old_node2, internal))
                new_tree.edges.append(Edge(new_leaf, internal))

                # put this new tree in the list
                new_trees.append(new_tree) 

        return new_trees

def newick_format(tree_in):
    tree = tree_in.copy()

    if len(tree.nodes) == 1:
        return "{};".format(tree.nodes[0])
    elif len(tree.nodes) == 2:
        return "({},{});".format(*tree.nodes)
    elif len(tree.nodes) > 2:
        # reduce one of the nodes in the tree
        for candidate_node in tree.nodes:
            # ignore leaves
            if candidate_node.name is not None:
                continue

            adjacent_edges = [edge for edge in tree.edges if candidate_node in edge.nodes]
            adjacent_nodes = [node for edge in adjacent_edges for node in edge.nodes if node in edge.nodes and node is not candidate_node]
            adjacent_leaves = [node for node in adjacent_nodes if node.name is not None]

            # find a node with two leaves
            if len(adjacent_leaves) == 2 or len(adjacent_leaves) == 3:
                leaf1, leaf2 = adjacent_leaves[0: 2]
                edges_to_cut = [edge for edge in adjacent_edges if leaf1 in edge.nodes or leaf2 in edge.nodes]
                candidate_node.name = "({},{})".format(leaf1, leaf2)

                # remove leaves
                tree.nodes.remove(leaf1)
                tree.nodes.remove(leaf2)
                for edge in edges_to_cut: tree.edges.remove(edge)

                # cycle this one again
                return newick_format(tree)

if __name__ == '__main__':
    leaves = open('rosalind_eubt.txt').read().split()
    trees = enumerate_trees(leaves)

    print '\n'.join([newick_format(tree) for tree in trees])
