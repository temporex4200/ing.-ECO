import matplotlib.pyplot as plt
import networkx as nx

# Código para definir actividades y cálculos de tiempos, holguras, etc.

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
etiquetas = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
for nodo in G.nodes():
    plt.text(pos[nodo][0], pos[nodo][1] + 0.1, s=f'ES={ES[nodo]}, EF={EF[nodo]}\nLS={LS[nodo]}, LF={LF[nodo]}\nHolgura={holgura[nodo]}', bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='center')

plt.title('Diagrama PERT con Detalles')
plt.show()
