import random
class Random_Data():
    
    def data_matrix(no_of_rows_of_data : int,no_of_column_of_data : int):
        list_open = []
        for i in range(no_of_rows_of_data*no_of_column_of_data): 
            m = random.randint(0,9)
            list_open.append(m)
        list_main = list_open
        mt_lst = []
        for _ in range(no_of_rows_of_data):
            mt_lst.append(list_main[:no_of_column_of_data])
            del list_main[:no_of_column_of_data]
        return mt_lst
    
    def null_matrix(no_of_rows_of_data : int,no_of_column_of_data : int):
        list_open = []
        for i in range(no_of_rows_of_data*no_of_column_of_data): 
            m = random.randint(0,0)
            list_open.append(m)
        list_main = list_open
        mt_lst = []
        for _ in range(no_of_rows_of_data):
            mt_lst.append(list_main[:no_of_column_of_data])
            del list_main[:no_of_column_of_data]
        return mt_lst
    
'''      #bro this one is hard!


        def identity_matrix(no_of_rows_of_data : int,no_of_column_of_data : int):
        list_open =[]
        for i in range(no_of_rows_of_data*no_of_column_of_data): 
            m = [0]*(no_of_rows_of_data*no_of_column_of_data)
            list_open.append(m)
        mt_lst = []
        for _ in range(no_of_rows_of_data):
            mt_lst.append(list_open[:no_of_column_of_data])
            del list_open[:no_of_column_of_data]
        return mt_lst
'''