def count(string):
    count_upper = 0
    count_lower = 0
    for i in string:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    print("No. of Upper case characters:", count_upper,
          "No. of lower case characters:", count_lower)


str1 = "The quick Brow Fox"
a = (str1)
count(a)
