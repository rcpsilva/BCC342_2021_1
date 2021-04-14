import numpy as np

def generate_and_test(bounds,fobj):
    
    nvars = len(bounds)
    best_sol = []
    best_val = 0

    bounds = [np.arange(b[0],b[1]+1) for b in bounds]
    frontier = [[x] for x in bounds[0]]

    while frontier:
        solution = frontier.pop(0)

        if len(solution) == nvars:
            print(solution)
            s_val = fobj(solution)
            if best_sol:
                if s_val < best_val:
                    best_val = s_val
                    best_sol = solution
            else:
                best_val = s_val
                best_sol = solution
        else:
            for val in bounds[len(solution)][::-1]:
                frontier = [solution + [val]] + frontier

    return {'best_sol': best_sol,
            'best_val': best_val}

def permute_and_test(n,fobj):
    
    best_sol = []
    best_val = 0

    elements = set([i for i in range(n)]) 
    frontier = [[x] for x in range(n)]

    while frontier:
        solution = frontier.pop(0)

        if len(solution) == n:
            print(solution)
            s_val = fobj(solution)
            if best_sol:
                if s_val < best_val:
                    best_val = s_val
                    best_sol = solution
            else:
                best_val = s_val
                best_sol = solution
        else:
            new_solutions = []
            for val in elements - set(solution):
                new_solutions = new_solutions + [solution + [val]] 

            frontier = new_solutions + frontier


    return {'best_sol': best_sol,
            'best_val': best_val}

n = 4
fobj = lambda x : -np.sum(x)
bounds = [[0,1] for i in range(n)]
#bounds = [[0,1,2,3,4],[1,2,3,4,5],[1,2,3]]

#res = generate_and_test(bounds,fobj)

res = permute_and_test(n,fobj)
print(res)