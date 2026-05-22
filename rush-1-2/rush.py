import sys

def rush(x, y):
    """
    Draws a square pattern based on x (width) and y (height)

    Args:
        x (int): Width of the pattern
        y (int): Height of the pattern
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""
        for col in range(x):
            # Edge case: 1D lines are all asterisks
            if x == 1 or y == 1:
                line += "*"
            # Corners
            elif row == 0 and col == 0:
                line += "/"
            elif row == 0 and col == x - 1:
                line += "\\"
            elif row == y - 1 and col == 0:
                line += "\\"
            elif row == y - 1 and col == x - 1:
                line += "/"
            # Edges
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                line += "*"
            else:
                line += " "
        print(line)