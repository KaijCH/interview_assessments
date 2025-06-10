import collections

# iterative implementation
def flattens_iterative(elements: list) ->list:
    if not elements: return []
    opts = collections.deque(elements)
    visits, res = {id(elements)}, []
    while opts:
        curr = opts.popleft()
        if not curr: continue
        if isinstance(curr, int):
            res.append(curr)
            continue
        if id(curr) in visits: continue
        visits.add(id(curr))
        while curr:
            ele = curr.pop()
            opts.appendleft(ele)
    return res


# recursive implementation
def recurs(elements: list, visits: set) -> list:
    res = []
    visits.add(id(elements))
    for ele in elements:
        if id(ele) in visits:
            continue
        if isinstance(ele, int):
            res.append(ele)
        else:
            res += recurs(ele, visits)
    return res

def flattens_recursive(elements: list) -> list:
    if not elements: return []
    visits = set()
    visits.add(id(elements))
    return recurs(elements,  visits)
