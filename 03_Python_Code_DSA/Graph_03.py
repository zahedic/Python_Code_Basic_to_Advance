import networkx as nx
import matplotlib.pyplot as plt

# নোড সংখ্যা নির্ধারণ করা (10 নোড)
num_nodes = 10

# একটি সম্পূর্ণ গ্রাফ তৈরি করা
G = nx.complete_graph(num_nodes)

# নোডগুলির অবস্থান পেতে একটি পেন্টাগ্রাম লেআউট ব্যবহার করা
pos = nx.shell_layout(G)

# গ্রাফ অঙ্কন করা
plt.figure(figsize=(6, 6))
nx.draw(G, pos, with_labels=False, node_color="blue", node_size=300, edge_color="black", width=1.5)
plt.show()
