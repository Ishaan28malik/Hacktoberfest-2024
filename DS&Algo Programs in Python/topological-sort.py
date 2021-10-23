
def topological_sort(graph, start):
    seen = set()
    stack = [] #path variable is gone, stack and order are new
    order = [] #order will be in reverse order at first
    s = [start]
    while s:
        x = s.pop()
        if x not in seen:
            seen.add(x) #no need to apend to path
            s.extend(graph[x])

            while stack and x not in graph[stack[-1]]:
                order.append(stack.pop())
            stack.append(x)

    return stack + order[::-1]
    
