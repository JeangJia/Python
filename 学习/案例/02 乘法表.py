num=int(input("num:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f"{i} x {j} = {i*j} ",end="\t")
    print('')