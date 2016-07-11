
# ============================================================
def solve():
    """
    """
    grid_size = (6, 6)
    # grid_size = (20, 20)
    def routes(x, y, total_routes):
        print x, y
        if x == grid_size[0] and y == grid_size[1]:
            return total_routes + 1
        if x < grid_size[0]:
            return routes(x+1, y, total_routes)
        if y < grid_size[1]:
            return routes(x, y+1, total_routes)

    return routes(1, 1, 0)

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()