import os

def save(output, output_path):
    """
    Save the output to a file or print it if no output path is specified.

    Args:
        output (str or bytes): The output content to save.
        output_path (str, optional): The path to save the output.
    """
    if output_path:
        mode = 'w' if isinstance(output, str) else 'wb'
        with open(output_path, mode) as file:
            file.write(output)
    else:
        print(output)