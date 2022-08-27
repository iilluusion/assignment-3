x=input("enter string")

def count_upper_lower(x):
    upper = 0
    lower = 0
    for i in x:
        if i.isupper() is True:
            upper += 1
        elif i.islower() is True:
            lower += 1
    print("No. of Upper case characters:", upper)
    print("No. of lower case characters:", lower)

count_upper_lower(x)