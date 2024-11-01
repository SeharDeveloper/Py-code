# pattern(*) using nested loops..
#* 
#* * 
#* * *
#* * * *
#* * * * *
#* * * * * *
#* * * * * * *
#* * * * * * * *
#* * * * * * * * *
#* * * * * * * * *
#* * * * * * * *
#* * * * * * *
#* * * * * *
#* * * * *
#* * * *
#* * *
#* *
#*
rows=9
for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()

rows=9
for i in range(rows,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()