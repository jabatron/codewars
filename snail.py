def snail(snail_map):
    x = len(snail_map[0])
    y = len(snail_map)
    print (f"x-> {x}, y-> {y}")
    x_s = 0
    x_dir = 1
    y_s = 0
    y_dir = 1
    # voy direccion X
    for x_aux in range(x_s, x, x_dir):
        print (snail_map[y_s][x_aux], end=",")

    x_dir = 1 if x_dir == -1 else -1

    #x_s += 1
    y_s += 1

    # voy dirección y
    for y_aux in range(y_s, y, y_dir):
        print (snail_map[y_aux][x_aux], end=",")
    
    y_dir = 1 if y_dir == -1 else -1
    #x_s +=1     

    x -= 1
    y -= 1
    # vuelvo direccion X
    for x_aux in range(x-1, x_s-1, x_dir):
        print (snail_map[y][x_aux], end=",")

    x_dir = 1 if x_dir == -1 else -1

    # vuelvo direccion y
    for y_aux in range(y-1, y_s-1, y_dir):
        print (snail_map[y_aux][x_s], end=",")
    
    y_dir = 1 if y_dir == -1 else -1

    # voy direccion X
    x_s += 1
    for x_aux in range(x_s, x, x_dir):
        print (snail_map[y_s][x_aux], end=",")

snail([[1,2,3], [4,5,6], [7,8,9]])