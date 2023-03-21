"""
The utilities module
"""

def get_inputs (columns):
    """
    Create a inputs of columns
    """
    values = []
    for column in columns:
        print(f"Insira a {column[0]}")
        value = input()
        if value :
            values.append((column[0], value))

    return dict(values)
