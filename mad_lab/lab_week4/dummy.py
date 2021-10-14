import csv

student_id = '1001'
total = 0
dict_list = []
file_temp1 = open("data.csv", 'r')
file = csv.DictReader(file_temp1)
for row in file:
    if row["Student id"] == student_id:
        dict_list.append(row)
        total += int(row[" Marks"])
print("dict_list: ", dict_list)
print("total: ", total)
file_temp1.close()