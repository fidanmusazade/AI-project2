class CSP():
    '''
    Class for solving graph coloring CSP problem
    
    Inputs:
        variables - the list of variables to color
        domains - available color options for each variable
        neighbors - neighbors of each variable
        
    Methods:
        is_safe - check whether an assignment is safe according to constraints
        check_constraints - check if all constraints are followed
    '''
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.current_domain = {v: list(self.domains[v]) for v in self.variables}
    
    def is_safe(self, var, color, assignment):
        for i in self.neighbors[var]:
            if i in assignment and assignment[i]==color:
                return False
        return True
    
        
    def check_constraints(self, assignment):
        flag = 0
        for var in self.variables:
            for neighbor in self.neighbors[var]:
                if assignment[var]==assignment[neighbor]:
                    flag = 1
                    print('OOPS...Something went wrong!')
        if not flag:
            print('All constraints are satisfied. Congratulations!')