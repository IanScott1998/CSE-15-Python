from logic import TruthTable

print "enter proposition 1:"
p1 = raw_input()
print "enter proposition 2:"
p2 = raw_input()

myTable = TruthTable(["q","p"],[p1])
myTable2 = TruthTable(["q","p"],[p2])

if(myTable.table == myTable2.table):
    print "The propositions are equivalent."
else:
    print "The propositions are not equivalent."
myTable.latex()
myTable2.latex()
