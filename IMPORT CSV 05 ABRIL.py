import csv

myData=[["first_name","second_name","grade"],
        ['Alex','Brian','A'],
        ['Tom','smith','B']]
        
myFile =open('example2.csv','w')
with myFile:
        writer=csv.writer(myFile)
        writer.writerows(myData)
        
        print("writing complete")
