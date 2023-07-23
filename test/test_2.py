import os
import json
import csv
import pickle


def traverse_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            result.append({
                "name": file,
                "parent": os.path.basename(root),
                "type": "file",
                "size": file_size
            })

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_directory_size(dir_path)
            result.append({
                "name": dir,
                "parent": os.path.basename(root),
                "type": "directory",
                "size": dir_size
            })

    return result


def get_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


directory = os.getcwd()
result = traverse_directory(directory)

json_file_path = "result.json"
save_to_json(result, json_file_path)

csv_file_path = "result.csv"
save_to_csv(result, csv_file_path)

pickle_file_path = "result.pickle"
save_to_pickle(result, pickle_file_path)
