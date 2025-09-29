import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

nodes=["A","B","C","D","E"]
G.add_nodes_from(nodes)

edges=[("A","B"),("B","C"),("C","D"),("C","E")]
G.add_edges_from(edges)

pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color='skyblue',node_size=2000,font_size=20,font_color='red', font_weight='bold')
nx.draw_networkx_edge_labels(G,pos,edge_labels={("A","B"):"A-B",("B","C"):"B-C",("C","D"):"C-D",("C","E"):"C-E"})


plt.title('Graph')
plt.show()


























































