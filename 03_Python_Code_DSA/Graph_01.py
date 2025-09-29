# NetworkX লাইব্রেরি ব্যবহার করে গ্রাফ আঁকা হবে
import networkx as nx
import matplotlib.pyplot as plt


# একটি নতুন গ্রাফ তৈরি করছি
G = nx.Graph()

# নোড বা ভের্টেক্সগুলো যোগ করছি
nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

# এজ বা সংযোগগুলো যোগ করছি
edges = [("A", "B"), ("B", "C"), ("C", "D"), ("C", "E")]
G.add_edges_from(edges)

# গ্রাফটি প্রদর্শনের জন্য সেটিংস
pos = nx.spring_layout(G)  # নোডের পজিশন নির্ধারণ
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=20, font_color='black', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={("A", "B"): "A-B", ("B", "C"): "B-C", ("C", "D"): "C-D", ("C", "E"): "C-E"})

# গ্রাফটি দেখানো
plt.title("Graph Representation")
plt.show()

