import networkx as nx
import sys

def distance(w1, w2):
    l2 = list(w2)
    for c in w1:
        if c in l2:
            del l2[l2.index(c)]
    return len(l2)


if __name__ == "__main__":
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
            for aword in words
            if aword != word and distance(word, aword) == 1]

    print(nx.shortest_path(g, sys.argv[3], sys.argv[4]))
