import csv

results= []
with open('example2.csv') as File:
    reader= csv.DictReader(File)
    for row in reader:
        results.append(row)
        print (results)
    
    
    
    