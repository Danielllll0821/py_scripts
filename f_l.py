def filter_list(l):
    'return a new list with the strings filtered out'
    L = []
    for i in range(0, len(l) - 1):
        
        if isinstance(l[i], int):
            e = l[i]
            L.append(e)
            #print(L)
        else:
            l.remove(l[i])
            
	return L


list1 = [1, 2, 'a', 'b',3]

filter_list(list1)
