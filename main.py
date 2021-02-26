from utils import read_values
from csp import CSP
from solver import Solver 
from collections import OrderedDict


if __name__=='__main__':
    variables, domains, neighbors, assignment = read_values('tst.txt')
    csp = CSP(variables, domains, neighbors)
    solver = Solver(csp)
    output = solver.backtracking(assignment)
    if output is False:
        print('Sorry but there is no solution :(')
    else:
        print('Found solution! Here is what I assigned to each variable (key is variable, value is color):')
        print(OrderedDict(sorted(output[1].items())).items())
        csp.check_constraints(output[1])
        print('Thanks for using me. See you next time!')