# Introduction
Description of the project

# Pseudocode
Put pseudocode in this box:

```
1. Read all DNA reads from the input file into a list.

2. Build the De Bruijn graph:
   For each read in reads:
      Silde a window of length k across the read.
      For each k-mer:
        left = first k-1 bases
        right = last k-1 bases
        Add an edge from left -> right in the graph

3. Determine the start node:
   For each node in the graph:
      check if the node is an edge in the graph
      if it isn't, it's a start node, so append it to a list of start nodes
      

4. Perform Eulerian walk:
   Initialize a list to keep track of the tour
   Start at the chosen start node.
   While the current node has edges:
      randomly choose on of it's edges to be the next node
      remove the edge from the graph
      extend the tour list which a recursive call with the next_node
   Return the tour + the current node

   where the tour is an empty list and the while loop continues until a node has no edges this logic will return a reverse order tour traversal of the graph.
   the first return won't be hit until we reach the final edge in the subgraph/graph, where it will then return [] + [final edge] which will be returned to the previous recursive call
   where the node of the previous call can continue exploring it's edges until it has none left.

5. Convert path to sequence:
   Start with the first (k-1)-mer in the path.
   For each next node in the path:
      Append only the last nucleotide.

6. Repeat steps 4 and 5 for every start node in the graph.


```

# Successes
Description of the team's learning points

# Struggles
Our biggest hurdle as a group was understanding recursion it the context of graph traversal and then figuring out how to implement it. More specifically the mechanism of backtracking through the graph once you reached the final edge. Even now after we figured out how to implement it, it still doesn't feel the most intuitive, nor the easiest to explain. As we have it implemented now, the approach works for a small subsample of the reads, however, python has a arbitray recursion limit that our assembly implementation exceeds when using too many of the reads. In our current implementation we are not taking into account how many times a node touches an edge. That is, the higher frequencies associated with an edge of a node could correspond to read pile-up or overlaps, which could be used to inform graph traversal. With our current implementation we are not accounting for edge frequencies, and this could be making our graph traversal more ambiguous and complicated, leading to too many recursive calls, and thus a crash when we have too many reads.

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Other member
Connor - My biggest takeaway from this project is how careful you have to be when d the data structures you create from become increasingly larger as you process a large dataset. You also have to be very considerate of what you're doing with the datastructures you create - for our group we ran into trouble with the recursive call of the eulerian walk of our graph. This is most likely a result of not storing the information correct initially. However, through this struggle we've started to think through different ways we can deal with this, and it's made me think about the data structures I'm making more intimately than I have in the past.
I also am very thankful for how much my group members communicated with me, if it wasn't for them, I would still be stuck trying to figure out how recursion would work in the context of this problem.

# Generative AI Appendix
As per the syllabus
