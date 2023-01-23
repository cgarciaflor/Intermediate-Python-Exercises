def uniquelist(list):
    unique_list = []
    
    for val in list:
        if val not in unique_list:
            unique_list.append(val)
    print(unique_list)


list = []

n = int(input("Enter number of elements : "))

print("Enter all elements: ")


for e in range(0, n):
	ele = int(input())

	list.append(ele)

uniquelist(list)

my_list = [1,10,10,22,22,4,6,7,99,100,100]
uniquelist(my_list)


