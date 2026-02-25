from collections import defaultdict
import random

def read_fastq(filename):
    """Read sequences from a FASTQ file.

    Args:
        filename (str): Path to FASTQ file.

    Returns:
        list: List of DNA sequence strings (quality scores ignored).

    Example:

    10
    """
    sequences = []
    with open(filename, 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
            if line_count % 4 == 2:  # Sequence line in FASTQ format
                sequences.append(line.strip())
    return sequences



class DeBruijnGraph:
    """Main class for De Bruijn graphs and genome assembly.

    This class builds De Bruijn graphs from sequencing reads and performs
    genome assembly by finding Eulerian paths through connected components
    of the graph.

    Attributes:
        graph (defaultdict): Adjacency list representation of graph edges.
            Keys are (k-1)-mers, values are lists of adjacent (k-1)-mers.
        k (int): The k-mer size used for graph construction.

    Example:

        True
    """

    def __init__(self, reads, k):
        """Initialize De Bruijn graph from sequencing reads.

        Args:
            reads (list): List of DNA sequence strings.
            k (int): K-mer size for graph construction.

        Example:

            True
        """
        self.graph = defaultdict(list)
        self.k = k
        self.build_graph_from_reads(reads, k)

    def add_edge(self, left, right):
        """Add a directed edge to the graph.

        Args:
            left (str): Source (k-1)-mer node.
            right (str): Destination (k-1)-mer node.

        Example:

            True
        """
        self.graph[left].append(right)

    def remove_edge(self, left, right):
        """Remove a directed edge from the graph.

        Args:
            left (str): Source (k-1)-mer node.
            right (str): Destination (k-1)-mer node.

        Example:

            0
        """

        self.graph[left].remove(right)

    def build_graph_from_reads(self, reads, k):
        """Build De Bruijn graph from multiple sequencing reads.

        Extracts all k-mers from all reads and adds edges between
        consecutive (k-1)-mers within each k-mer.

        Args:
            reads (list): List of DNA sequence strings.
            k (int): K-mer length for graph construction.

        Example:

            True
        """

        for read in reads:
            for i in range(len(read) - k + 1):
                k_mer = read[i: i + k]
                l_mer = k_mer[0: k - 1]
                r_mer = k_mer[1:]
                self.add_edge(l_mer, r_mer)



    def eulerian_walk(self, node, graph, seed=None):
        """Perform recursive Eulerian walk on a graph component.

        This is a recursive function that follows all edges from a node
        to traverse the graph, building a path in reverse order.

        Args:
            node (str): Current node to traverse from.
            graph (defaultdict): Graph or subgraph to traverse.
            seed (int, optional): Seed for random edge selection.

        Returns:
            list: List of (k-1)-mers traversed (in reverse order).

        Example:

            True
        """

        tour = []

        while graph[node]:
            next_node = random.choices(graph[node])
            self.remove_edge(node, next_node[0])
            tour.extend(self.eulerian_walk(next_node[0], graph))

        return tour + [node]


    def assemble_contigs(self, seed=None):
        """Assemble all contigs from the De Bruijn graph.

        Finds all connected components and generates an Eulerian path
        for each component, producing multiple assembled contigs.

        Args:
            seed (int, optional): Random seed for reproducible assembly.

        Returns:
            list: List of assembled contig sequences (DNA strings).

        Example:

            True
        """

        start_nodes = []
        for key in self.graph.keys():
            if key not in self.graph.values():
                start_nodes.append(key)

        contigs = []
        for node in start_nodes:
            walk = self.eulerian_walk(node, self.graph)
            contig = self.tour_to_sequence(walk)
            contigs.append(contig)


    def tour_to_sequence(self, tour):
        """Convert a tour of (k-1)-mers into a DNA sequence.

        Args:
            tour (list): List of (k-1)-mer strings in order.

        Returns:
            str: Assembled DNA sequence.

        Example:

            'ATGGCG'
        """

        ordered_tour = tour[::-1]
        contig = ""


        pass

    def get_assembly_stats(self, contigs):
        """Calculate assembly statistics for assembled contigs.

        Args:
            contigs (list): List of contig sequences.

        Returns:
            dict: Dictionary containing assembly statistics:
                - num_contigs: Total number of contigs
                - total_length: Total assembled sequence length
                - longest_contig: Length of longest contig
                - shortest_contig: Length of shortest contig
                - mean_length: Mean contig length
                - n50: N50 statistic

        Example:

            3
        """
        pass

    def write_fasta(self, contigs, filename):
        """Write assembled contigs to a FASTA file.

        Args:
            contigs (list): List of contig sequences.
            filename (str): Output FASTA filename.

        Example:

        """
        pass

dbg = DeBruijnGraph(["ABDBC", "EFGEFGHI"], k=3)

