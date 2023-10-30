import json

def compare_json(file1, file2, file3):
    # Load data from File1.json and File2.json
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    # Compare data from File1.json to File2.json
    missing_data = find_missing_data(data1, data2)

    # Save missing data to File3.json
    with open(file3, 'w') as f3:
        json.dump(missing_data, f3, indent=2)

    # Print missing record count
    print(f"Missing record count: {len(missing_data)}")

def find_missing_data(data1, data2):
    missing_data = []

    if isinstance(data1, dict) and isinstance(data2, dict):
        for key, value in data1.items():
            if key not in data2:
                missing_data.append({key: value})
            else:
                missing_data.extend(find_missing_data(value, data2[key]))

    elif isinstance(data1, list) and isinstance(data2, list):
        for i, item in enumerate(data1):
            if i < len(data2):
                missing_data.extend(find_missing_data(item, data2[i]))
            else:
                missing_data.append(item)

    return missing_data

if __name__ == "__main__":
    #MYSQL File
    file1_path = "GWA -Latest 27th OCT/GWA MYSQL- PP SG - 25_OCT/movies_0.json"
    #DDB File
    file2_path = "GWA -Latest 27th OCT/GWA DDB - PP SG - 27-OCT/movies_0.json"
    #Output File
    file3_path = "Output/MissingDDBRecords.json"

    compare_json(file1_path, file2_path, file3_path)
