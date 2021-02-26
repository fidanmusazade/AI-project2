def read_values(filename):
    variables = set()
    domains = dict()
    neighbors = dict()
    assignment = dict()
    
    file = open(filename, 'r')
    line = file.readline()
    while(not line[:6]=='colors'):
        line = file.readline()
    colors = int(line[8:].strip())

    while(not line[0].isdigit()):
        line = file.readline()
    while(len(line)>0 and line[0].isdigit()):
        a, b = map(int, line.split(','))

        if a not in variables:
            variables.add(a)
            neighbors[a] = []
        if b not in variables:
            variables.add(b)
            neighbors[b] = []

        if b not in neighbors[a]:
            neighbors[a].append(b)
        if a not in neighbors[b]:
            neighbors[b].append(a)

        line = file.readline()
    variables = list(variables)
    for var in variables:
        domains[var] = [i for i in range(1, colors+1)]
    return variables, domains, neighbors, assignment