#Work will start here!!!

'''This Project is being made for the sole purpose of generating random data for matrices!'''
import random
no_of_rows_of_data = int(input("How many rows of data you want:"))
no_of_column_of_data = int(input("How many columns of data you want:"))


#def matrix_generator(norod,nocod):
'''
class Matrix_Gen():
    def matrix_data_generator(norod,nocod):
        x=[]
        for i in range(no_of_column_of_data):
            i= random.randint(0,10)
            x.append(i)
        print(x)

    def matrix_rows_genrator(nor):
        y=[]
        for i in range(no_of_rows_of_data):
            y.copy()
            print(y)


Matrix_Gen.matrix_generator(no_of_rows_of_data,no_of_column_of_data)
Matrix_Gen.matrix_rows_genrator(no_of_rows_of_data)

'''

#2nd approach
# since there would be n*k elements in a matrix
# me making a huge list and then breaking it into colums
# and would think of grouping each element later

#def no_of_elements(n :int,k: int): return n*k 
Toatal_no_of_data=no_of_rows_of_data*no_of_column_of_data

list_open = []
for i in range(Toatal_no_of_data): 
    m = random.randint(0,9)
    list_open.append(m)
print(list_open)
#print(elements(Toatal_no_of_data))

# generating number works

# now we breaking the list into n and k

#list slicing time?

def my_slicer():
    empty_list = []
    for i in range(no_of_rows_of_data):
        new_list =list_open[:no_of_column_of_data]
        new_list.sort()
        empty_list.append(f'{new_list}')
    return empty_list
print(my_slicer())
print(my_slicer()[0])