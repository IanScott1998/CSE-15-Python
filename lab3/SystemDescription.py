from logic import TruthTable
from logic import getVars


prop = []
thing = 'Y'
thang = 'N'

while(thing != thang):
    prop.append(raw_input("Enter a Proposition: "))
   
    print "Would you like to enter more (Y/N): "
    thing = raw_input()

#myTable.display()

myTable = TruthTable(prop)  
consist = 0
#print myTable.table

for x in myTable.table:
    #print x
    stringTime = str(x)
    #print stringTime
    l = []
    for t in stringTime:
        try:
            l.append(int(t))
        except ValueError:
            pass
    #print l
    total = 0.0
    add = 0.0
    for i in l:
        add = add+i
        total = total+1
    total = add/total
    #print total
    if total == 1.0:
        consist = 1
    if total == 0.0:
        consist = 1
        
if(consist == 1):
     print "Your description is consistent"

else:
     print "Your description is not consistent"




    
