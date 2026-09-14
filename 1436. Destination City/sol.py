paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

starts = set()
starts = {i for i,j in paths}
for i, j in paths:
    if j not in starts:
        print(j)