import csv

with open('example4.csv','w') as csvfile:
    fieldnames=['first_name','last_name','grade']
    writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'grade':'b','first_name':'ALEX','last_name':'Brian'})
    writer.writerow({'grade':'a','first_name':'Rachael',
        'last_name':'rodriguez'})
    
    writer.writerow({'grade':'b','first_name':'Jane','last_name':'Oscar'})
    writer.writerow({'grade':'b','first_name':'Jane','last_name':'loive'})
    
    
    print("writing complete")
    

    