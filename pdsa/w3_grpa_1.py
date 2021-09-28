def prelim_dict(L):
    """
    takes in a list of item names and return a dictionary with item names as keys and the 
    
    number of orders for corresponding items as values
    
    Eg: input: [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]
        
        output: {1006: 3, 1008: 4, 1009: 2, 1007: 4, 1005: 3, 1001: 3, 1003: 3, 1004: 4, 1002: 4}
    
    Parameters
    ----------
    L : List of integers

    Returns
    -------
    out : dictionary where both the keys and values are integers

    """
    out = {}
    for i in L:
        if i in out:
            out[i] += 1
        else:
            out[i] = 1
    return out

def count_list(D):
    """
    takes in a dictionary with item name as key and number of orders as value and returns
    
    list of number of orders sorted in descending order
    
    Eg: input: {1006: 3, 1008: 4, 1009: 2, 1007: 4, 1005: 3, 1001: 3, 1003: 3, 1004: 4, 1002: 4}
    
        output: [4, 3, 2]
    """
    count_list = []
    for i in D:
        count_list.append(D[i])
    count_list = sorted(count_list, reverse=True)
    count_list_final = []
    for i in count_list:
        if i in count_list_final:
            continue
        else:
            count_list_final.append(i)
    return count_list_final

def swap_key_value(D):
    """
    takes in a dictionary and swaps the keys with values where the new keys are the number of 
    
    orders and values are the list of all item names odered the corresponding number of times sorted in ascending order
    
    Eg: input: {1006: 3, 1008: 4, 1009: 2, 1007: 4, 1005: 3, 1001: 3, 1003: 3, 1004: 4, 1002: 4}
        
        output: {3: [1001, 1003, 1005, 1006], 4: [1002, 1004, 1007, 1008], 2: [1009]}

    Parameters
    ----------
    D : dictionary

    Returns
    -------
    first_dict: dictionary with keys and values swapped

    """
    first_dict = {}
    for i in D:
        if D[i] in first_dict:
            first_dict[D[i]].append(i)
            first_dict[D[i]].sort()
        else:
            first_dict[D[i]] = [i]
    return first_dict

def DishPrepareOrder(order_list):
    """
    takes in a list of items and ordered and returns a list of unique items sorted by
    
    the order of preperation

    Parameters
    ----------
    order_list : list of integers

    Returns
    -------
    out : list of integers

    """
    prelim_dictionary = prelim_dict(order_list)
    count_list_final = count_list(prelim_dictionary)
    swapped_dictionary = swap_key_value(prelim_dictionary)    
    out = []
    for i in count_list_final:
        out.extend(swapped_dictionary[i])
    return out
        

a = [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]

b = DishPrepareOrder(a)