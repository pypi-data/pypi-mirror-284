import unittest
import networkx as nx
import numpy as np
from openqaoa.problems import ShortestPath, QUBO


def terms_list_equality(terms_list1, terms_list2):
    """
    Check the terms equality between two terms list
    where the order of edges do not matter.
    """
    if len(terms_list1) != len(terms_list2):
        bool = False
    else:
        for term1, term2 in zip(terms_list1, terms_list2):
            bool = True if (term1 == term2 or term1 == term2[::-1]) else False

    return bool


def terms_list_isclose(terms_list1, terms_list2):
    """
    Check if the distance between two terms list
    where the order of edges do not matter.
    """
    if len(terms_list1) != len(terms_list2):
        bool = False
    else:
        for term1, term2 in zip(terms_list1, terms_list2):
            bool = (
                True
                if np.isclose(term1, term2) or np.isclose(term1, term2[::-1])
                else False
            )

    return bool


class TestShortestPath(unittest.TestCase):
    """Tests for ShortestPath class"""

    def test_shortestpath_terms_weights_constant(self):
        """Test terms,weights,constant of QUBO generated by Shortest Path class"""

        sp_terms = [
            [0],
            [1],
            [2],
            [3],
            [1],
            [1, 2],
            [2, 1],
            [2],
            [2],
            [2, 3],
            [3, 2],
            [3],
            [0],
            [0, 1],
            [1],
            [1, 3],
            [0, 3],
            [3, 1],
            [3],
        ]
        sp_weights = [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 4, -4, 1, 1, -4, 1, 1]
        conv_sp_terms = [
            [1, 2],
            [2, 1],
            [2, 3],
            [3, 2],
            [0, 1],
            [1, 3],
            [0, 3],
            [3, 1],
            [0],
            [1],
            [2],
            [3],
            [],
        ]
        conv_sp_weights = [
            0.25,
            0.25,
            0.25,
            0.25,
            -1.0,
            0.25,
            -1.0,
            0.25,
            -0.5,
            -0.5,
            -0.5,
            -0.5,
            2.5,
        ]
        sp_qubo_terms = [[1, 2], [2, 3], [0, 1], [1, 3], [0, 3], [0], [1], [2], [3]]
        sp_qubo_weights = [0.5, 0.5, -1.0, 0.5, -1.0, -0.5, -0.5, -0.5, -0.5]
        sp_qubo_constant = 2.5

        gr = nx.generators.fast_gnp_random_graph(3, 1, seed=1234)
        for u, v in gr.edges():
            gr.edges[u, v]["weight"] = 1
        for w in gr.nodes():
            gr.nodes[w]["weight"] = 1
        source, dest = 0, 2
        sp = ShortestPath(gr, source, dest)
        n_variables = sp.G.number_of_nodes() + sp.G.number_of_edges() - 2
        bin_terms, bin_weights = sp.terms_and_weights()
        terms, weights = QUBO.convert_qubo_to_ising(n_variables, bin_terms, bin_weights)
        qubo = sp.qubo

        self.assertTrue(terms_list_equality(bin_terms, sp_terms))
        self.assertEqual(list(bin_weights), sp_weights)
        self.assertTrue(terms_list_equality(terms, conv_sp_terms))
        self.assertEqual(list(weights), conv_sp_weights)
        self.assertTrue(terms_list_equality(sp_qubo_terms, qubo.terms))
        self.assertEqual(sp_qubo_weights, qubo.weights)
        self.assertEqual(sp_qubo_constant, qubo.constant)

    def test_shortestpath_random_instance(self):
        """Test random instance method of Shortest Path problem class"""
        sp_rand_terms = [[1, 2], [2, 3], [0, 1], [1, 3], [0, 3], [0], [1], [2], [3]]
        sp_rand_weights = [0.5, 0.5, -1.0, 0.5, -1.0, -0.5, -0.5, -0.5, -0.5]
        sp_rand_constant = 2.5

        gr = nx.generators.fast_gnp_random_graph(3, 1, seed=1234)
        for u, v in gr.edges():
            gr.edges[u, v]["weight"] = 1.0
        for w in gr.nodes():
            gr.nodes[w]["weight"] = 1.0
        sp_prob = ShortestPath.random_instance(
            n_nodes=3, edge_probability=1, seed=1234, source=0, dest=2
        ).qubo

        self.assertTrue(terms_list_equality(sp_rand_terms, sp_prob.terms))
        self.assertEqual(sp_rand_weights, sp_prob.weights)
        self.assertEqual(sp_rand_constant, sp_prob.constant)

        self.assertEqual(sp_prob.terms, ShortestPath(gr, 0, 2).qubo.terms)
        self.assertEqual(sp_prob.weights, ShortestPath(gr, 0, 2).qubo.weights)
        self.assertEqual(sp_prob.constant, ShortestPath(gr, 0, 2).qubo.constant)

    def test_assertion_error(self):
        def test_assertion_fn():
            n_row = 1
            n_col = 1

            G = nx.triangular_lattice_graph(n_row, n_col)
            G = nx.convert_node_labels_to_integers(G)
            G.remove_edges_from(nx.selfloop_edges(G))

            node_weights = np.round(np.random.rand(len(G.nodes())), 3)
            edge_weights = np.round(np.random.rand(len(G.edges())), 3)

            node_dict = dict(zip(list(G.nodes()), node_weights))
            edge_dict = dict(zip(list(G.edges()), edge_weights))

            nx.set_edge_attributes(G, values=edge_dict, name="weight")
            nx.set_node_attributes(G, values=node_dict, name="weight")

            shortest_path_problem = ShortestPath(G, 0, -1)
            shortest_path_qubo = shortest_path_problem.qubo

        self.assertRaises(Exception, test_assertion_fn)


if __name__ == "__main__":
    unittest.main()
