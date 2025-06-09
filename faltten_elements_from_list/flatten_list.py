import collections

def flattens(elements: list) ->list:
    if not elements: return []
    res = []
    visits = set()
    opts = collections.deque(elements)
    while opts:
        curr = opts.popleft()
        if not curr: continue
        if id(opts) == id(curr) or id(curr) in visits: continue
        visits.add(id(curr))
        visits.add(id(opts))
        if isinstance(curr, int):
            res.append(curr)
        else:
            while curr:
                ele = curr.pop()
                opts.appendleft(ele)
    return res
