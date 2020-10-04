def fibonacci(n1):
    '''
    uses generater to return fibonacci sequence 
    up to given # n dynamically
    '''
    a,b = 1,1

    for _ in range(0,n1):
        yield a
        a,b = b,a+b

    return a
