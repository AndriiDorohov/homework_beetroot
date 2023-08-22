import json
from json.decoder import JSONDecodeError


def read_dataset(file_path):
    try:
          with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist or is not accessible.")
        return None
    except JSONDecodeError as e:
         print(f"The phone book is missing or empty: {e}")
         return None

def write_dataset(dataset, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dataset, file)
