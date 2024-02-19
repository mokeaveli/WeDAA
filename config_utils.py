import json

def load_config(config_file_path):
    """
    Load configuration from a JSON file.

    Parameters:
    - config_file_path (str): The path to the configuration JSON file.

    Returns:
    - dict: The configuration settings loaded from the file.
    """
    try:
        with open(config_file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Configuration file not found at {config_file_path}.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the configuration file at {config_file_path}.")
        exit(1)
