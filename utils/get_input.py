"""
The input values module
"""
def get_inputs (text, columns):
    """
    Create a inputs of columns
    """
    values = []
    for column in columns:
        value = input(f"{text} {column[0]}")
        if value :
            values.append((column[0], value))

    return dict(values)
