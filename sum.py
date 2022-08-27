List1=[int(x) for x in input().split()]
print("List is",List1)
def sum(x):
    sum=0
    for i in List1:
        sum=sum+i
    return sum
z=sum(List1)
print("sum of elements in list",z)   
