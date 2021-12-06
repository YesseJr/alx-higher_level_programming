#!/usr/bin/python3
def magic_calculation(a, b):
    j11 = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                j11 += (a**b)/i
        except:
            j11 = b + a
            break
    return j11
