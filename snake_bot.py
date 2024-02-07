def printfix(list):
    for xx, x in enumerate(list[:]):
        for yy, y in enumerate(x):
            if type(y) == type(0) and not y < 10:
                list[xx][yy] = str(y)
            else:
                list[xx][yy] = f" {y}"
        print(x)

def grid_maker(body, grid, walls):
    grid_save = [[" " for y in range(0, grid[1])] for x in range(0, grid[0]) ]
    for z in body:
        grid_save[z[0]][z[1]] = "b"
        
    if walls:
        grid_save.append(["w" for x in range(0, len(grid_save[1]))])
        grid_save.insert(0, ["w" for x in range(0, len(grid_save[1]))])
        for x in grid_save:
            x.append("w")
            x.insert(0, "w")
        
    return grid_save

def path_finder(head, body, target, grid):  
    around = [(0,-1), (-1,0), (1,0), (0,1)]
    grid_save = grid_maker(body, grid, walls=False)

    grid_save[int(head[0])][int(head[1])] = "H"
    grid_save[int(target[0])][int(target[1])] = 0


    #crea el mapa de numeros
    n = 0
    inicial_p = [(int(target[0]), int(target[1]))]
    finding = True
    while finding:
        if n > grid[0]*grid[1]:
            for xx, x in enumerate(grid_save):
                for yy, y in enumerate(x):
                    if grid_save[xx][yy] == " ":
                        grid_save[xx][yy] = 1
            finding = False

        n += 1
        inicial_p_save = inicial_p[:]
        inicial_p.clear()
        for y in inicial_p_save:
            for x in around:
                coords = x[0]+y[0], x[1]+y[1] 
                if coords[0]<0 or coords[0]>grid[0]-1 or coords[1]<0 or coords[1]>grid[1]-1:
                    pass
                elif grid_save[coords[0]][coords[1]] == " ":
                    grid_save[coords[0]][coords[1]] = n
                    inicial_p.append(coords)
                elif grid_save[coords[0]][coords[1]] == "H":
                    finding = False

    # darle las indicaciones a la serpiente en base a ese mapa de numeros
    around_ns = []         
    for x in around[:]:
        coords = head[0]+x[0], head[1]+x[1] 
        if coords[0]<0 or coords[0]>grid[0]-1 or coords[1]<0 or coords[1]>grid[1]-1:
            around.remove(x)
        elif type(grid_save[coords[0]][coords[1]]) == type(4):
            around_ns.append(grid_save[coords[0]][coords[1]])
        else:
            around.remove(x)
    
    try:
        return around[around_ns.index(min(around_ns))]
    except:
        return True