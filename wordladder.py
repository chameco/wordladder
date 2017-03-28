import networkx as nx
import sys

words = set()

with open(sys.argv[1], "r") as f:
    for line in f:
        if line[0] == "*":
            continue
        words.add(line[0:int(sys.argv[2])])

g = nx.Graph(name="words")
g.add_nodes_from(words)
alphabet = [chr(x + 97) for x in range(0, 26)]
[g.add_edge(word, aword)
        for word in words
        for aword in [word[0:i] + ac + word[i+1:]
            for i in range(len(word))
            for ac in alphabet]
        if aword in words and aword != word]

print(nx.shortest_path(g, sys.argv[3], sys.argv[4]))
