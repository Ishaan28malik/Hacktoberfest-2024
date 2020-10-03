import hillclimb

def objective_function(i):
    return i

max_evaluations=500

def test_simple_hillclimb():
    '''
    test whether given a really simple move
    operator that just increments the number given
    we always end up with with largest number
    we can get after the number of evaluations
    we specify
    '''
    def move_operator(i):
        yield i+1
    def init_function():
        return 1
    
    num_evaluations,best_score,best=hillclimb.hillclimb(init_function,move_operator,objective_function,max_evaluations)
    
    assert num_evaluations == max_evaluations
    assert best == max_evaluations
    assert best_score == max_evaluations

def test_peak_hillclimb():
    '''
    check we hit the peak value (and don't iterate more than we need to)
    '''
    def move_operator(i):
        if i < 100:
            yield i+1
    def init_function():
        return 1
    
    
    num_evaluations,best_score,best=hillclimb.hillclimb(init_function,move_operator,objective_function,max_evaluations)
    
    assert num_evaluations <= max_evaluations
    assert num_evaluations == 100
    assert best == 100
    assert best_score == 100

def test_hillclimb_and_restart():
    '''
    see whether we restart on each number correctly
    '''
    def move_operator(i):
        # even numbers only go up to 50
        if i % 2 == 0 and i < 50:
            yield i+2
        elif i % 2 != 0 and i < 100: # odd numbers go higher
            yield i+2

    def init_function_gen():
        yield 2 # start off on the even numbers then restart on odds
        while True:
            yield 3
    init_gen=init_function_gen()
    init_function=lambda: init_gen.next()
    
    
    num_evaluations,best_score,best=hillclimb.hillclimb_and_restart(init_function,move_operator,objective_function,max_evaluations)
    
    # should have used all iterations
    assert num_evaluations == max_evaluations
    # should have jumped onto odd numbers
    assert best == 101
    assert best_score == 101

def test_hillclimb_and_restart_getting_worse():
    '''
    see whether we restart on each number correctly
    '''
    def move_operator(i):
        # even numbers only go up to 50
        if i % 2 == 0 and i < 50:
            yield i+2
        elif i % 2 != 0 and i < 100: # odd numbers go higher
            yield i+2
    
    def init_function_gen():
        yield 3 # start off on the odd numbers then restart on evens
        while True:
            yield 2
    init_gen=init_function_gen()
    init_function=lambda: init_gen.next()
    
    num_evaluations,best_score,best=hillclimb.hillclimb_and_restart(init_function,move_operator,objective_function,max_evaluations)
    
    # should have used all iterations
    assert num_evaluations == max_evaluations
    # should have retained score from odd numbers
    assert best == 101
    assert best_score == 101

    