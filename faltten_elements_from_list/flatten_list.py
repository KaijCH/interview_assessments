import collections

# iterative implementation
def flattens_iterative(elements: list) ->list:
    if not elements: 
        return []
    opts = collections.deque(elements)
    visits, res = {id(elements)}, []
    while opts:
        curr = opts.popleft()
        if not curr: 
            continue
        if isinstance(curr, int):
            res.append(curr)
            continue
        memo = id(curr)
        if memo in visits: 
            continue
        visits.add(memo)
        while curr: 
            ele = curr.pop()
            opts.appendleft(ele)
    return res


# recursive implementation
def recurs(elements: list, visits: set) -> list:
    visits.add(id(elements))
    res = []
    for ele in elements:
        if isinstance(ele, int):
            res.append(ele)
            continue
        if id(ele) in visits:
            continue
        res += recurs(ele, visits)
    return res

def flattens_recursive(elements: list) -> list:
    if not elements: 
        return []
    visits = set()
    return recurs(elements,  visits)
