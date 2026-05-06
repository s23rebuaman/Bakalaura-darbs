# https://realpython.com/python-csv/
# import csv

# marsruti = []

# with open('ventspils-reiss_marsruti.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         marsruti.append(row)
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} - {row[1]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')
#     print(len(marsruti))
#     print(marsruti[0])
#     print(marsruti[1])
#     print(marsruti[2])

#https://www.w3schools.com/PYTHON/python_mysql_insert.asp
import mysql.connector
#https://realpython.com/python-csv/
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootAdmin.2004",
  database="ventspils_reiss"
)

mycursor = mydb.cursor()

query = "INSERT INTO reisi (reisa_nr, reisa_nosaukums) VALUES (%s, %s)"

marsruti = []

with open('ventspils-reiss_marsruti.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    batch_size = 500 
    for row in csv_reader:
        marsruti.append(row)
        if line_count == 0:
            line_count += 1
        elif line_count > 0:
            values = marsruti[line_count]
            mycursor.execute(query, values)
            line_count += 1
        elif (line_count + 1) % batch_size == 0:
            mydb.commit()

print(line_count, "lines inserted.")