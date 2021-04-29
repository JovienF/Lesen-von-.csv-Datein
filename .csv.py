import csv 
csv.list_dialects()

reader = csv.reader(open("C:\Users\Jovien\Lesen-von-.csv-Datein\sensor_360.csv"))
for row in reader:
    print(row)