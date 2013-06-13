#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0

    metacache = [1,2,8,3,6,9,17,4,20,7]
    max = 1
    if i <= j :
        k = j / 2
        if k > i :
            i = k

        for n in range(i,j):
            c = 0
            while n > 1 :
                if n < 10 :
                    c += metacache[n-1]
                    n = 1
                else:
                    if (n % 2) == 0 :
                        n = (n / 2)
                        c += 1
                    else :
                        n = ((3 * n) + 1)/2
                        c += 2
            if c > max :
                max = c;
    else :
        k = i / 2
        if k > j :
            j = k
        for n in range(j,i):
            c = 0
            while n > 1 :
                if n < 10 :
                    c += metacache[n-1]
                    n = 1
                else:
                    if (n % 2) == 0 :
                        n = (n / 2)
                        c += 1
                    else :
                        n = ((3 * n) + 1)/2
                        c += 2
            if c > max :
                max = c;

    return max

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)


