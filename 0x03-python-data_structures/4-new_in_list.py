#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    if idx < 0:
      return list_copy  
    elif    idx > len(my_list):
        return list_copy
    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
