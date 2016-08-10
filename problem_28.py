
# =============================================================================
def get_corners(level):
    """ Devuelve las esquinas de un nivel. Los niveles deben ser impares
        por que el primer nivel es 1 y crecen de 2 en 2 (hacia los lados
        y hacia arriba y abajo)
    """
    if level % 2 == 0:
        raise Exception('Level must be odd')
    decrement = level - 1
    upper_right = level * level
    corners = [upper_right - (decrement * i) for i in range(4)]
    return corners


# =============================================================================
def solve():
    """ Se suma 1 por que el rango empieza en el nivel 3, el valor del
        nivel 1 es 1.
        Se evalua hasta 1002 para que se vea el nivel 1001
    """
    return 1 + sum(sum(get_corners(level)) for level in range(3, 1002, 2))


# =============================================================================
if __name__ == '__main__':
    print solve()
