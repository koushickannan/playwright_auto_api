import csv
from typing import List, Dict, Any


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads a CSV file and returns a list of dictionaries, where each dictionary represents a row.
    The first row of the CSV is assumed to be the header.

    :param file_path: Path to the CSV file.
    :return: List of dictionaries containing the CSV data.
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv(file_path: str, data: List[Dict[str, Any]], fieldnames: List[str]):
    """
    Writes a list of dictionaries to a CSV file. The first row will be the header.

    :param file_path: Path to the CSV file.
    :param data: List of dictionaries containing the data to write.
    :param fieldnames: List of fieldnames for the CSV.
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
