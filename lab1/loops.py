i = 0
largest = None
while i<10:
    print "Enter a number:"
    j = int(raw_input())
    if j%2 != 0:
        if j > largest:
            largest=j
    i += 1
if largest != None:
    print largest
else:
    print "No odd numbers were entered"
