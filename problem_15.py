
import sys

# ============================================================
def solve():
    """
    """
    grid_size = (20, 20)
    def routes(x, y):
        """ The most inefficient way to solve this problem;
        """
        if x == grid_size[0] and y == grid_size[1]:
            solve.total_routes += 1
            if solve.total_routes % 1000000 == 0:
                sys.stdout.write('\r%i' % solve.total_routes)
        if x < grid_size[0]:
            routes(x+1, y)
        if y < grid_size[1]:
            routes(x, y+1)
    
    solve.total_routes = 0
    routes(0, 0)
    return solve.total_routes

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()