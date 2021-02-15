import networkx
import pydot
eg1 = pydot.graph_from_dot_file("eg1.dot")
eg1[0].write_png("eg1.png")
nxeg1 = networkx.drawing.nx_pydot.from_pydot(eg1[0])
