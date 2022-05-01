class BankEMP:
    
    def __init__(self,name,dept,age):
        self.name=name
        self.dept=dept
        self.age=age
        
    def __repr__(self):
        return'{'+self.name+','+self.dept+','+str(self.age)+'}'
            
if __name__=='__main__':
    emps=[
        BankEMP('Elijah','IT',20),
        BankEMP('NIK','Barking',21),
        BankEMP('Lucien','finance',19)
    ]
    
    #sort list by name in the natural order using 'attrgetterd()=
    emps.sort(key=attrgetter('name'))
    print(emps)