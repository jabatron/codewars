# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(ln):
    ln_aux = []
    c0 = 0
    for e in ln:
        if e != 0:
            ln_aux.append(e)
        else:
            c0 += 1
    for i in range(c0):
        ln_aux.append(0)

    return ln_aux

print (move_zeros([1, 0, 1, 2, 0, 1, 3]))