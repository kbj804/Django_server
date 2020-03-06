import csv
import json


# input_file_name = "data.csv"
# output_file_name = "data.txt"
# with open(r'./server_project/test/preprocess_data/manual_data.json', "r", encoding="utf-8", newline="") as input_file, \
#         open(r'./server_project/test/preprocess_data/result.csv', "w", encoding="utf-8", newline="") as output_file:
        
#     reader = csv.reader(input_file)
#     # 첫 줄은 col_names 리스트로 읽어 놓고
#     col_names = next(reader)
#     # 그 다음 줄부터 zip으로 묶어서 json으로 dumps
#     for cols in reader:
#         doc = {col_name: col for col_name, col in zip(col_names, cols)}
#         print(json.dumps(doc, ensure_ascii=False), file=output_file)


input_file_name = "./server_project/test/preprocess_data/manual_data.txt"
output_file_name = "./server_project/test/preprocess_data/data.csv"

with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
        open(output_file_name, "w", encoding="utf-8", newline="") as output_file:
    data = []
    for line in input_file:
        print(line)
        datum = json.loads(line)
        data.append(datum)
        
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(data[0].keys())
    for line in data:
        csvwriter.writerow(line.values())