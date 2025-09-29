import networkx as nx
import  matplotlib.pyplot as plt

G=nx.DiGraph()
G.add_edge('A','B',weight=3)
G.add_edge('B','C',weight=10)
G.add_edge('C','A',weight=3)

pos=nx.circular_layout(G)
labels=nx.get_edge_attributes(G,'weight')
nx.draw(G,pos,with_labels=True,node_color='lightblue',node_size=1500,font_size=20,font_color='red',font_weight='bold')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.title('Graph')
plt.show()
