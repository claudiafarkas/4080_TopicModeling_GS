import csv
import json
import os


file_path = 'tf_41178.csv'
file_name = os.path.basename(file_path)
print("The file name is:", file_name)

# Initialize list for body data
body_data = []

# Open CSV file and load content
with open(file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    print("Column names:", reader.fieldnames)
    for i, row in enumerate(reader):
        if i >= 1 and i < 40:  # counting from rows 2 to 40
            body_data.append(row['Body'])
            print("Body Output: \n", body_data)

# Write to JSON file
output_location = '/Users/Claudia/topicModeling-GS/topicModeling/tf_41178_bodyOutput.json'
with open(output_location, 'w') as json_file:
    json.dump(body_data, json_file)




