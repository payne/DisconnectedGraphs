import networkx
import pydot
eg1 = pydot.graph_from_dot_file("eg2.dot")
eg1[0].write_png("eg2.png")
nxeg1 = networkx.drawing.nx_pydot.from_pydot(eg1[0])
u1 = networkx.DiGraph.to_undirected(nxeg1)
cc1=networkx.algorithms.connected_components(u1)

for i, f in enumerate(cc1, start=1):
   if (len(f) >= 5): print("Component %d: %s" % (i, f))


