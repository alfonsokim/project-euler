from collections import namedtuple

TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".strip().split('\n')

# ============================================================
SimpleEdge = namedtuple('SimpleEdge', 'value, left, right')

# ------------------------------------------------------------
class Edge(SimpleEdge):
    """
    """

    def max_route(self):
        """
        """
        if self.left.value > self.right.value:
            return self.left
        else:
            return self.right

    def next(self):
        """
        """
        return None not in [self.left, self.right]

# ============================================================
def build_tree():
    """
    """
    null_edge = Edge(value=0, left=None, right=None)
    edges = [Edge(value=int(v), left=null_edge, right=null_edge) 
             for v in TRIANGLE[len(TRIANGLE)-1].split(' ')]
    levels = [edges]
    for level_idx in range(len(TRIANGLE)-2, -1, -1):
        level = TRIANGLE[level_idx].split(' ')
        last_level = levels[-1]
        level_edges = []
        for edge_idx in range(len(level)):
            edge = Edge(value=int(level[edge_idx]), 
                        left=last_level[edge_idx],
                        right=last_level[edge_idx + 1])
            level_edges.append(edge)
        levels.append(level_edges)
    return levels[-1][0]

# ============================================================
def solve():
    """
    """
    level = build_tree()
    accumulated = 0
    while level.next():
        print level.value
        accumulated += level.value
        level = level.max_route()
    return accumulated

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()