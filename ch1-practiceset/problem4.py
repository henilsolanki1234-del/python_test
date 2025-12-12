import os

def list_directory_contents(path='/'):
    """
    Prints the names of all entries (files and folders) in the given directory.
    If no path is provided, uses the current working directory.
    """
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")

if __name__ == "__main__":
    # Example usage:
    # If you want to list the current directory, just call without argument
    list_directory_contents()

    # Or specify a path:
    # list_directory_contents("/path/to/your/directory")
