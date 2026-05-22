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
            # Check if current coordinate is one of the 4 corners
            is_corner = (row == 0 and col == 0) or \
                        (row == 0 and col == x - 1) or \
                        (row == y - 1 and col == 0) or \
                        (row == y - 1 and col == x - 1)
            
            # Check if current coordinate is on an edge
            is_top_bottom = (row == 0) or (row == y - 1)
            is_left_right = (col == 0) or (col == x - 1)

            if is_corner:
                line += "o"
            elif is_top_bottom:
                line += "-"
            elif is_left_right:
                line += "|"
            else:
                line += " "
        print(line)