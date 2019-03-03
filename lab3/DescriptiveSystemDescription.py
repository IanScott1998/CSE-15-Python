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
myVars = getVars(prop)
description = []

print "Your table uses the variables: ", myVars
for x in myVars:
    print "Enter meaning of ", x ,":"
    desc = raw_input()
    description.append(desc)
myTable = TruthTable(prop)  
consist = 0
#print myTable.table
isCase = 2
notCase = 2

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
        isCase = 1
    if total == 0.0:
        consist = 1
        notCase = 1
        
if(consist == 1):
     #print "Your description is consistent"

     print "Your description is consistent when: "
     true = []
     false = []
     for x in myVars:
         statement = description.pop()
         if isCase == 1:
             true.append(statement);
         if notCase == 1:
             false.append(statement);

     case1 = []
     case2 = []
     for x in true:
         #print x
         case1.append(["it is the case that ", x])
     for x in false:
         case2.append(["it is not the case that ", x])

     if case1 == []:
        print case2

     if case2 == []:
        print case1

     else:
        print case1, " or ", case2

     
else:
     print "Your description is not consistent"


    
