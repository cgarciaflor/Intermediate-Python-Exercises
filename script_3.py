def dict(string):
    low = string.lower()
    remove = low.replace(" ","")

    dict1 = {}
    for ele in remove:
        dict1[ele] = dict1.get(ele,0) + 1
    print(dict1)

string = input("Enter an input: ")
dict(string)