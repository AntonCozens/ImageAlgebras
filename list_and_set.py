def list_to_set(list):
    if list == []:
        return []
    return _list_to_set_([], list[0], list[1:])

def _list_to_set_(hd, e, tl):
    if tl == []:
        return hd + [e]
    rest = remove_all(tl, [e])
    if rest == []:
        return hd + [e]
    return _list_to_set_(hd + [e], rest[0], rest[1:] ) 

def remove_all(l, d):
    if d == []:
        return l
    return remove_els(l, d[0], d[1:])

def remove_els(l, e, tl):
    if tl == []:
        return remove_el(l, e)
    return remove_els(remove_el(l, e), tl[0], tl[1:])

def remove_el(l, e):
    if e in l:
        l.remove(e)
        return remove_el(l, e)
    else:
        return l

print (remove_el([1,2,2,2,2,2,2,3],2))

print (remove_all([1,2,3], []))
print (remove_all([1,2,3], [2]))

print(list_to_set([]))
print (list_to_set([1, 2, 3, 1, 1, 2, 4, 3]))
