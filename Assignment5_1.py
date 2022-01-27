n = int(input("Please enter the row number: "))
list1 = []
for i in range (n):
    pattern = []
    for j in range (i+1):
        if j==0 or j==i:
            pattern.append(1)
        else:
            pattern.append(list1[i-1][j-1] + list1[i-1][j])
    list1.append(pattern)
 

for i in range(n):
    for j in range(i+1):
        print(format(list1[i][j] ,"<4") ,end="")
    print()



