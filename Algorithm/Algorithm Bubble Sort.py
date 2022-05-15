from tkinter import *

def bubble_sort(num_list):
    indexing_length = len(num_list)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if num_list[i]>num_list[i+1]:
                sorted = False
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

        return num_list

print(bubble_sort([3,1,4,2,5]))


