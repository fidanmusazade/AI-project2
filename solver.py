import numpy as np
import heapq

class Solver:
    '''
    Class that implements backtracking together with AC3 and heustics to color the graph
    Inputs:
        csp - Constraint Satisfaction Problem
    Methods:
        MRV - finds the value with minimum remaining values
        LCV - orders the colors (least constraining value first)
        AC3 - does AC3 pruning
        revise - used for AC3
        backtracking - implements the backtracking algorithm
    '''
    def __init__(self, csp):
        self.csp = csp

    def MRV(self, assignment):
        candidates = []
        for var in self.csp.variables:
            if var not in assignment:
                #sort by number of values in domain. if equal then take the one with most neighbors
                heapq.heappush(candidates, (len(self.csp.domains[var]), -len(self.csp.neighbors), var))
        return heapq.heappop(candidates)[2]

    def LCV(self, var, assignment):
        lcv = []
        for color in self.csp.domains[var]:
            breaks = 0

            for i in self.csp.neighbors[var]:
                if color in self.csp.domains[i]:
                    breaks += 1

            heapq.heappush(lcv, (breaks, color))

        return [i[1] for i in lcv]

    def AC3(self, queue, assignment):
        while len(queue) != 0:
            xi, xj = queue.pop()
            revised = self.revise(xi, xj)
            if revised:
                if len(self.csp.current_domain[xi]) == 0:
                    return False
                current_neighbors = [i for i in self.csp.neighbors[xi] if i != xj]
                for neighbor in current_neighbors:
                    if neighbor not in assignment:
                        queue.append([xi, neighbor])
        return True


    def revise(self, xi, xj):
        revised = False
        #only if single value is left in xj's domain and it is the same as color of xi, xi cannot have this color
        if len(self.csp.current_domain[xj]) == 1:
            color = self.csp.current_domain[xj][0]
            if color in self.csp.current_domain[xi]:
                self.csp.current_domain[xi].remove(color)
                revised = True
        return revised


    def backtracking(self, assignment): 
        if len(assignment)==len(self.csp.variables):
            return True, assignment
        
        var = self.MRV(assignment)
        ordered_colors = self.LCV(var, assignment)
        
        for color in ordered_colors:
            if (self.csp.is_safe(var, color, assignment)):
                self.csp.current_domain[var] = [color]
                arcs = list()
                
                for xj in self.csp.neighbors[var]:
                    # if xj not in assignment:
                    arcs.append([var, xj])
                
                passed = self.AC3(arcs, assignment)
                if passed:
                    assignment[var] = color
                    result = self.backtracking(assignment)
                    
                    if result:
                        return result
            try:
                del assignment[var]
            except:
                pass

        return False