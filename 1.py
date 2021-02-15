import networkx
import pydot
eg1 = pydot.graph_from_dot_file("eg1.dot")
eg1[0].write_png("eg1.png")
nxeg1 = networkx.drawing.nx_pydot.from_pydot(eg1[0])
u1 = networkx.DiGraph.to_undirected(nxeg1)
cc1=networkx.algorithms.connected_components(u1)
for c in cc1:
  print(c)


