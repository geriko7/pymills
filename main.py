#!/usr/bin/python
# SETTINGS - PLEASE FILL THEM IN!
# # THERE ARE NO ERROR CATCHINGS IF YOU DON'T FILL THEM IN

#no settings yet?? - and will get no later, too...

# You shall read this note... just, please...
# I forgot to comment a lot of stuff, so, if You
# understand anything. Comment it.
# Thanks for your understanding.

""" A gift below
/* I'm an indentation bunny  */
/*                I prevent  */
/*  ()()          changes to */
/*  ('.')         this code. */
/*  (()()                    */
/* *(_()()                   */
"""



# LOADING BELOW

# IMPORTING
import os
import platform
import random
import sys

try:
    if sys.argv[1] == "debug":
        debug = True
    else:
        debug = False
except KeyboardInterrupt:
    raise KeyboardInterrupt
except:
    debug = False


if True: # EMPTIER - SETTER - OR ANYTHING IT IS...
    inmillP = [] # Player's InMill
    inmill = [] # Opponent's InMill
    a7=d7=g7=b6=d6=f6=c5=d5=e5=a4=b4=c4=e4=f4=g4=c3=d3=e3=b2=d2=f2=a1=d1=g1="*"
    phase = "placement"
    thebad = 0
    pcslft = 9
    bd = 0
    rmvd = 0
    opcslft = 9
    last = 0
    go2 = 0
    dontmove = []
    cs = 0
    qr = 0
    strats = 0 # everything is an emptier here. So i wont comment anything
    #choice = 0 # just an emptier - not necessary atm (around at the line of 987)
    rest = True
    rest2 = 0
    ailvl = "Test" # debug only
    strategy = 999
    put = 0 # debug only
    pcs = 9
    opcs = 9
# # MILLS INIT
try:
    strategy = int(sys.argv[2])
    cs = int(sys.argv[2])
except:
    pass
# DEFINITIONS
if True:
    def clear(): # just clearing the screen...
        if sysname == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    def pmill2(a,b,c,side): # yeah, will use it later. Try to understand it
        if side == "opp":
            if (
                a == "X" and b == "X" and c == "O" or
                a == "X" and b == "O" and c == "X" or
                a == "O" and b == "X" and c == "X"
                ):
                return True
            else:
                return False
        else:
            return False
    def pmill(a,b,c,side): # like above
        if side == "opp":
            if (
                a == "X" and b == "X" and c == "*" or
                a == "X" and b == "*" and c == "X" or
                a == "*" and b == "X" and c == "X"
                ):
                return True
            else:
                return False
        elif side == "player":
            if (
                 a == "O" and b == "O" and c == "*" or
                 a == "O" and b == "*" and c == "O" or
                 a == "*" and b == "O" and c == "O"
                 ):
                 return True
            else:
                return False
        else:
            return False
    def notmill(a,b,c): # nocomment.
        if a == "O" and b == "O" and c != "O":
            return True
        elif a == "O" and b != "O" and c == "O":
            return True
        elif a != "O" and b == "O" and c == "O":
            return True
        elif a != "O" and b != "O" and c == "O":
            return True
        elif a != "O" and b == "O" and c != "O":
            return True
        elif a == "O" and b != "O" and c != "O":
            return True
        elif a != "O" and b != "O" and c != "O":
            return True
        elif a == "O" and b == "O" and c == "O":
            return False
        else:
            return False
    def notmillO(a,b,c):
        if a == "X" and b == "X" and c != "X":
            return True
        elif a == "X" and b != "X" and c == "X":
            return True
        elif a != "X" and b == "X" and c == "X":
            return True
        elif a != "X" and b != "X" and c == "X":
            return True
        elif a != "X" and b == "X" and c != "X":
            return True
        elif a == "X" and b != "X" and c != "X":
            return True
        elif a != "X" and b != "X" and c != "X":
            return True
        elif a == "X" and b == "X" and c == "X":
            return False
        else:
            return False
    def choose_strategy(disallow):
        global cs
        try:
            global sat
            print sat
        except:
            pass
        if phase == "placement":
            sx = ("*", "X")
            strategy = []
            if cs == 0:
                priority = 1.0
                if (
                    a1 in sx and a7 in sx and g7 in sx
                    ):
                    if disallow != "1" and disallow != 1:
                        if (
                            a1 == "X" or g7 == "X" or a7 == "X"
                            ):
                            priority+=0.4
                        strategy.append("%d,1" % priority)
                if (
                    a7 in sx and g7 in sx and g1 in sx
                    ):
                    if disallow != "2" and disallow != 2:
                        if (
                            a7 == "X" or g1 == "X" or g7 == "X"
                            ):
                            priority+=0.4
                        strategy.append("%d,2" % priority)
                if (
                    g7 in sx and g1 in sx and a1 in sx
                    ):
                    if disallow != "3" and disallow != 3:
                        if (
                            a1 == "X" or g1 == "X" or g7 == "X"
                            ):
                            priority+=0.4
                        strategy.append("%d,3" % priority)
                if (
                    d2 in sx and d1 in sx and d3 in sx and
                    b2 in sx and f2 in sx
                    ):
                    if disallow != "4" and disallow != 4:
                        if (
                            d1 == "X" or b2 == "X"
                            ):
                            priority+=0.4
                        if (
                            d2 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,4" % priority)
                if (
                    g4 in sx and f4 in sx and e4 in sx and
                    f2 in sx and f6 in sx
                    ):
                    if disallow != "5" and disallow != 5:
                        if (
                            f2 == "X" or g4 == "X"
                            ):
                            priority+=0.4
                        if (
                            f4 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,5" % priority)
                if (
                    d7 in sx and d6 in sx and d5 in sx and
                    b6 in sx and f6 in sx
                    ):
                    if disallow != "6" and disallow != 6:
                        if (
                            d7 == "X" or b6 == "X"
                            ):
                            priority+=0.4
                        if (
                            d6 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,6" % priority)
                if (
                    a4 in sx and b4 in sx and c4 in sx and
                    b6 in sx and b2 in sx
                    ):
                    if disallow != "7" and disallow != 7:
                        if (
                            c4 == "X" or b2 == "X"
                            ):
                            priority+=0.4
                        if (
                            b4 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,7" % priority)
                if (
                    b4 in sx and b2 in sx and d2 in sx and
                    b6 in sx and f2 in sx
                    ):
                    if disallow != "8" and disallow != 8:
                        if (
                            b4 == "X" or d2 == "X"
                            ):
                            priority+=0.4
                        if (
                            b2 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,8" % priority)
                if (
                    f2 in sx and f4 in sx and d2 in sx and
                    b2 in sx and f6 in sx
                    ):
                    if disallow != "9" and disallow != 9:
                        if (
                            d2 == "X" or f4 == "X"
                            ):
                            priority+=0.4
                        if (
                            f2 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,9" % priority)
                if (
                    f6 in sx and d6 in sx and f4 in sx and
                    b6 in sx and f2 in sx
                    ):
                    if disallow != "10" and disallow != 10:
                        if (
                            d6 == "X" or f4 == "X"
                            ):
                            priority+=0.4
                        if (
                            f6 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,10" % priority)
                if (
                    d6 in sx and b6 in sx and b4 in sx and
                    b2 in sx and f6 in sx
                    ):
                    if disallow != "11" and disallow != 11:
                        if (
                            d6 == "X" or b4 == "X"
                            ):
                            priority+=0.4
                        if (
                            b6 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,11" % priority)
                if (
                    c4 in sx and c3 in sx and d3 in sx and
                    e3 in sx and c5 in sx
                    ):
                    if disallow != "12" and disallow != 12:
                        if (
                            c4 == "X" or d3 == "X"
                            ):
                            priority+=0.4
                        if (
                            c3 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,12" % priority)
                if (
                    e4 in sx and e3 in sx and d3 in sx and
                    c3 in sx and e5 in sx
                    ):
                    if disallow != "13" and disallow != 13:
                        if (
                            d3 == "X" or e4 == "X"
                            ):
                            priority+=0.4
                        if (
                            e3 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,13" % priority)
                if (
                    e5 in sx and e4 in sx and d5 in sx and
                    c5 in sx and e3 in sx
                    ):
                    if disallow != "14" and disallow != 14:
                        if (
                            e4 == "X" or d5 == "X"
                            ):
                            priority+=0.4
                        if (
                            e5 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,14" % priority)
                if (
                    d5 in sx and c5 in sx and c4 in sx and
                    c3 in sx and e5 in sx
                    ):
                    if disallow != "15" and disallow != 15:
                        if (
                            c4 == "X" or d5 == "X"
                            ):
                            priority+=0.4
                        if (
                            c5 == "X"
                            ):
                            priority-=0.4
                        strategy.append("%d,15" % priority)
                if (
                    a1 in sx and g7 in sx and g1 == "*" or
                    a1 in sx and g7 in sx and a7 == "*"
                    ):
                    if disallow != "16" and disallow != 16:
                        strategy.append("%d,16" % priority)
                if (
                    g1 in sx and a7 in sx and g7 == "*" or
                    g1 in sx and a7 in sx and a1 == "*"
                    ):
                    if disallow != "17" and disallow != 17:
                        strategy.append("%d,17" % priority)
                # THE UNIQUE STRATEGY BELOW
                if (
                    a7 in sx and d1 in sx and g1 in sx and
                    a1 in sx and a4 in sx
                    ):
                    if disallow != "18" and disallow != 18:
                        strategy.append("%d,18" % priority)
                if (
                    g4 in sx and a1 in sx and g1 in sx and
                    d1 in sx and g7 in sx
                    ):
                    if disallow != "19" and disallow != 19:
                        strategy.append("%d,19" % priority)
                if (
                    g7 in sx and d1 in sx and g1 in sx and
                    g4 in sx and a1 in sx
                    ):
                    if disallow != "20" and disallow != 20:
                        strategy.append("%d,20" % priority)
                if (
                    g4 in sx and g7 in sx and a7 in sx and
                    d7 in sx and g1 in sx
                    ):
                    if disallow != "21" and disallow != 21:
                        strategy.append("%d,21" % priority)
                if (
                    b6 in sx and b2 in sx and d2 in sx and
                    b4 in sx and f2 in sx
                    ):
                    if disallow != "22" and disallow != 22:
                        strategy.append("%d,22" % priority)
                if (
                    b2 in sx and f2 in sx and f4 in sx and
                    d2 in sx and f6 in sx
                    ):
                    if disallow != "23" and disallow != 23:
                        strategy.append("%d,23" % priority)
                if (
                    d2 in sx and f2 in sx and f6 in sx and
                    f4 in sx and b2 in sx
                    ):
                    if disallow != "24" and disallow != 24:
                        priority = 1.0
                        if (
                            d2 == "X" or f2 == "X" or f6 == "X"
                            ):
                            priority+=0.4
                        strategy.append("%d,24" % priority)
                if (
                    b6 in sx and f4 in sx and f6 in sx and
                    d6 in sx and f2 in sx
                    ):
                    if disallow != "25" and disallow != 25:
                        priority = 1.0
                        if (
                            b6 == "X" or f6 == "X" or f4 == "X"
                            ):
                            priority+=0.4
                        strategy.append("%d,25" % priority)
                if (
                    f6 in sx and b6 in sx and b4 in sx and
                    d6 in sx and b2 in sx
                    ):
                    if disallow != "26" and disallow != 26:
                        priority = 1.0
                        if (
                            b4 == "X" or b6 == "X" or
                            f6 == "X"
                            ):
                            priority+=0.4
                        strategy.append("%d,26" % priority)
                ## SHALL CONTINUE!! (with inner & mid stuff)
                
                
                
                ## NEW TECH IDEA!
                ### PRIORITY CHOOSING INSTEAD OF RANDOM CHOOSING
                ### BETWEEN STRATEGIES!
                if isinstance(strategy, list) and strategy != []:
                    i = max(strategy).split(',')
                    # i[0] is priority and i[1] is strategy
                    global strategy
                    strategy = int(i[1])
                    """
                    global strategy
                    try:
                        strategy = random.choice(strategy)
                    except IndexError:
                        print strategy
                        print "IndexError"
                        raw_input()
                    """
                else:
                    strategy = 999
            else:
                strategy = cs
        elif phase == "game" or phase == "fly":
            sx = ("*","X")
            strategy = []
            if cs == 0:
                if (
                    b2 == "*" and d2 == "*" and f2 == "*"
                    ):
                    if disallow != "1" and disallow != 1:
                        strategy.append(1)
                """
                if (
                    a1 == "*" and d1 == "*" and g1 == "*"
                    ):
                    if disallow != "2" and disallow != 1:
                        strategy.append(2)
                """
                if isinstance(strategy, list) and strategy != []:
                    global strategy
                    try:
                        strategy = random.choice(strategy)
                        sat = 1
                    except IndexError:
                        print strategy
                        print "IndexError"
                        raw_input()
                else:
                    strategy = 999
                    sat = 0
                    cs = 0
                    return
            else:
                strategy = cs
                sat = 1
        elif phase == "ofly" or phase == "bfly":
            sx = ("*","X")
            strategy = []
            strategy = 999
            """
            if cs == 0:
                if (
                    True == False
                    ):
                    if disallow != "1" and disallow != 1:
                        strategy.append(1)
                    if isinstance(strategy, list) and strategy != []:
                        global strategy
                        try:
                            strategy = random.choice(strategy)
                        except IndexError:
                            print strategy
                            print "IndexError"
                            raw_input()
                    else:
                        strategy = 999
            else:
                strategy = cs
            """
        sat = 1
    def use_strategy():
        sx = ("*","X")
        global strategy
        global cs
        global sat
        sat = 1
        if phase == "placement":
            # checking mill opportunities
            for i in possible_mills:
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill(a,b,c,"opp"):
                    for y in [i[0],i[1],i[2]]:
                        exec("x = " + y)
                        if x == "*":
                            exec("global " + y + " ; " + y + " = 'X'")
                            return
                        else:
                            continue
            # checking mill oppurtinities above
            # checking player's mill opportunities
            #if opcslft != 1: # should work a lil bit on it
            for i in possible_mills:
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill(a,b,c,"player"):
                    for y in [i[0],i[1],i[2]]:
                        exec("x = " + y)
                        if x == "*":
                            exec("global " + y + " ; " + y + " = 'X'")
                            return
                        else:
                            continue
            # checking player's strategy
            # # Strategy 1
            if (
                a4 == "O" and d1 == "O" and a1 == "*" and
                g1 == "*" and a7 == "*"
                ):
                if g4 == "*":
                    global g1
                    g1 = "X"
                elif d7 == "*":
                    global a7
                    a7 = "X"
                else:
                    global a1
                    a1 = "X"
                return
            if (
                g4 == "O" and d1 == "O" and g1 == "*" and
                a1 == "*" and g7 == "*"
                ):
                if d7 == "*":
                    global g7
                    g7 = "X"
                elif a4 == "*":
                    global a1
                    a1 = "X"
                else:
                    global g1
                    g1 = "X"
                return
            if (
                g4 == "O" and d7 == "O" and g7 == "*" and
                a7 == "*" and g1 == "*"
                ):
                if d1 == "*":
                    global g1
                    g1 = "X"
                elif a4 == "*":
                    global a7
                    a7 = "X"
                else:
                    global g7
                    g7 = "X"
                return
            if (
                a4 == "O" and d7 == "O" and a7 == "*" and
                a1 == "*" and g7 == "*"
                ):
                if d1 == "*":
                    global a1
                    a1 = "X"
                elif g4 == "*":
                    global g7
                    g7 = "X"
                else:
                    global a7
                    a7 = "X"
                return
            if (
                b4 == "O" and d2 == "O" and b2 == "*" and
                f2 == "*" and b6 == "*"
                ):
                if f4 == "*":
                    global f2
                    f2 = "X"
                elif d6 == "*":
                    global b6
                    b6 = "X"
                else:
                    global b2
                    b2 = "X"
                return
            if (
                d2 == "O" and f4 == "O" and f2 == "*" and
                b2 == "*" and f6 == "*"
                ):
                if b4 == "*":
                    global b2
                    b2 = "X"
                elif d6 == "*":
                    f6 = "X"
                else:
                    global f2
                    f2 = "X"
                return
            if (
                f4 == "O" and d6 == "O" and f6 == "*" and
                f2 == "*" and b6 == "*"
                ):
                if b4 == "*":
                    global b6
                    b6 = "X"
                elif d2 == "*":
                    global f2
                    f2 = "X"
                else:
                    global f6
                    f6 = "X"
                return
            if (
                b4 == "O" and d6 == "O" and b6 == "*" and
                f6 == "*" and b2 == "*"
                ):
                if d2 == "*":
                    global b2
                    b2 = "X"
                elif f4 == "*":
                    global f6
                    f6 = "X"
                else:
                    global b6
                    b6 = "X"
                return
            if (
                c4 == "O" and d3 == "O" and c3 == "*" and
                e3 == "*" and c5 == "*"
                ):
                if e4 == "*":
                    global e3
                    e3 = "X"
                elif d5 == "*":
                    global c5
                    c5 = "X"
                else:
                    global c3
                    c3 = "X"
                return
            if (
                d3 == "O" and e4 == "O" and e3 == "*" and
                c3 == "*" and e5 == "*"
                ):
                if c4 == "*":
                    global c3
                    c3 = "X"
                elif d5 == "*":
                    global e5
                    e5 = "X"
                else:
                    global e3
                    e3 = "X"
                return
            if (
                e4 == "O" and d5 == "O" and e5 == "*" and
                e3 == "*" and c5 == "*"
                ):
                if c4 == "*":
                    global c5
                    c5 = "X"
                elif d3 == "*":
                    global e3
                    e3 = "X"
                else:
                    global e5
                    e5 = "X"
                return
            if (
                c4 == "O" and d5 == "O" and c5 == "*" and
                c3 == "*" and e5 == "*"
                ):
                if d3 == "*":
                    global c3
                    c3 = "X"
                elif e4 == "*":
                    global e5
                    e5 = "X"
                else:
                    global c5
                    c5 = "X"
                return
            # # Strategy 2
            if (
                a1 == "O" and g7 == "O" and g1 == "*" or
                a1 == "O" and g7 == "O" and a7 == "*"
                ):
                ggo = 0
                if g1 == "*":
                    global g1
                    g1 = "X"
                elif a7 == "*":
                    global a7
                    a7 = "X"
                else:
                    ggo = 1
                if ggo != 1:
                    return
            if (
                a7 == "O" and g1 == "O" and a1 == "*" or
                a7 == "O" and g1 == "O" and g7 == "*"
                ):
                ggo = 0
                if a1 == "*":
                    global a1
                    a1 = "X"
                elif g7 == "*":
                    global g7
                    g7 = "X"
                else:
                    ggo = 1
                if ggo != 1:
                    return
            if (
                b2 == "O" and f6 == "O" and f2 == "*" or
                b2 == "O" and f6 == "O" and b6 == "*"
                ):
                ggo = 0
                print ggo
                if f2 == "*":
                    global f2
                    f2 = "X"
                elif b6 == "*":
                    global b6
                    b6 = "X"
                else:
                    ggo = 1
                if ggo != 1:
                    return
            if (
                b6 == "O" and f2 == "O" and b2 == "*" or
                b6 == "O" and f2 == "O" and f6 == "*"
                ):
                ggo = 0
                if b2 == "*":
                    global b2
                    b2 = "X"
                elif f6 == "*":
                    global f6
                    f6 = "X"
                else:
                    ggo = 1
                if ggo != 1:
                    return
            if (
                c3 == "O" and e5 == "O" and e3 == "*" or
                c3 == "O" and e5 == "O" and c5 == "*"
                ):
                ggo = 0
                if e3 == "*":
                    global e3
                    e3 = "X"
                elif c5 == "*":
                    global c5
                    c5 = "X"
                else:
                    ggo = 1
                if ggo != 1:
                    return
            if (
                e3 == "O" and c5 == "O" and c3 == "*" or
                e3 == "O" and c5 == "O" and e5 == "*"
                ):
                ggo = 0
                if c3 == "*":
                    global c3
                    c3 = "X"
                elif e5 == "*":
                    global e5
                    e5 = "X"
                else:
                    ggo = 1
                if ggo != 1:
                    return
            # Strategy 3
            if (
                d3 == "O" and f2 == "O" and d2 == "*" and
                b2 == "*" and d1 == "*" or
                d3 == "O" and b2 == "O" and d2 == "*" and
                f2 == "*" and d1 == "*" or
                d1 == "O" and b2 == "O" and d2 == "*" and
                d3 == "*" and f2 == "*" or
                d1 == "O" and f2 == "O" and d2 == "*" and
                d3 == "*" and b2 == "*"
                ):
                if b2 == "*" and b4 == "*":
                    global b2
                    b2 = "X"
                elif f2 == "*" and f4 == "*":
                    global f2
                    f2 = "X"
                elif ( 
                    a1 == "*" and d1 == "*" or
                    g1 == "*" and d1 == "*"
                    ):
                    global d1
                    d1 = "X"
                elif (
                    d3 == "*" and c3 == "*" or
                    d3 == "*" and e3 == "*"
                    ):
                    global d3
                    d3 = "X"
                else:
                    global d2
                    d2 = "X"
                return
            ## SHALL CONTINUE!!!!!
            # checking player's strategy above
            if strategy == 1:
                cs = 1
                global a7;global a1;global g7
                if (
                    a1 in sx and a4 in sx and a7 in sx and
                    d7 in sx and g7 in sx
                    ):
                    cs = 1
                    if a1 == "*":
                        a1 = "X"
                    elif g7 == "*":
                        g7 = "X"
                    elif a7 == "*":
                        a7 = "X"
                    else:
                        sat = 0
                        thebad = 1
                        cs = 0
                        return
                else:
                    sat = 0
                    cs = 0
                    thebad = 1
                    return
            if strategy == 2:
                cs = 2
                global a7;global g7;global g1
                if (
                    a7 in sx and g1 in sx and g7 in sx and
                    g4 in sx and d7 in sx
                    ):
                    if a7 == "*":
                        a7 = "X"
                    elif g1 == "*":
                        g1 = "X"
                    elif g7 == "*":
                        g7 = "X"
                    else:
                        sat = 0
                        thebad = 2
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 2
                    cs = 0
                    return
            if strategy == 3:
                cs = 3
                global a1;global g1;global g7
                if (
                    g7 in sx and g1 in sx and a1 in sx and
                    d1 in sx and g4 in sx
                    ):
                    if a1 == "*":
                        a1 = "X"
                    elif g1 == "*":
                        g1 = "X"
                    elif g7 == "*":
                        g7 = "X"
                    else:
                        sat = 0
                        thebad = 3
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 3
                    cs = 0
                    return
            if strategy == 4:
                cs = 4
                global d1;global d2;global b2
                if (
                    d2 in sx and d1 in sx and d3 in sx and
                    b2 in sx and f2 in sx
                    ):
                    if d1 == "*":
                        d1 = "X"
                    elif b2 == "*":
                        b2 = "X"
                    elif d2 == "*":
                        d2 = "X"
                    else:
                        sat = 0
                        thebad = 4
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 4
                    cs = 0
                    return
            if strategy == 5:
                cs = 5
                global g4;global f2;global f4
                if (
                    g4 in sx and f4 in sx and e4 in sx and
                    f2 in sx and f6 in sx
                    ):
                    if f2 == "*":
                        f2 = "X"
                    elif g4 == "*":
                        g4 = "X"
                    elif f4 == "*":
                        f4 = "X"
                    else:
                        sat = 0
                        thebad = 5
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 5
                    cs = 0
                    return
            if strategy == 6:
                cs = 6
                global d7;global b6; global d6
                if (
                    d7 in sx and d6 in sx and d5 in sx and
                    b6 in sx and f6 in sx
                    ):
                    if d7 == "*":
                        d7 = "X"
                    elif b6 == "*":
                        b6 = "X"
                    elif d6 == "*":
                        d6 = "X"
                    else:
                        sat = 0
                        thebad = 6
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 6
                    cs = 0
                    return
            if strategy == 7:
                cs = 7
                global c4; global b2; global b4
                if (
                    a4 in sx and b4 in sx and c4 in sx and
                    b6 in sx and b2 in sx
                    ):
                    if b2 == "*":
                        b2 = "X"
                    elif c4 == "*":
                        c4 = "X"
                    elif b4 == "*":
                        b4 = "X"
                    else:
                        sat = 0
                        thebad = 7
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 7
                    cs = 0
                    return
            if strategy == 8: # CLEVER STRATEGY - NOT TESTED
                cs = 8
                global b2;global d2;global b4
                if (
                    b4 in sx and b2 in sx and d2 in sx and
                    b6 in sx and f2 in sx
                    ):
                    if d2 == "*":
                        d2 = "X"
                    elif b4 == "*":
                        b4 = "X"
                    elif b2 == "*":
                        b2 = "X"
                    else:
                        sat = 0
                        thebad = 8
                        cs = 0
                        return
                elif (
                    b4 in sx and d2 in sx and b2 in sx and
                    f2 == "O"
                    ):
                    if b6 == "*":
                        global b6
                        b6 = "X"
                    else:
                        sat = 0
                        thebad = 8
                        cs = 0
                        return
                elif (
                    b4 in sx and d2 in sx and b2 in sx and
                    b6 == "O"
                    ):
                    if f2 == "*":
                        global f2
                        f2 = "X"
                    else:
                        sat = 0
                        thebad = 8
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 8
                    cs = 0
                    return
            if strategy == 9:
                cs = 9
                global d2;global f2;global f4
                if (
                    f2 in sx and f4 in sx and d2 in sx and
                    b2 in sx and f6 in sx
                    ):
                    if d2 == "*":
                        d2 = "X"
                    elif f4 == "*":
                        f4 = "X"
                    elif f2 == "*":
                        f2 = "X"
                    else:
                        sat = 0
                        thebad = 9
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 9
                    cs = 0
                    return
            if strategy == 10:
                cs = 10
                global f6;global f4; global d6
                if (
                    f6 in sx and d6 in sx and f4 in sx and
                    b6 in sx and f2 in sx
                    ):
                    if d6 == "*":
                        d6 = "X"
                    elif f4 == "*":
                        f4 = "X"
                    elif f6 == "*":
                        f6 = "X"
                    else:
                        sat = 0
                        thebad = 10
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 10
                    cs = 0
                    return
            if strategy == 11:
                cs = 11
                global d6;global b6;global b4
                if (
                    d6 in sx and b6 in sx and b4 in sx and
                    b2 in sx and f6 in sx
                    ):
                    if d6 == "*":
                        d6 = "X"
                    elif b4 == "*":
                        b4 = "X"
                    elif b6 == "*":
                        b6 = "X"
                    else:
                        sat = 0
                        thebad = 11
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 11
                    cs = 0
                    return
            if strategy == 12:
                cs = 12
                global c4;global c3; global d3
                if (
                    c4 in sx and c3 in sx and d3 in sx and
                    e3 in sx and c5 in sx
                    ):
                    if c4 == "*":
                        c4 = "X"
                    elif d3 == "*":
                        d3 = "X"
                    elif c3 == "*":
                        c3 = "X"
                    else:
                        sat = 0
                        thebad = 12
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 12
                    cs = 0
                    return
            if strategy == 13:
                cs = 13
                global e4;global e3;global d3
                if (
                    e4 in sx and e3 in sx and d3 in sx and
                    c3 in sx and e5 in sx
                    ):
                    if d3 == "*":
                        d3 = "X"
                    elif e4 == "*":
                        e4 = "X"
                    elif e3 == "*":
                        e3 = "X"
                    else:
                        sat = 0
                        thebad = 13
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 13
                    cs = 0
                    return
            if strategy == 14:
                cs = 14
                global e4;global e5;global d5
                if (
                    e5 in sx and e4 in sx and d5 in sx and
                    c5 in sx and e3 in sx
                    ):
                    if e4 == "*":
                        e4 = "X"
                    elif d5 == "*":
                        d5 = "X"
                    elif e5 == "*":
                        e5 = "X"
                    else:
                        sat = 0
                        thebad = 14
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 14
                    cs = 0
                    return
            if strategy == 15:
                cs = 15
                global c5;global c4;global d5
                if (
                    d5 in sx and c5 in sx and c4 in sx and
                    c3 in sx and e5 in sx
                    ):
                    if d5 == "*":
                        d5 = "X"
                    elif c4 == "*":
                        c4 = "X"
                    elif c5 == "*":
                        c5 = "X"
                    else:
                        sat = 0
                        thebad = 15
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 15
                    cs = 0
                    return
            if strategy == 16: # ULTIMATE STRATEGY
                cs = 16
                global a1;global g1;global g7;global a7
                if (
                    a1 == "*" and g7 == "*" and g1 == "*" or
                    a1 == "*" and g7 == "*" and a7 == "*"
                    ):
                    if a1 == "*":
                        a1 = "X"
                    elif g7 == "*":
                        g7 = "X"
                    else:
                        sat = 0
                        thebad = 16
                        cs = 0
                        return
                elif (
                    a1 == "X" and g7 == "X" and g1 == "*" and
                    a7 == "O" and d1 != "O" and g4 != "O"
                    ):
                    g1 = "X"
                elif (
                    a1 == "X" and g7 == "X" and g1 == "O" and
                    a7 == "*" and a4 != "O" and d7 != "O"
                    ):
                    a7 = "X"
                else:
                    sat = 0
                    thebad = 16
                    cs = 0
                    return
            if strategy == 17: # ULTIMATE STRATEGY
                cs = 17
                global g1;global a7;global a1;global g7
                if (
                    g1 == "*" and a7 == "*" and g7 == "*" or
                    g1 == "*" and a7 == "*" and a1 == "*"
                    ):
                    if g1 == "*":
                        g1 = "X"
                    elif a7 == "*":
                        a7 = "X"
                    else:
                        sat = 0
                        thebad = 17
                        cs = 0
                        return
                elif (
                    g1 == "X" and a7 == "X" and a1 == "*" and
                    g7 == "O" and d1 != "O" and a4 != "O"
                    ):
                    a1 = "X"
                elif (
                    g1 == "X" and a7 == "X" and a1 == "O" and
                    g7 == "*" and g4 != "O" and d7 != "O"
                    ):
                    g7 = "X"
                else:
                    sat = 0
                    thebad = 17
                    cs = 0
                    return
            if strategy == 18: # DEADLY ONE
                cs = 18
                global a7;global d1;global a1
                if (
                    a7 in sx and d1 in sx and g1 in sx and
                    a1 in sx and a4 in sx
                    ):
                    if a7 == "*":
                        a7 = "X"
                    elif d1 == "*":
                        d1 = "X"
                    elif a1 == "*":
                        a1 = "X"
                    else:
                        sat = 0
                        thebad = 18
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 18
                    cs = 0
                    return
            if strategy == 19:
                cs = 19
                global g4;global a1;global g1
                if (
                    g4 in sx and a1 in sx and g1 in sx and
                    d1 in sx and g7 in sx
                    ):
                    if g4 == "*":
                        g4 = "X"
                    elif a1 == "*":
                        a1 = "X"
                    elif g1 == "*":
                        g1 = "X"
                    else:
                        sat = 0
                        thebad = 19
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 19
                    cs = 0
                    return
            if strategy == 20:
                cs = 20
                global g7;global d1;global g1
                if (
                    g7 in sx and d1 in sx and g1 in sx and
                    g4 in sx and a1 in sx
                    ):
                    if g7 == "*":
                        g7 = "X"
                    elif d1 == "*":
                        d1 = "X"
                    elif g1 == "*":
                        g1 = "X"
                    else:
                        sat = 0
                        thebad = 20
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 20
                    cs = 0
                    return
            if strategy == 21:
                cs = 21
                global g4;global a7;global g7
                if (
                    g4 in sx and g7 in sx and a7 in sx and
                    d7 in sx and g1 in sx
                    ):
                    if g4 == "*":
                        g4 = "X"
                    elif a7 == "*":
                        a7 = "X"
                    elif g7 == "*":
                        g7 = "X"
                    else:
                        sat = 0
                        thebad = 21
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 21
                    cs = 0
                    return
            if strategy == 22:
                cs = 22
                global b6,b2,d2
                if (
                    b6 in sx and b2 in sx and d2 in sx and
                    b4 in sx and f2 in sx
                    ):
                    if d2 == "*":
                        d2 = "X"
                    elif b6 == "*":
                        b6 = "X"
                    elif b2 == "*":
                        b2 = "X"
                    else:
                        sat = 0
                        thebad = 22
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 22
                    cs = 0
                    return
            if strategy == 23:
                cs = 23
                global b2,f2,f4
                if (
                    b2 in sx and f2 in sx and f4 in sx and
                    d2 in sx and f6 in sx
                    ):
                    if b2 == "*":
                        b2 = "X"
                    elif f4 == "*":
                        f4 = "X"
                    elif f2 == "*":
                        f2 = "X"
                    else:
                        sat = 0
                        thebad = 23
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 23
                    cs = 0
                    return
            if strategy == 24:
                cs = 24
                global d2,f2,f6
                if (
                    d2 in sx and f2 in sx and f6 in sx and
                    f4 in sx and b2 in sx
                    ):
                    if d2 == "*":
                        d2 = "X"
                    elif f6 == "*":
                        f6 = "X"
                    elif f2 == "*":
                        f2 = "X"
                    else:
                        sat = 0
                        thebad = 24
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 24
                    cs = 0
                    return
            if strategy == 25: # DEADLY STRATEGY - NEW ONE
                cs = 25
                global b6;global f4;global f6
                if (
                    b6 in sx and f4 in sx and f6 in sx and
                    d6 in sx and f2 in sx
                    ):
                    if b6 == "*":
                        b6 = "X"
                    elif f4 == "*":
                        f4 = "X"
                    elif f6 == "*":
                        f6 = "X"
                    else:
                        sat = 0
                        thebad = 25
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 25
                    cs = 0
                    return
            if strategy == 26:
                cs = 26
                global f6,b6,b4
                if (
                    f6 in sx and b6 in sx and b4 in sx and
                    d6 in sx and b2 in sx
                    ):
                    if f6 == "*":
                        f6 = "X"
                    elif b4 == "*":
                        b4 = "X"
                    elif b6 == "*":
                        b6 = "X"
                    else:
                        sat = 0
                        thebad = 26
                        cs = 0
                        return
                else:
                    sat = 0
                    thebad = 26
                    cs = 0
                    return
            if strategy == 999:
                cs = 0
                go = False
                while go != True:
                    choice = random.choice(locations)
                    exec("i = " + choice)
                    if i == "*":
                        exec("global " + choice + "; " + choice + " = 'X'")
                        clear() # shall look after this before release
                        go = True
                    else:
                        continue
            global sat
            if sat == 0:
                sat = 1
        if phase == "game":
            global bd
            global last
            # Checking mill closing opportunities
            for i in mill_closings:
                go2 = False
                i = i.split(',')
                movefrom = i[0].split('.')[0] # e.g. 'd2'
                moveto = i[0].split('.')[1] # e.g. 'd1'
                for y in i[1].split('.'):
                    exec("q = " + y)
                    if q == "X":
                        continue
                    else:
                        go2 = 2
                        break
                if go2 == 2:
                    continue
                exec("a = " + movefrom)
                exec("b = " + moveto)
                if (
                    a == "X" and b == "*"
                    ):
                    exec("global " + movefrom + "; " + movefrom + " = '*'")
                    exec("global " + moveto + "; " + moveto + " = 'X'")
                    last = movefrom + "," + moveto
                    return
            if strategy == 1:
                #b2,d2,f2
                cs = 1
                if b2 in sx and d2 in sx and f2 in sx:
                    last = 0
                    if d1 == "X" and d2 == "*":
                        bd = False
                        try:
                            amove("d1","d2","opponent")
                            last = "d1,d2"
                        except ValueError:
                            bd = True
                    if b4 == "X" and b2 == "*" and bd == True:
                        bd = False
                        try:
                            amove("b4","b2","opponent")
                            last = "b4,b2"
                        except ValueError:
                            bd = True
                    if f4 == "X" and f2 == "*" and bd == True:
                        bd = False
                        try:
                            amove("f4","f2","opponent")
                            last = "f4,f2"
                        except ValueError:
                            bd = True
                    if g1 == "X" and d1 == "*" and bd == True:
                        bd = False
                        try:
                            amove("g1","d1","opponent")
                            last = "g1,d1"
                        except ValueError:
                            bd = True
                    if a1 == "X" and d1 == "*" and bd == True:
                        bd = False
                        try:
                            amove("a1","d1","opponent")
                            last = "a1,d1"
                        except ValueError:
                            bd = True
                    if d3 == "X" and d2 == "*" and bd == True:
                        bd = False
                        try:
                            amove("d3","d2","opponent")
                            last = "d3,d2"
                        except ValueError:
                            sat = 0
                            cs = 0
                            thebad = 1
                            return
                    if last == 0:
                        sat = 0
                        cs = 0
                        thebad = 1
                        return
                else:
                    sat = 0
                    cs = 0
                    thebad = 1
                    return
            if strategy == 999:
                breaker = False
                cs = 1
                sat = 1
                strats = []
                for i in locations:
                    if breaker == True:
                        break
                    exec("d = " + i)
                    if d == "X":
                        select3d = i
                        for i in locations:
                            if select3d + "," + i in validmovements or i + "," + select3d in validmovements:
                                #print select3d + "," + i # for debug purposes ---> slow down process also bc of print
                                exec("a = " + select3d)
                                exec("b = " + i)
                                if a == "X" and b == "*":
                                    #print "X and b is good!"
                                    strats.append("%s,%s" % (select3d, i))
                                    """
                                    now = select3d + "," + i
                                    global last
                                    if last != now and last2 != now:
                                        last = select3d + "," + i
                                        last2 = i + "," + select3d
                                        breaker = True;break
                                    else:
                                        continue
                                    """
                                else:
                                    continue
                try:
                    omove = random.choice(strats)
                except IndexError:
                    breaker = False
                    cs = 1
                    sat = 1
                    strats = []
                    for i in locations:
                        if breaker == True:
                            break
                        exec("d = " + i)
                        if d == "X":
                            select3d = i
                            for i in locations:
                                if select3d + "," + i in validmovements or i + "," + select3d in validmovements:
                                    exec("a = " + select3d)
                                    exec("b = " + i)
                                    if a == "X" and b == "*":
                                        strats.append("%s,%s" % (select3d, i))
                    try:
                        omove = random.choice(strats)
                    except IndexError:
                        global phase
                        phase = "pwin"
                        return
                somove = omove.split(',')
                movef = somove[0] # select3d
                movet = somove[1] # i
                exec("global " + movef + "; " + movef + " = '*'")
                exec("global " + movet + "; " + movet + " = 'X'")
                global last
                last = movef + "," + movet
                #raw_input() # for debug purposes
        if phase == "ofly" or phase == "bfly":
            # checking possible mills
            for i in possible_mills:
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill(a,b,c,"opp"):
                    if (
                        a == "*" or b == "*" or c == "*"
                        ):
                        for y in locations:
                            exec("q = " + y)
                            if (
                                q == "X" and
                                y not in [i[0],i[1],i[2]]
                                ):
                                movefrom = y
                                break
                        if a == "*":
                            moveto = i[0]
                        elif b == "*":
                            moveto = i[1]
                        elif c == "*":
                            moveto = i[2]
                        else:
                            print "Unexpected error."
                            print "Code x991"
                            raw_input()
                            break
                        exec("global " + movefrom + " ;" + movefrom + " = '*'")
                        exec("global " + moveto + " ;" + moveto + " = 'X'")
                        last = "%s,%s" % (movefrom,moveto)
                        return
            # checking player's mills
            """
            for i in possible_mills:
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill(a,b,c,"player"):
                    if (
                        a == "*" or b == "*" or c == "*"
                        ):
                        for y in locations:
                            exec("q = " + y)
                            if q == "X":
                                movefrom = y
                                break
                        if a == "*":
                            moveto = i[0]
                        elif b == "*":
                            moveto = i[1]
                        elif c == "*":
                            moveto = i[2]
                        else:
                            print "Unexpected error."
                            print "Code x992"
                            raw_input()
                            break
                        exec("global " + movefrom + " ;" + movefrom + " = '*'")
                        exec("global " + moveto + " ;" + moveto + " = 'X'")
                        last = "%s,%s" % (movefrom,moveto)
                        return
            """
            # # MODERN CHECKING OF POSSIBLE MILLS
            # # # Idea for that:
            # # # dontmove list , dontmove = []
            # # # add to the list and remove them everytime, etc...
            # Handling don't moves
            for i in mill_closings: # e.g.: "d2.d1,a1.g1"
                i = i.split(',') # ['d2.d1','a1.g1']
                z = i[1].split('.') # ['a1','g1']
                p = i[0].split('.') # ['d2','d1']
                exec("a = " + p[0]) # 'd2'
                exec("b = " + p[1]) # 'd1'
                exec("c = " + z[0]) # 'a1'
                exec("d = " + z[1]) # 'g1'
                print pmill(a,b,c,"player")
                print p[1]
                print p[1] in dontmove
                if (
                    pmill(a,b,c,"player") == False and
                    p[1] in dontmove
                    ):
                    print "removing " + p[1]
                    dontmove.remove(p[1])
                    raw_input()
                """ # JUST A THOUGHT.
                if (
                    c == "O" and d == "O" and
                    a == "O" and b == "X" and
                    p[1] not in dontmove
                    ):
                    dontmove.append(p[1])
                """
            raw_input()
            movefrom = 0
            for i in mill_closings: # e.g.: "d2.d1,a1.g1"
                i = i.split(',') # ['d2.d1','a1.g1']
                z = i[1].split('.') # ['a1','g1']
                exec("q = " + z[0]) # 'a1'
                exec("y = " + z[1]) # 'g1'
                if q == "O" and y == "O": # a1 == "O" and g1 == "O"
                    p = i[0].split('.') # ['d2','d1']
                    exec("q = " + p[0]) # 'd2'
                    exec("y = " + p[1]) # 'd1'
                    if q == "O" and y == "*": # d2 is 'O' d1 is '*'
                        moveto = p[1] # 'd1'
                        dontmove.append(moveto) # don't move d1
                        for y in locations:
                            exec("q = " + y)
                            if (
                                q == "X" and y not in dontmove
                                ):
                                movefrom = y
                                break
                        if movefrom == 0:
                            for y in locations:
                                exec("q = " + y)
                                if (
                                    q == "X"
                                    ):
                                    movefrom = y
                                    break
                        exec("global " + movefrom + " ;" + movefrom + " = '*'")
                        exec("global " + moveto + " ;" + moveto + " = 'X'")
                        last = "%s,%s" % (movefrom,moveto)
                        return
            if strategy == 999:
                strats = []
                for i in locations:
                    #print i # debug
                    exec("a = " + i)
                    if a == "X":
                        #print a # debug
                        exec(a + " = '*'")
                        for o in locations:
                            #print o # debug
                            exec("b = " + o)
                            if b == "*":
                                #print i + o + " TRUE" # debug
                                strats.append("%s,%s" % (i,o))
                            else:
                                continue
                tmove = random.choice(strats)
                ttmove = tmove.split(',')
                movef = ttmove[0]
                movet = ttmove[1]
                #print "SETTING TODAY!!" # debug
                exec("global " + movef + ";" + movef + " = '*'")
                exec("global " + movet + ";" + movet + " = 'X'")
                global last; last = movef + "," + movet
                #raw_input() # for debug purposes
    def amove(mfrom,mto,side):
        if mfrom + "," + mto in validmovements or mto + "," + mfrom in validmovements:
            exec("c = " + mfrom)
            exec("d = " + mto)
            if side.lower() == "opponent":
                #raw_input() # for debug purposes
                if c == "X" and d == "*":
                    exec("global " + mfrom + "; " + mfrom + " = '*'")
                    exec("global " + mto + "; " + mto + " = 'X'")
            elif side.lower() == "player":
                if c == "O" and d == "*":
                    exec(mfrom + " = '*'")
                    exec(mto + " = 'O'")
            else:
                raise ValueError()
        else:
            raise ValueError()
# INIT
sysname = platform.system()
# # BASIC INIT

if True:
    mi4 = False
    m1=m2=m3=m4=m5=m6=m7=m8=m9=m10=m11=m12=m13=m14=m15=m16=0
    m21=m22=m23=m24=m25=m26=m27=m28=m29=m210=m211=m212=m213=m214=m215=m216=0
    locations = ["a7","d7","g7","b6","d6","f6","c5","d5","e5","a4","b4","c4","e4","f4","g4","c3","d3","e3","b2","d2","f2","a1","d1","g1"]
    validmovements = ["a7,d7","a7,a4",
                      "d7,g7","a4,a1",
                      "b6,d6","b6,b4",
                      "d6,f6","b4,b2",
                      "c5,d5","c5,c4",
                      "d5,e5","c4,c3",
                      "a4,b4","d7,d6",
                      "b4,c4","d6,d5",
                      "e4,f4","d3,d2",
                      "f4,g4","d2,d1",
                      "c3,d3","e5,e4",
                      "d3,e3","e4,e3",
                      "b2,d2","f6,f4",
                      "d2,f2","f4,f2",
                      "a1,d1","g7,g4",
                      "d1,g1","g4,g1"]
    possible_mills = ["a1,d1,g1",
                      "b2,d2,f2",
                      "c3,d3,e3",
                      "a4,b4,c4",
                      "e4,f4,g4",
                      "c5,d5,e5",
                      "b6,d6,f6",
                      "a7,d7,g7",
                      "a1,a4,a7",
                      "b2,b4,b6",
                      "c3,c4,c5",
                      "d1,d2,d3",
                      "d5,d6,d7",
                      "e3,e4,e5",
                      "f2,f4,f6",
                      "g1,g4,g7"]
    mill_closings = [
                    # LAYOUT
                    # {from}.{to},{need to be 'X'}.{need to be 'X'}
                    # # HORIZONTAL  VERTICAL
                    "d2.d1,a1.g1","b4.a4,a1.a7",           # X*X start
                    "d1.d2,f2.b2","a4.b4,b2.b6",
                    "d3.d2,f2.b2","c4.b4,b2.b6",
                    "d2.d3,c3.e3","b4.c4,c3.c5",
                    "b2.b4,a4.c4","b6.d6,d5.d7",
                    "b6.b4,a4.c4","f6.d6,d5.d7",
                    "f2.f4,e4.g4","b2.d2,d1.d3",
                    "f6.f4,e4.g4","f2.d2,d1.d3",
                    "d6.d5,c5.e5","f4.e4,e3.e5",
                    "d5.d6,b6.f6","e4.f4,f2.f6",
                    "d7.d6,b6.f6","g4.f4,f2.f6",
                    "d6.d7,a7.g7","f4.g4,g1.g7",           # X*X end
                    "a4.a1,d1.g1","d7.a7,a1.a4",           # *XX + XX* start
                    "g4.g1,d1.a1","d1.a1,a4.a7",
                    "b4.b2,d2.f2","d2.b2,b4.b6",
                    "f4.f2,d2.b2","d6.b6,b2.b4",
                    "e4.e3,d3.c3","d3.c3,c4.c5",
                    "c4.c3,d3.e3","d5.c5,c3.c4",
                    "a1.a4,b4.c4","a1.d1,d2.d3",
                    "a7.a4,b4.c4","g1.d1,d2.d3",
                    "c3.c4,b4.a4","c3.d3,d1.d2",
                    "c5.c4,b4.a4","e3.d3,d1.d2",
                    "e3.e4,f4.g4","a7.d7,d5.d6",
                    "e5.e4,f4.g4","g7.d7,d5.d6",
                    "g1.g4,f4.e4","c5.d5,d6.d7",
                    "g7.g4,f4.e4","e5.d5,d6.d7",
                    "c4.c5,d5.e5","d5.e5,e3.e4",
                    "e4.e5,d5.c5","d3.e3,e4.e5",
                    "b4.b6,d6.f6","d2.f2,f4.f6",
                    "f4.f6,d6.b6","d6.f6,f4.f2",
                    "a4.a7,d7.g7","d1.g1,g4.g7",
                    "g4.g7,d7.a7","d7.g7,g4.g1",
                    # 64 possible closings. Nice...
                    ]
# BOARD
while phase == "placement":
    inmill = list(set(inmill))
    inmillP = list(set(inmillP))
    clear()
    if pcslft <= 0 and opcslft == 0:
        #rest = "nopcs" # IDK why it's here... possibly necessary
        phase = "game"
        cs = 0
        break
    print "                                      a    b    c    d    e    f    g"
    print "                                 7    %s--------------%s--------------%s    7" % (a7, d7, g7) # 7
    print "                                      |              |              |"
    print "                                 6    |    %s---------%s---------%s    |    6" % (b6, d6, f6)  # 6
    print "                                      |    |         |         |    |"
    print "                                 5    |    |    %s----%s----%s    |    |    5" % (c5, d5, e5)  # 5
    print "                                      |    |    |         |    |    |"
    print "                                 4    %s----%s----%s         %s----%s----%s    4" % (a4, b4, c4, e4, f4, g4)  # 4
    print "                                      |    |    |         |    |    |"
    print "                                 3    |    |    %s----%s----%s    |    |    3"  % (c3, d3, e3) # 3
    print "                                      |    |         |         |    |"
    print "                                 2    |    %s---------%s---------%s    |    2" % (b2, d2, f2) # 2
    print "                                      |              |              |"
    print "                                 1    %s--------------%s--------------%s    1" % (a1, d1, g1)  # 1
    print "                                      a    b    c    d    e    f    g"
    print "Current phase: Placement\n"
    if True:
        if rest == True:
            print "Please enter the location of your current piece."
        elif rest == "ERROR VAR":
            print "Incorrect location! You have entered: %s" % put
        else:
            if (
                rest != "ERROR EXST" and rest != "MILL" and 
                rest != "OMILL" and rest != "ERROR NB" and 
                rest != "nopcs" and rest != "ERROR INMILL"
                ):
                print "A problem occured. Error code: x843 , please report it immediately!"
        if rest == "ERROR EXST":
            print "You've tried to place your piece to a captured position! This is incorrect!"
        if rest == "MILL":
            print "You have formed a mill!"
            print "Enter one of your opponent's pieces location to remove it!"
        elif rest == "OMILL":
            print "Your opponent have formed a mill and removed %r" % rmvd
        if rest == "ERROR NB":
            rest = "MILL"
            print "The selected piece is neither your opponent's nor empty. Select another one."
        if rest == "nopcs":
            print "Sorry, but you don't have any pieces left."
        if rest == "ERROR INMILL":
            rest = "MILL"
            print "The piece that you are trying to remove is in mill."
            print "If the problem still occurs, please learn the rules of this game."
            print "Thereafter, if the problem still occurs, contact Us."
    print "Yours pieces left: %d" % pcslft
    print "Opponent's pieces left: %d" % opcslft
    print "Opponent's level: %s" % ailvl
    if debug == True:
        print "Player InMill: %r    Opponent InMill: %r" % (inmillP,inmill)
        print "Result: %r       Put: %r" % (rest,put) # debug only
        print "'strategy' variable: %r      'cs' - current strategy: %r" % (strategy,cs) # debug only
    # PLAYER TURN
    put = raw_input(">> ")
    if put not in locations:
        rest = "ERROR VAR"
        continue
    else:
        if rest != "MILL" and rest != "ERROR INMILL":
            rest = True
        else:
            if put in inmill:
                rest = "ERROR INMILL"
                continue
            try:
                exec("i = " + put)
            except:
                continue
            if i == "X":
                opcs-=1
                try:
                    exec(put + " = '*'")
                except:
                    rest = "ERROR VAR"
            else:
                rest = "ERROR NB"
    if rest != "MILL" and rest != "ERROR NB" and rest != "ERROR INMILL":
        try:
            exec("i = " + put)
        except:
            continue
        if i == "*":
            try:
                exec(put + " = 'O'")
            except:
                rest = "ERROR VAR"
        elif rest != "ERROR VAR":
            rest = "ERROR EXST"
    if rest == True:
        pcslft-=1
    if rest == "MILL":
        rest = True
    # MILLS
    if a7 == "O" and d7 == "O" and g7 == "O":
        if all(x in inmillP for x in ['a7', 'd7', 'g7']) == False:
            inmillP.extend(["a7","d7","g7"])
        if m1 != True:
            m1 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'd7', 'g7']):
        inmillP.remove("a7")
        inmillP.remove("d7")
        inmillP.remove("g7")
    if b6 == "O" and d6 == "O" and f6 == "O":
        if all(x in inmillP for x in ['b6', 'd6', 'f6']) == False:
            inmillP.extend(["b6","d6","f6"])
        if m2 != True and rest != "MILL":
            m2 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b6', 'd6', 'f6']):
        inmillP.remove("b6")
        inmillP.remove("d6")
        inmillP.remove("f6")
    if c5 == "O" and d5 == "O" and e5 == "O":
        if all(x in inmillP for x in ['c5', 'd5', 'e5']) == False:
            inmillP.extend(["c5","d5","e5"])
        if m3 != True and rest != "MILL":
            m3 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c5', 'd5', 'e5']):
        inmillP.remove("c5")
        inmillP.remove("d5")
        inmillP.remove("e5")
    if a4 == "O" and b4 == "O" and c4 == "O":
        if all(x in inmillP for x in ['a4', 'b4', 'c4']) == False:
            inmillP.extend(["a4","b4","c4"])
        if m4 != True and rest != "MILL":
            m4 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a4', 'b4', 'c4']):
        inmillP.remove("a4")
        inmillP.remove("b4")
        inmillP.remove("c4")
    if e4 == "O" and f4 == "O" and g4 == "O":
        if all(x in inmillP for x in ['e4', 'f4', 'g4']) == False:
            inmillP.extend(["e4","f4","g4"])
        if m5 != True and rest != "MILL":
            m5 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e4', 'f4', 'g4']):
        inmillP.remove("e4")
        inmillP.remove("f4")
        inmillP.remove("g4")
    if c3 == "O" and d3 == "O" and e3 == "O":
        if all(x in inmillP for x in ['c3', 'd3', 'e3']) == False:
            inmillP.extend(["c3","d3","e3"])
        if m6 != True and rest != "MILL":
            m6 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'd3', 'e3']):
        inmillP.remove("c3")
        inmillP.remove("d3")
        inmillP.remove("e3")
    if b2 == "O" and d2 == "O" and f2 == "O":
        if all(x in inmillP for x in ['b2', 'd2', 'f2']) == False:
            inmillP.extend(["b2","d2","f2"])
        if m7 != True and rest != "MILL":
            m7 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'd2', 'f2']):
        inmillP.remove("b2")
        inmillP.remove("d2")
        inmillP.remove("f2")
    if a1 == "O" and d1 == "O" and g1 == "O":
        if all(x in inmillP for x in ['a1', 'd1', 'g1']) == False:
            inmillP.extend(["a1","d1","g1"])
        if m8 != True and rest != "MILL":
            m8 = True
            mi4 = True # for strategy
            rest = "MILL"
    elif all(x in inmillP for x in ['a1', 'd1', 'g1']):
        inmillP.remove("a1")
        inmillP.remove("d1")
        inmillP.remove("g1")
    # VERTICALS
    if a7 == "O" and a4 == "O" and a1 == "O":
        if all(x in inmillP for x in ['a7', 'a4', 'a1']) == False:
            inmillP.extend(["a7","a4","a1"])
        if m9 != True and rest != "MILL":
            m9 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'a4', 'a1']):
        inmillP.remove("a7")
        inmillP.remove("a4")
        inmillP.remove("a1")
    if b2 == "O" and b4 == "O" and b6 == "O":
        if all(x in inmillP for x in ['b2', 'b4', 'b6']) == False:
            inmillP.extend(["b2","b4","b6"])
        if m10 != True and rest != "MILL":
            m10 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'b4', 'b6']):
        inmillP.remove("b2")
        inmillP.remove("b4")
        inmillP.remove("b6")
    if c3 == "O" and c4 == "O" and c5 == "O":
        if all(x in inmillP for x in ['c3', 'c4', 'c5']) == False:
            inmillP.extend(["c3","c4","c5"])
        if m11 != True and rest != "MILL":
            m11 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'c4', 'c5']):
        inmillP.remove("c3")
        inmillP.remove("c4")
        inmillP.remove("c5")
    if d1 == "O" and d2 == "O" and d3 == "O":
        if all(x in inmillP for x in ['d1', 'd2', 'd3']) == False:
            inmillP.extend(["d1","d2","d3"])
        if m12 != True and rest != "MILL":
            m12 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d1', 'd2', 'd3']):
        inmillP.remove("d1")
        inmillP.remove("d2")
        inmillP.remove("d3")
    if d7 == "O" and d6 == "O" and d5 == "O":
        if all(x in inmillP for x in ['d7', 'd6', 'd5']) == False:
            inmillP.extend(["d7","d6","d5"])
        if m13 != True and rest != "MILL":
            m13 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d7', 'd6', 'd5']):
        inmillP.remove("d7")
        inmillP.remove("d6")
        inmillP.remove("d5")
    if e5 == "O" and e4 == "O" and e3 == "O":
        if all(x in inmillP for x in ['e5', 'e4', 'e3']) == False:
            inmillP.extend(["e5","e4","e3"])
        if m14 != True and rest != "MILL":
            m14 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e5', 'e4', 'e3']):
        inmillP.remove("e5")
        inmillP.remove("e4")
        inmillP.remove("e3")
    if f2 == "O" and f4 == "O" and f6 == "O":
        if all(x in inmillP for x in ['f2', 'f4', 'f6']) == False:
            inmillP.extend(["f2","f4","f6"])
        if m15 != True and rest != "MILL":
            m15 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['f2', 'f4', 'f6']):
        inmillP.remove("f2")
        inmillP.remove("f4")
        inmillP.remove("f6")
    if g1 == "O" and g4 == "O" and g7 == "O":
        if all(x in inmillP for x in ['g1', 'g4', 'g7']) == False:
            inmillP.extend(["g1","g4","g7"])
        if m16 != True and rest != "MILL":
            m16 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['g1', 'g4', 'g7']):
        inmillP.remove("g1")
        inmillP.remove("g4")
        inmillP.remove("g7")
    """
    if a7 == "O" and d7 == "O" and g7 == "O" and m1 != True:
        m1 = True
        rest = "MILL"
    elif b6 == "O" and d6 == "O" and f6 == "O" and m2 != True:
        m2 = True
        rest = "MILL"
    elif c5 == "O" and d5 == "O" and e5 == "O" and m3 != True:
        m3 = True
        rest = "MILL"
    elif a4 == "O" and b4 == "O" and c4 == "O" and m4 != True:
        m4 = True
        rest = "MILL"
    elif e4 == "O" and f4 == "O" and g4 == "O" and m5 != True:
        m5 = True
        rest = "MILL"
    elif c3 == "O" and d3 == "O" and e3 == "O" and m6 != True:
        m6 = True
        rest = "MILL"
    elif b2 == "O" and d2 == "O" and f2 == "O" and m7 != True:
        m7 = True
        rest = "MILL"
    elif a1 == "O" and d1 == "O" and g1 == "O" and m8 != True:
        m8 = True
        rest = "MILL"
    # VERTICALS
    elif a7 == "O" and a4 == "O" and a1 == "O" and m9 != True:
        m9 = True
        rest = "MILL"
    elif b2 == "O" and b4 == "O" and b6 == "O" and m10 != True:
        m10 = True
        rest = "MILL"
    elif c3 == "O" and c4 == "O" and c5 == "O" and m11 != True:
        m11 = True
        rest = "MILL"
    elif d1 == "O" and d2 == "O" and d3 == "O" and m12 != True:
        m12 = True
        rest = "MILL"
    elif d7 == "O" and d6 == "O" and d5 == "O" and m13 != True:
        m13 = True
        rest = "MILL"
    elif e5 == "O" and e4 == "O" and e3 == "O" and m14 != True:
        m14 = True
        rest = "MILL"
    elif f2 == "O" and f4 == "O" and f6 == "O" and m15 != True:
        m15 = True
        rest = "MILL"
    elif g1 == "O" and g4 == "O" and g7 == "O" and m16 != True:
        m16 = True
        rest = "MILL"
    """
    if rest != "ERROR VAR" and rest != "ERROR EXST" and rest != "OMILL" and rest != "MILL" and rest != "ERROR NB":
        if opcslft == 0:
            continue
        # OPPONENT TURN
        # STRATEGY CHOOSING
        sx = ("*","X")
        if strategy == 999:
            choose_strategy(0)
        # STRATEGY USING
        qr = 0
        sat = 0
        while sat != 1:
            qr+=1
            # # # E M E R G E N C Y # # #
            #  Shall remove at release  #
            if qr == 15:
                strategy = 999
                use_strategy()
                break
            #  Shall remove at release  #
            # # # E M E R G E N C Y # # #
            if sat == 0:
                choose_strategy(thebad)
            use_strategy()
                #raw_input() # for debugging of 'checking mill opportunities'
        # STRATEGY END
        opcslft-=1
        # OPPONENT MILLS
        if a7 == "X" and d7 == "X" and g7 == "X":
            if all(x in inmill for x in ['a7', 'd7', 'g7']) == False:
                inmill.extend(["a7","d7","g7"])
            if m21 != True:
                m21 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'd7', 'g7']):
            inmill.remove("a7")
            inmill.remove("d7")
            inmill.remove("g7")
        if b6 == "X" and d6 == "X" and f6 == "X":
            if all(x in inmill for x in ['b6', 'd6', 'f6']) == False:
                inmill.extend(["b6","d6","f6"])
            if m22 != True and rest != "OMILL":
                m22 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b6', 'd6', 'f6']):
            inmill.remove("b6")
            inmill.remove("d6")
            inmill.remove("f6")
        if c5 == "X" and d5 == "X" and e5 == "X":
            if all(x in inmill for x in ['c5', 'd5', 'e5']) == False:
                inmill.extend(["c5","d5","e5"])
            if m23 != True and rest != "OMILL":
                m23 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c5', 'd5', 'e5']):
            inmill.remove("c5")
            inmill.remove("d5")
            inmill.remove("e5")
        if a4 == "X" and b4 == "X" and c4 == "X":
            if all(x in inmill for x in ['a4', 'b4', 'c4']) == False:
                inmill.extend(["a4","b4","c4"])
            if m24 != True and rest != "OMILL":
                m24 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a4', 'b4', 'c4']):
            inmill.remove("a4")
            inmill.remove("b4")
            inmill.remove("c4")
        if e4 == "X" and f4 == "X" and g4 == "X":
            if all(x in inmill for x in ['e4', 'f4', 'g4']) == False:
                inmill.extend(["e4","f4","g4"])
            if m25 != True and rest != "OMILL":
                m25 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e4', 'f4', 'g4']):
            inmill.remove("e4")
            inmill.remove("f4")
            inmill.remove("g4")
        if c3 == "X" and d3 == "X" and e3 == "X":
            if all(x in inmill for x in ['c3', 'd3', 'e3']) == False:
                inmill.extend(["c3","d3","e3"])
            if m26 != True and rest != "OMILL":
                m26 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'd3', 'e3']):
            inmill.remove("c3")
            inmill.remove("d3")
            inmill.remove("e3")
        if b2 == "X" and d2 == "X" and f2 == "X":
            if all(x in inmill for x in ['b2', 'd2', 'f2']) == False:
                inmill.extend(["b2","d2","f2"])
            if m27 != True and rest != "OMILL":
                m27 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'd2', 'f2']):
            inmill.remove("b2")
            inmill.remove("d2")
            inmill.remove("f2")
        if a1 == "X" and d1 == "X" and g1 == "X":
            if all(x in inmill for x in ['a1', 'd1', 'g1']) == False:
                inmill.extend(["a1","d1","g1"])
            if m28 != True and rest != "OMILL":
                m28 = True
                mi4 = True # for strategy
                rest = "OMILL"
        elif all(x in inmill for x in ['a1', 'd1', 'g1']):
            inmill.remove("a1")
            inmill.remove("d1")
            inmill.remove("g1")
        # VERTICALS
        if a7 == "X" and a4 == "X" and a1 == "X":
            if all(x in inmill for x in ['a7', 'a4', 'a1']) == False:
                inmill.extend(["a7","a4","a1"])
            if m29 != True and rest != "OMILL":
                m29 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'a4', 'a1']):
            inmill.remove("a7")
            inmill.remove("a4")
            inmill.remove("a1")
        if b2 == "X" and b4 == "X" and b6 == "X":
            if all(x in inmill for x in ['b2', 'b4', 'b6']) == False:
                inmill.extend(["b2","b4","b6"])
            if m210 != True and rest != "OMILL":
                m210 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'b4', 'b6']):
            inmill.remove("b2")
            inmill.remove("b4")
            inmill.remove("b6")
        if c3 == "X" and c4 == "X" and c5 == "X":
            if all(x in inmill for x in ['c3', 'c4', 'c5']) == False:
                inmill.extend(["c3","c4","c5"])
            if m211 != True and rest != "OMILL":
                m211 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'c4', 'c5']):
            inmill.remove("c3")
            inmill.remove("c4")
            inmill.remove("c5")
        if d1 == "X" and d2 == "X" and d3 == "X":
            if all(x in inmill for x in ['d1', 'd2', 'd3']) == False:
                inmill.extend(["d1","d2","d3"])
            if m212 != True and rest != "OMILL":
                m212 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d1', 'd2', 'd3']):
            inmill.remove("d1")
            inmill.remove("d2")
            inmill.remove("d3")
        if d7 == "X" and d6 == "X" and d5 == "X":
            if all(x in inmill for x in ['d7', 'd6', 'd5']) == False:
                inmill.extend(["d7","d6","d5"])
            if m213 != True and rest != "OMILL":
                m213 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d7', 'd6', 'd5']):
            inmill.remove("d7")
            inmill.remove("d6")
            inmill.remove("d5")
        if e5 == "X" and e4 == "X" and e3 == "X":
            if all(x in inmill for x in ['e5', 'e4', 'e3']) == False:
                inmill.extend(["e5","e4","e3"])
            if m214 != True and rest != "OMILL":
                m214 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e5', 'e4', 'e3']):
            inmill.remove("e5")
            inmill.remove("e4")
            inmill.remove("e3")
        if f2 == "X" and f4 == "X" and f6 == "X":
            if all(x in inmill for x in ['f2', 'f4', 'f6']) == False:
                inmill.extend(["f2","f4","f6"])
            if m215 != True and rest != "OMILL":
                m215 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['f2', 'f4', 'f6']):
            inmill.remove("f2")
            inmill.remove("f4")
            inmill.remove("f6")
        if g1 == "X" and g4 == "X" and g7 == "X":
            if all(x in inmill for x in ['g1', 'g4', 'g7']) == False:
                inmill.extend(["g1","g4","g7"])
            if m216 != True and rest != "OMILL":
                m216 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['g1', 'g4', 'g7']):
            inmill.remove("g1")
            inmill.remove("g4")
            inmill.remove("g7")
        if rest == "OMILL":
            pcs-=1
            go = False
            for i in possible_mills:
                if go == True:
                    break
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill(a,b,c,"player"):
                    for y in [i[0],i[1],i[2]]:
                        if go2 == True:
                            continue
                        exec("x = " + y)
                        if x == "O":
                            for q in [i[0],i[1],i[2]]:
                                exec("q = " + q)
                                if q == "X":
                                    go2 = True
                                    break
                            if y not in inmillP:
                                exec(y + " = '*'")
                                rmvd = y
                                go = True
                                break
                            else:
                                continue
                        else:
                            continue
            go2 = 0
            for i in possible_mills:
                if go == True:
                    break
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill2(a,b,c,"opp"):
                    for y in [i[0],i[1],i[2]]:
                        if go2 == True:
                            continue
                        exec("x = " + y)
                        if x == "O":
                            if y not in inmillP:
                                exec(y + " = '*'")
                                rmvd = y
                                go = True
                                break
                            else:
                                continue
                        else:
                            continue
            # random choosing
            while go != True:
                choice = random.choice(locations)
                while choice in inmillP:
                    choice = random.choice(locations)
                exec("i = " + choice)
                if i == "O":
                    exec(choice + " = '*'")
                    rmvd = choice
                    go = True
                else:
                    continue
while phase == "game":
    strategy = 999
    inmill = list(set(inmill))
    inmillP = list(set(inmillP))
    clear()
    if opcs == 3 and pcs == 3:
        phase = "bfly"
        break
    elif opcs == 3:
        phase = "ofly"
        break
    elif pcs == 3:
        rest = True
        phase = "fly"
        break
    print "                                      a    b    c    d    e    f    g"
    print "                                 7    %s--------------%s--------------%s    7" % (a7, d7, g7) # 7
    print "                                      |              |              |"
    print "                                 6    |    %s---------%s---------%s    |    6" % (b6, d6, f6)  # 6
    print "                                      |    |         |         |    |"
    print "                                 5    |    |    %s----%s----%s    |    |    5" % (c5, d5, e5)  # 5
    print "                                      |    |    |         |    |    |"
    print "                                 4    %s----%s----%s         %s----%s----%s    4" % (a4, b4, c4, e4, f4, g4)  # 4
    print "                                      |    |    |         |    |    |"
    print "                                 3    |    |    %s----%s----%s    |    |    3"  % (c3, d3, e3) # 3
    print "                                      |    |         |         |    |"
    print "                                 2    |    %s---------%s---------%s    |    2" % (b2, d2, f2) # 2
    print "                                      |              |              |"
    print "                                 1    %s--------------%s--------------%s    1" % (a1, d1, g1)  # 1
    print "                                      a    b    c    d    e    f    g"
    print "Current phase: Main-Game\n"
    if rest == True:
        print "Please move one of your pieces. E.g.: a1,d1 / g1,g4"
    if rest == "MILL":
        print "You have formed a mill!"
        print "Enter one of your opponent's pieces location to remove it!"
    elif rest == "OMILL":
        print "Your opponent have formed a mill and removed %r" % rmvd
    if rest == "MFNVA" and rest2 == "MTNVA":
        rest = True
        print "Neither %s nor %s is a valid location. Please try again." % (movef, movet)
    elif rest == "MFNVA":
        rest = True
        print "%s is not a valid location. Please try again." % movef
    elif rest2 == "MTNVA":
        rest2 = 0
        print "%s is not a valid location. Please try again" % movet
    if rest == "ERROR IE":
        print "You've entered %s. This is invalid." % movef
        print "Please enter a movement like the following: 'a1,d1' or 'g1,g4'"
    if rest == "ERROR BPL":
        print "You have entered an incorrect movement."
        print "You've tried to move from %s to %s" % (movef,movet)
        print "Please try again."
    if rest == "ERROR NVM":
        print "You have entered an incorrect movement."
        print "If you still experience this problem, please learn the rules."
        print "Please try again."
    if rest == "ERROR BS":
        rest = 'MILL'
        print "The entered location is not valid. Please try again."
    if rest == "ERROR INMILL":
        rest = 'MILL'
        print "The piece that you are trying to remove is in mill."
        print "If the problem still occurs, please learn the rules of this game."
        print "Thereafter, if the problem still occurs, contact Us."
    print "Your pieces: %d" % pcs
    print "Opponent's pieces: %d" % opcs
    print "Last movement: %s" % last
    print "Opponent's level: %s" % ailvl
    if debug == True:
        print "Player InMill: %r    Opponent InMill: %r" % (inmillP, inmill) # debug only
        print "Result: %r       Put: %r" % (rest,put) # debug only
        print "'strategy' var: %r       'cs' - current strategy: %r" % (strategy, cs) # debug only
    # PLAYER TURN
    move = raw_input(">> ")
    if rest == "MILL":
        if move not in locations:
            rest = "ERROR BS"
            continue
        exec("i = " + move)
        if move in inmill:
            rest = "ERROR INMILL"
            continue
        if i == "X":
            exec(move + " = '*'")
            opcs-=1
            rest = True
        else:
            rest = "ERROR BS"
            continue
    else:
        move = move.replace("'","")
        try:
            move = move.split(',')
            movef = move[0]
            movet = move[1]
        except IndexError:
            rest = "ERROR IE"
            continue
        if movef not in locations:
            rest = "MFNVA"
        if movet not in locations:
            rest2 = "MTNVA"
        if rest == "MFNVA":
            continue
        if movef + "," + movet in validmovements or movet + "," + movef in validmovements:
            exec("i = " + movef)
            exec("d = " + movet)
            if i == "O" and d == "*":
                exec(movef + " = '*'")
                exec(movet + " = 'O'")
                rest = True
            else:
                rest = "ERROR BPL"
                continue
        else:
            rest = "ERROR NVM"
            continue
 # MILLS
    if True: # notmill() tech
        if notmill(a7,d7,g7):
            m1 = False
        if notmill(b6,d6,f6):
            m2 = False
        if notmill(c5,d5,e5):
            m3 = False
        if notmill(a4,b4,c4):
            m4 = False
        if notmill(e4,f4,g4):
            m5 = False
        if notmill(c3,d3,e3):
            m6 = False
        if notmill(b2,d2,f2):
            m7 = False
        if notmill(a1,d1,g1):
            m8 = False
        if notmill(a7,a4,a1):
            m9 = False
        if notmill(b2,b4,b6):
            m10 = False
        if notmill(c3,c4,c5):
            m11 = False
        if notmill(d1,d2,d3):
            m12 = False
        if notmill(d7,d6,d5):
            m13 = False
        if notmill(e5,e4,e3):
            m14 = False
        if notmill(f2,f4,f6):
            m15 = False
        if notmill(g1,g4,g7):
            m16 = False
    if a7 == "O" and d7 == "O" and g7 == "O":
        if all(x in inmillP for x in ['a7', 'd7', 'g7']) == False:
            inmillP.extend(["a7","d7","g7"])
        if m1 != True:
            m1 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'd7', 'g7']):
        inmillP.remove("a7")
        inmillP.remove("d7")
        inmillP.remove("g7")
    if b6 == "O" and d6 == "O" and f6 == "O":
        if all(x in inmillP for x in ['b6', 'd6', 'f6']) == False:
            inmillP.extend(["b6","d6","f6"])
        if m2 != True and rest != "MILL":
            m2 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b6', 'd6', 'f6']):
        inmillP.remove("b6")
        inmillP.remove("d6")
        inmillP.remove("f6")
    if c5 == "O" and d5 == "O" and e5 == "O":
        if all(x in inmillP for x in ['c5', 'd5', 'e5']) == False:
            inmillP.extend(["c5","d5","e5"])
        if m3 != True and rest != "MILL":
            m3 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c5', 'd5', 'e5']):
        inmillP.remove("c5")
        inmillP.remove("d5")
        inmillP.remove("e5")
    if a4 == "O" and b4 == "O" and c4 == "O":
        if all(x in inmillP for x in ['a4', 'b4', 'c4']) == False:
            inmillP.extend(["a4","b4","c4"])
        if m4 != True and rest != "MILL":
            m4 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a4', 'b4', 'c4']):
        inmillP.remove("a4")
        inmillP.remove("b4")
        inmillP.remove("c4")
    if e4 == "O" and f4 == "O" and g4 == "O":
        if all(x in inmillP for x in ['e4', 'f4', 'g4']) == False:
            inmillP.extend(["e4","f4","g4"])
        if m5 != True and rest != "MILL":
            m5 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e4', 'f4', 'g4']):
        inmillP.remove("e4")
        inmillP.remove("f4")
        inmillP.remove("g4")
    if c3 == "O" and d3 == "O" and e3 == "O":
        if all(x in inmillP for x in ['c3', 'd3', 'e3']) == False:
            inmillP.extend(["c3","d3","e3"])
        if m6 != True and rest != "MILL":
            m6 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'd3', 'e3']):
        inmillP.remove("c3")
        inmillP.remove("d3")
        inmillP.remove("e3")
    if b2 == "O" and d2 == "O" and f2 == "O":
        if all(x in inmillP for x in ['b2', 'd2', 'f2']) == False:
            inmillP.extend(["b2","d2","f2"])
        if m7 != True and rest != "MILL":
            m7 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'd2', 'f2']):
        inmillP.remove("b2")
        inmillP.remove("d2")
        inmillP.remove("f2")
    if a1 == "O" and d1 == "O" and g1 == "O":
        if all(x in inmillP for x in ['a1', 'd1', 'g1']) == False:
            inmillP.extend(["a1","d1","g1"])
        if m8 != True and rest != "MILL":
            m8 = True
            mi4 = True # for strategy
            rest = "MILL"
    elif all(x in inmillP for x in ['a1', 'd1', 'g1']):
        inmillP.remove("a1")
        inmillP.remove("d1")
        inmillP.remove("g1")
    # VERTICALS
    if a7 == "O" and a4 == "O" and a1 == "O":
        if all(x in inmillP for x in ['a7', 'a4', 'a1']) == False:
            inmillP.extend(["a7","a4","a1"])
        if m9 != True and rest != "MILL":
            m9 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'a4', 'a1']):
        inmillP.remove("a7")
        inmillP.remove("a4")
        inmillP.remove("a1")
    if b2 == "O" and b4 == "O" and b6 == "O":
        if all(x in inmillP for x in ['b2', 'b4', 'b6']) == False:
            inmillP.extend(["b2","b4","b6"])
        if m10 != True and rest != "MILL":
            m10 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'b4', 'b6']):
        inmillP.remove("b2")
        inmillP.remove("b4")
        inmillP.remove("b6")
    if c3 == "O" and c4 == "O" and c5 == "O":
        if all(x in inmillP for x in ['c3', 'c4', 'c5']) == False:
            inmillP.extend(["c3","c4","c5"])
        if m11 != True and rest != "MILL":
            m11 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'c4', 'c5']):
        inmillP.remove("c3")
        inmillP.remove("c4")
        inmillP.remove("c5")
    if d1 == "O" and d2 == "O" and d3 == "O":
        if all(x in inmillP for x in ['d1', 'd2', 'd3']) == False:
            inmillP.extend(["d1","d2","d3"])
        if m12 != True and rest != "MILL":
            m12 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d1', 'd2', 'd3']):
        inmillP.remove("d1")
        inmillP.remove("d2")
        inmillP.remove("d3")
    if d7 == "O" and d6 == "O" and d5 == "O":
        if all(x in inmillP for x in ['d7', 'd6', 'd5']) == False:
            inmillP.extend(["d7","d6","d5"])
        if m13 != True and rest != "MILL":
            m13 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d7', 'd6', 'd5']):
        inmillP.remove("d7")
        inmillP.remove("d6")
        inmillP.remove("d5")
    if e5 == "O" and e4 == "O" and e3 == "O":
        if all(x in inmillP for x in ['e5', 'e4', 'e3']) == False:
            inmillP.extend(["e5","e4","e3"])
        if m14 != True and rest != "MILL":
            m14 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e5', 'e4', 'e3']):
        inmillP.remove("e5")
        inmillP.remove("e4")
        inmillP.remove("e3")
    if f2 == "O" and f4 == "O" and f6 == "O":
        if all(x in inmillP for x in ['f2', 'f4', 'f6']) == False:
            inmillP.extend(["f2","f4","f6"])
        if m15 != True and rest != "MILL":
            m15 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['f2', 'f4', 'f6']):
        inmillP.remove("f2")
        inmillP.remove("f4")
        inmillP.remove("f6")
    if g1 == "O" and g4 == "O" and g7 == "O":
        if all(x in inmillP for x in ['g1', 'g4', 'g7']) == False:
            inmillP.extend(["g1","g4","g7"])
        if m16 != True and rest != "MILL":
            m16 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['g1', 'g4', 'g7']):
        inmillP.remove("g1")
        inmillP.remove("g4")
        inmillP.remove("g7")
    """
    if a7 == "O" and d7 == "O" and g7 == "O" and m1 != True:
        m1 = True
        rest = "MILL"
    elif b6 == "O" and d6 == "O" and f6 == "O" and m2 != True:
        m2 = True
        rest = "MILL"
    elif c5 == "O" and d5 == "O" and e5 == "O" and m3 != True:
        m3 = True
        rest = "MILL"
    elif a4 == "O" and b4 == "O" and c4 == "O" and m4 != True:
        m4 = True
        rest = "MILL"
    elif e4 == "O" and f4 == "O" and g4 == "O" and m5 != True:
        m5 = True
        rest = "MILL"
    elif c3 == "O" and d3 == "O" and e3 == "O" and m6 != True:
        m6 = True
        rest = "MILL"
    elif b2 == "O" and d2 == "O" and f2 == "O" and m7 != True:
        m7 = True
        rest = "MILL"
    elif a1 == "O" and d1 == "O" and g1 == "O" and m8 != True:
        m8 = True
        rest = "MILL"
    # VERTICALS
    elif a7 == "O" and a4 == "O" and a1 == "O" and m9 != True:
        m9 = True
        rest = "MILL"
    elif b2 == "O" and b4 == "O" and b6 == "O" and m10 != True:
        m10 = True
        rest = "MILL"
    elif c3 == "O" and c4 == "O" and c5 == "O" and m11 != True:
        m11 = True
        rest = "MILL"
    elif d1 == "O" and d2 == "O" and d3 == "O" and m12 != True:
        m12 = True
        rest = "MILL"
    elif d7 == "O" and d6 == "O" and d5 == "O" and m13 != True:
        m13 = True
        rest = "MILL"
    elif e5 == "O" and e4 == "O" and e3 == "O" and m14 != True:
        m14 = True
        rest = "MILL"
    elif f2 == "O" and f4 == "O" and f6 == "O" and m15 != True:
        m15 = True
        rest = "MILL"
    elif g1 == "O" and g4 == "O" and g7 == "O" and m16 != True:
        m16 = True
        rest = "MILL"
    """
    # OPPONENT'S TURN
    if (
        rest != "MILL" and rest != "ERROR NVM" and
        rest != "ERROR BPL" and rest != "MFNVA" and 
        rest != "MTNVA" and rest != "ERROR BS" and
        rest != "ERROR IE" and rest != "ERROR INMILL" and 
        phase == "game"
        ):
        sx = ("*","X")
        sat = 0
        qr = 0
        if rest != "OMILL":
            while sat != 1:
                qr+=1
                # # # E M E R G E N C Y # # #
                #  Shall remove at release  #
                if qr == 15:
                    print "Entered emergency"
                    raw_input()
                    strategy = 999
                    use_strategy()
                    sat = 1
                    break
                #  Shall remove at release  #
                # # # E M E R G E N C Y # # #
                if sat == 0:
                    choose_strategy(thebad)
                use_strategy()
        # STRATEGY END
        """
        if a7 == "X" and d7 == "X" and g7 == "X" and m21 != True:
            m21 = True
            rest = "OMILL"
        elif b6 == "X" and d6 == "X" and f6 == "X" and m22 != True:
            m22 = True
            rest = "OMILL"
        elif c5 == "X" and d5 == "X" and e5 == "X" and m23 != True:
            m23 = True
            rest = "OMILL"
        elif a4 == "X" and b4 == "X" and c4 == "X" and m24 != True:
            m24 = True
            rest = "OMILL"
        elif e4 == "X" and f4 == "X" and g4 == "X" and m25 != True:
            m25 = True
            rest = "OMILL"
        elif c3 == "X" and d3 == "X" and e3 == "X" and m26 != True:
            m26 = True
            rest = "OMILL"
        elif b2 == "X" and d2 == "X" and f2 == "X" and m27 != True:
            m27 = True
            rest = "OMILL"
        elif a1 == "X" and d1 == "X" and g1 == "X" and m28 != True:
            m28 = True
            mi4 = True # for strategy
            rest = "OMILL"
        # VERTICALS
        elif a7 == "X" and a4 == "X" and a1 == "X" and m29 != True:
            m29 = True
            rest = "OMILL"
        elif b2 == "X" and b4 == "X" and b6 == "X" and m210 != True:
            m210 = True
            rest = "OMILL"
        elif c3 == "X" and c4 == "X" and c5 == "X" and m211 != True:
            m211 = True
            rest = "OMILL"
        elif d1 == "X" and d2 == "X" and d3 == "X" and m212 != True:
            m212 = True
            rest = "OMILL"
        elif d7 == "X" and d6 == "X" and d5 == "X" and m213 != True:
            m213 = True
            rest = "OMILL"
        elif e5 == "X" and e4 == "X" and e3 == "X" and m214 != True:
            m214 = True
            rest = "OMILL"
        elif f2 == "X" and f4 == "X" and f6 == "X" and m215 != True:
            m215 = True
            rest = "OMILL"
        elif g1 == "X" and g4 == "X" and g7 == "X" and m216 != True:
            m216 = True
            rest = "OMILL"
        """
        if notmillO(a7,d7,g7):
            m21 = False
        if notmillO(b6,d6,f6):
            m22 = False
        if notmillO(c5,d5,e5):
            m23 = False
        if notmillO(a4,b4,c4):
            m24 = False
        if notmillO(e4,f4,g4):
            m25 = False
        if notmillO(c3,d3,e3):
            m26 = False
        if notmillO(b2,d2,f2):
            m27 = False
        if notmillO(a1,d1,g1):
            m28 = False
        if notmillO(a7,a4,a1):
            m29 = False
        if notmillO(b2,b4,b6):
            m210 = False
        if notmillO(c3,c4,c5):
            m211 = False
        if notmillO(d1,d2,d3):
            m212 = False
        if notmillO(d7,d6,d5):
            m213 = False
        if notmillO(e5,e4,e3):
            m214 = False
        if notmillO(f2,f4,f6):
            m215 = False
        if notmillO(g1,g4,g7):
            m216 = False
        if a7 == "X" and d7 == "X" and g7 == "X":
            if all(x in inmill for x in ['a7', 'd7', 'g7']) == False:
                inmill.extend(["a7","d7","g7"])
            if m21 != True:
                m21 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'd7', 'g7']):
            inmill.remove("a7")
            inmill.remove("d7")
            inmill.remove("g7")
        if b6 == "X" and d6 == "X" and f6 == "X":
            if all(x in inmill for x in ['b6', 'd6', 'f6']) == False:
                inmill.extend(["b6","d6","f6"])
            if m22 != True and rest != "OMILL":
                m22 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b6', 'd6', 'f6']):
            inmill.remove("b6")
            inmill.remove("d6")
            inmill.remove("f6")
        if c5 == "X" and d5 == "X" and e5 == "X":
            if all(x in inmill for x in ['c5', 'd5', 'e5']) == False:
                inmill.extend(["c5","d5","e5"])
            if m23 != True and rest != "OMILL":
                m23 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c5', 'd5', 'e5']):
            inmill.remove("c5")
            inmill.remove("d5")
            inmill.remove("e5")
        if a4 == "X" and b4 == "X" and c4 == "X":
            if all(x in inmill for x in ['a4', 'b4', 'c4']) == False:
                inmill.extend(["a4","b4","c4"])
            if m24 != True and rest != "OMILL":
                m24 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a4', 'b4', 'c4']):
            inmill.remove("a4")
            inmill.remove("b4")
            inmill.remove("c4")
        if e4 == "X" and f4 == "X" and g4 == "X":
            if all(x in inmill for x in ['e4', 'f4', 'g4']) == False:
                inmill.extend(["e4","f4","g4"])
            if m25 != True and rest != "OMILL":
                m25 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e4', 'f4', 'g4']):
            inmill.remove("e4")
            inmill.remove("f4")
            inmill.remove("g4")
        if c3 == "X" and d3 == "X" and e3 == "X":
            if all(x in inmill for x in ['c3', 'd3', 'e3']) == False:
                inmill.extend(["c3","d3","e3"])
            if m26 != True and rest != "OMILL":
                m26 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'd3', 'e3']):
            inmill.remove("c3")
            inmill.remove("d3")
            inmill.remove("e3")
        if b2 == "X" and d2 == "X" and f2 == "X":
            if all(x in inmill for x in ['b2', 'd2', 'f2']) == False:
                inmill.extend(["b2","d2","f2"])
            if m27 != True and rest != "OMILL":
                m27 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'd2', 'f2']):
            inmill.remove("b2")
            inmill.remove("d2")
            inmill.remove("f2")
        if a1 == "X" and d1 == "X" and g1 == "X":
            if all(x in inmill for x in ['a1', 'd1', 'g1']) == False:
                inmill.extend(["a1","d1","g1"])
            if m28 != True and rest != "OMILL":
                m28 = True
                mi4 = True # for strategy
                rest = "OMILL"
        elif all(x in inmill for x in ['a1', 'd1', 'g1']):
            inmill.remove("a1")
            inmill.remove("d1")
            inmill.remove("g1")
        # VERTICALS
        if a7 == "X" and a4 == "X" and a1 == "X":
            if all(x in inmill for x in ['a7', 'a4', 'a1']) == False:
                inmill.extend(["a7","a4","a1"])
            if m29 != True and rest != "OMILL":
                m29 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'a4', 'a1']):
            inmill.remove("a7")
            inmill.remove("a4")
            inmill.remove("a1")
        if b2 == "X" and b4 == "X" and b6 == "X":
            if all(x in inmill for x in ['b2', 'b4', 'b6']) == False:
                inmill.extend(["b2","b4","b6"])
            if m210 != True and rest != "OMILL":
                m210 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'b4', 'b6']):
            inmill.remove("b2")
            inmill.remove("b4")
            inmill.remove("b6")
        if c3 == "X" and c4 == "X" and c5 == "X":
            if all(x in inmill for x in ['c3', 'c4', 'c5']) == False:
                inmill.extend(["c3","c4","c5"])
            if m211 != True and rest != "OMILL":
                m211 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'c4', 'c5']):
            inmill.remove("c3")
            inmill.remove("c4")
            inmill.remove("c5")
        if d1 == "X" and d2 == "X" and d3 == "X":
            if all(x in inmill for x in ['d1', 'd2', 'd3']) == False:
                inmill.extend(["d1","d2","d3"])
            if m212 != True and rest != "OMILL":
                m212 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d1', 'd2', 'd3']):
            inmill.remove("d1")
            inmill.remove("d2")
            inmill.remove("d3")
        if d7 == "X" and d6 == "X" and d5 == "X":
            if all(x in inmill for x in ['d7', 'd6', 'd5']) == False:
                inmill.extend(["d7","d6","d5"])
            if m213 != True and rest != "OMILL":
                m213 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d7', 'd6', 'd5']):
            inmill.remove("d7")
            inmill.remove("d6")
            inmill.remove("d5")
        if e5 == "X" and e4 == "X" and e3 == "X":
            if all(x in inmill for x in ['e5', 'e4', 'e3']) == False:
                inmill.extend(["e5","e4","e3"])
            if m214 != True and rest != "OMILL":
                m214 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e5', 'e4', 'e3']):
            inmill.remove("e5")
            inmill.remove("e4")
            inmill.remove("e3")
        if f2 == "X" and f4 == "X" and f6 == "X":
            if all(x in inmill for x in ['f2', 'f4', 'f6']) == False:
                inmill.extend(["f2","f4","f6"])
            if m215 != True and rest != "OMILL":
                m215 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['f2', 'f4', 'f6']):
            inmill.remove("f2")
            inmill.remove("f4")
            inmill.remove("f6")
        if g1 == "X" and g4 == "X" and g7 == "X":
            if all(x in inmill for x in ['g1', 'g4', 'g7']) == False:
                inmill.extend(["g1","g4","g7"])
            if m216 != True and rest != "OMILL":
                m216 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['g1', 'g4', 'g7']):
            inmill.remove("g1")
            inmill.remove("g4")
            inmill.remove("g7")
        if rest == "OMILL":
            ## SHALL MAKE IT BETTER!!
            pcs-=1
            go = False
            for i in possible_mills:
                if go == True:
                    break
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill(a,b,c,"player"):
                    for y in [i[0],i[1],i[2]]:
                        if go2 == True:
                            continue
                        exec("x = " + y)
                        if x == "O":
                            for q in [i[0],i[1],i[2]]:
                                exec("q = " + q)
                                if q == "X":
                                    go2 = True
                                    break
                            if y not in inmillP:
                                exec(y + " = '*'")
                                rmvd = y
                                go = True
                                break
                            else:
                                continue
                        else:
                            continue
            go2 = 0
            for i in possible_mills:
                if go == True:
                    break
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill2(a,b,c,"opp"):
                    for y in [i[0],i[1],i[2]]:
                        if go2 == True:
                            continue
                        exec("x = " + y)
                        if x == "O":
                            if y not in inmillP:
                                exec(y + " = '*'")
                                rmvd = y
                                go = True
                                break
                            else:
                                continue
                        else:
                            continue
            # random choosing
            while go != True:
                choice = random.choice(locations)
                while choice in inmillP:
                    choice = random.choice(locations)
                exec("i = " + choice)
                if i == "O":
                    exec(choice + " = '*'")
                    rmvd = choice
                    go = True
                else:
                    continue
while phase == "ofly":
    clear()
    if opcs < 3:
        phase = "pwin"
        break
    if opcs == 3 and pcs == 3:
        phase = "bfly"
        break
       # OPPONENT'S TURN
    if (
        rest != "MILL" and rest != "ERROR NVM" and
        rest != "ERROR BPL" and rest != "MFNVA" and 
        rest != "MTNVA" and rest != "ERROR BS" and
        rest != "ERROR IE" and phase == "ofly"
        ):
        sx = ("*","X")
        sat = 0
        while sat != 1:
            if sat == 0:
                choose_strategy(thebad)
            use_strategy()
            clear()
        # STRATEGY END
        if notmillO(a7,d7,g7):
            m21 = False
        if notmillO(b6,d6,f6):
            m22 = False
        if notmillO(c5,d5,e5):
            m23 = False
        if notmillO(a4,b4,c4):
            m24 = False
        if notmillO(e4,f4,g4):
            m25 = False
        if notmillO(c3,d3,e3):
            m26 = False
        if notmillO(b2,d2,f2):
            m27 = False
        if notmillO(a1,d1,g1):
            m28 = False
        if notmillO(a7,a4,a1):
            m29 = False
        if notmillO(b2,b4,b6):
            m210 = False
        if notmillO(c3,c4,c5):
            m211 = False
        if notmillO(d1,d2,d3):
            m212 = False
        if notmillO(d7,d6,d5):
            m213 = False
        if notmillO(e5,e4,e3):
            m214 = False
        if notmillO(f2,f4,f6):
            m215 = False
        if notmillO(g1,g4,g7):
            m216 = False
        if a7 == "X" and d7 == "X" and g7 == "X":
            if all(x in inmill for x in ['a7', 'd7', 'g7']) == False:
                inmill.extend(["a7","d7","g7"])
            if m21 != True:
                m21 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'd7', 'g7']):
            inmill.remove("a7")
            inmill.remove("d7")
            inmill.remove("g7")
        if b6 == "X" and d6 == "X" and f6 == "X":
            if all(x in inmill for x in ['b6', 'd6', 'f6']) == False:
                inmill.extend(["b6","d6","f6"])
            if m22 != True and rest != "OMILL":
                m22 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b6', 'd6', 'f6']):
            inmill.remove("b6")
            inmill.remove("d6")
            inmill.remove("f6")
        if c5 == "X" and d5 == "X" and e5 == "X":
            if all(x in inmill for x in ['c5', 'd5', 'e5']) == False:
                inmill.extend(["c5","d5","e5"])
            if m23 != True and rest != "OMILL":
                m23 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c5', 'd5', 'e5']):
            inmill.remove("c5")
            inmill.remove("d5")
            inmill.remove("e5")
        if a4 == "X" and b4 == "X" and c4 == "X":
            if all(x in inmill for x in ['a4', 'b4', 'c4']) == False:
                inmill.extend(["a4","b4","c4"])
            if m24 != True and rest != "OMILL":
                m24 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a4', 'b4', 'c4']):
            inmill.remove("a4")
            inmill.remove("b4")
            inmill.remove("c4")
        if e4 == "X" and f4 == "X" and g4 == "X":
            if all(x in inmill for x in ['e4', 'f4', 'g4']) == False:
                inmill.extend(["e4","f4","g4"])
            if m25 != True and rest != "OMILL":
                m25 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e4', 'f4', 'g4']):
            inmill.remove("e4")
            inmill.remove("f4")
            inmill.remove("g4")
        if c3 == "X" and d3 == "X" and e3 == "X":
            if all(x in inmill for x in ['c3', 'd3', 'e3']) == False:
                inmill.extend(["c3","d3","e3"])
            if m26 != True and rest != "OMILL":
                m26 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'd3', 'e3']):
            inmill.remove("c3")
            inmill.remove("d3")
            inmill.remove("e3")
        if b2 == "X" and d2 == "X" and f2 == "X":
            if all(x in inmill for x in ['b2', 'd2', 'f2']) == False:
                inmill.extend(["b2","d2","f2"])
            if m27 != True and rest != "OMILL":
                m27 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'd2', 'f2']):
            inmill.remove("b2")
            inmill.remove("d2")
            inmill.remove("f2")
        if a1 == "X" and d1 == "X" and g1 == "X":
            if all(x in inmill for x in ['a1', 'd1', 'g1']) == False:
                inmill.extend(["a1","d1","g1"])
            if m28 != True and rest != "OMILL":
                m28 = True
                mi4 = True # for strategy
                rest = "OMILL"
        elif all(x in inmill for x in ['a1', 'd1', 'g1']):
            inmill.remove("a1")
            inmill.remove("d1")
            inmill.remove("g1")
        # VERTICALS
        if a7 == "X" and a4 == "X" and a1 == "X":
            if all(x in inmill for x in ['a7', 'a4', 'a1']) == False:
                inmill.extend(["a7","a4","a1"])
            if m29 != True and rest != "OMILL":
                m29 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'a4', 'a1']):
            inmill.remove("a7")
            inmill.remove("a4")
            inmill.remove("a1")
        if b2 == "X" and b4 == "X" and b6 == "X":
            if all(x in inmill for x in ['b2', 'b4', 'b6']) == False:
                inmill.extend(["b2","b4","b6"])
            if m210 != True and rest != "OMILL":
                m210 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'b4', 'b6']):
            inmill.remove("b2")
            inmill.remove("b4")
            inmill.remove("b6")
        if c3 == "X" and c4 == "X" and c5 == "X":
            if all(x in inmill for x in ['c3', 'c4', 'c5']) == False:
                inmill.extend(["c3","c4","c5"])
            if m211 != True and rest != "OMILL":
                m211 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'c4', 'c5']):
            inmill.remove("c3")
            inmill.remove("c4")
            inmill.remove("c5")
        if d1 == "X" and d2 == "X" and d3 == "X":
            if all(x in inmill for x in ['d1', 'd2', 'd3']) == False:
                inmill.extend(["d1","d2","d3"])
            if m212 != True and rest != "OMILL":
                m212 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d1', 'd2', 'd3']):
            inmill.remove("d1")
            inmill.remove("d2")
            inmill.remove("d3")
        if d7 == "X" and d6 == "X" and d5 == "X":
            if all(x in inmill for x in ['d7', 'd6', 'd5']) == False:
                inmill.extend(["d7","d6","d5"])
            if m213 != True and rest != "OMILL":
                m213 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d7', 'd6', 'd5']):
            inmill.remove("d7")
            inmill.remove("d6")
            inmill.remove("d5")
        if e5 == "X" and e4 == "X" and e3 == "X":
            if all(x in inmill for x in ['e5', 'e4', 'e3']) == False:
                inmill.extend(["e5","e4","e3"])
            if m214 != True and rest != "OMILL":
                m214 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e5', 'e4', 'e3']):
            inmill.remove("e5")
            inmill.remove("e4")
            inmill.remove("e3")
        if f2 == "X" and f4 == "X" and f6 == "X":
            if all(x in inmill for x in ['f2', 'f4', 'f6']) == False:
                inmill.extend(["f2","f4","f6"])
            if m215 != True and rest != "OMILL":
                m215 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['f2', 'f4', 'f6']):
            inmill.remove("f2")
            inmill.remove("f4")
            inmill.remove("f6")
        if g1 == "X" and g4 == "X" and g7 == "X":
            if all(x in inmill for x in ['g1', 'g4', 'g7']) == False:
                inmill.extend(["g1","g4","g7"])
            if m216 != True and rest != "OMILL":
                m216 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['g1', 'g4', 'g7']):
            inmill.remove("g1")
            inmill.remove("g4")
            inmill.remove("g7")
        if rest == "OMILL":
            pcs-=1
            go = False
            while go != True:
                choice = random.choice(locations)
                while choice in inmillP:
                    choice = random.choice(locations)
                exec("i = " + choice)
                if i == "O":
                    exec(choice + " = '*'")
                    rmvd = choice
                    go = True
                else:
                    continue
    print "                                      a    b    c    d    e    f    g"
    print "                                 7    %s--------------%s--------------%s    7" % (a7, d7, g7) # 7
    print "                                      |              |              |"
    print "                                 6    |    %s---------%s---------%s    |    6" % (b6, d6, f6)  # 6
    print "                                      |    |         |         |    |"
    print "                                 5    |    |    %s----%s----%s    |    |    5" % (c5, d5, e5)  # 5
    print "                                      |    |    |         |    |    |"
    print "                                 4    %s----%s----%s         %s----%s----%s    4" % (a4, b4, c4, e4, f4, g4)  # 4
    print "                                      |    |    |         |    |    |"
    print "                                 3    |    |    %s----%s----%s    |    |    3"  % (c3, d3, e3) # 3
    print "                                      |    |         |         |    |"
    print "                                 2    |    %s---------%s---------%s    |    2" % (b2, d2, f2) # 2
    print "                                      |              |              |"
    print "                                 1    %s--------------%s--------------%s    1" % (a1, d1, g1)  # 1
    print "                                      a    b    c    d    e    f    g"
    print "Current phase: Flying (opponent)\n"
    if rest == True:
        print "Please move one of your pieces. E.g.: a1,d1 / g1,g4"
    if rest == "MILL":
        print "You have formed a mill!"
        print "Enter one of your opponent's pieces location to remove it!"
    elif rest == "OMILL":
        print "Your opponent have formed a mill and removed one of your pieces!"
    if rest == "MFNVA" and rest2 == "MTNVA":
        rest = True
        print "Neither %s nor %s is a valid location. Please try again." % (movef, movet)
    elif rest == "MFNVA":
        rest = True
        print "%s is not a valid location. Please try again." % movef
    elif rest2 == "MTNVA":
        rest2 = 0
        print "%s is not a valid location. Please try again" % movet
    if rest == "ERROR IE":
        print "You've entered %s. This is invalid." % movef
        print "Please enter a movement like the following: 'a1,d1' or 'g1,g4'"
    if rest == "ERROR BPL":
        print "You have entered an incorrect movement."
        print "You've tried to move from %s to %s" % (movef,movet)
        print "Please try again."
    if rest == "ERROR NVM":
        print "You have entered an incorrect movement."
        print "If you still experience this problem, please learn the rules."
        print "Please try again."
    if rest == "ERROR INMILL":
        rest = 'MILL'
        print "The piece that you are trying to remove is in mill."
        print "If the problem still occurs, please learn the rules of this game."
        print "Thereafter, if the problem still occurs, contact Us."
    print "Your pieces: %d" % pcs
    print "Opponent's pieces: %d" % opcs
    print "Opponent's level: %s" % ailvl
    print "Last movement: %s" % last # possible purpose - debug
    if debug == True:
        print "Don't move list: %r" % (dontmove) # debug only
        print "Result: %r       Put: %r" % (rest,put) # debug only
        print "'strategy' var: %r       'cs' - current strategy: %r" % (strategy, cs) # debug only
    # PLAYER TURN
    move = raw_input(">> ")
    if rest == "MILL":
        if move not in locations:
            rest = "ERROR BS"
        exec("i = " + move)
        if move in inmill:
            rest = "ERROR INMILL"
            continue
        if i == "X":
            exec(move + " = '*'")
            opcs-=1
            rest = True
        else:
            rest = "ERROR BS"
    else:
        move = move.replace("'","")
        try:
            move = move.split(',')
            movef = move[0]
            movet = move[1]
        except IndexError:
            rest = "ERROR IE"
            continue
        if movef not in locations:
            rest = "MFNVA"
        if movet not in locations:
            rest2 = "MTNVA"
        if rest == "MFNVA":
            continue
        if movef + "," + movet in validmovements or movet + "," + movef in validmovements:
            exec("i = " + movef)
            exec("d = " + movet)
            if i == "O" and d == "*":
                exec(movef + " = '*'")
                exec(movet + " = 'O'")
                rest = True
            else:
                rest = "ERROR BPL"
                continue
        else:
            rest = "ERROR NVM"
            continue
 # MILLS
    if notmill(a7,d7,g7):
        m1 = False
    if notmill(b6,d6,f6):
        m2 = False
    if notmill(c5,d5,e5):
        m3 = False
    if notmill(a4,b4,c4):
        m4 = False
    if notmill(e4,f4,g4):
        m5 = False
    if notmill(c3,d3,e3):
        m6 = False
    if notmill(b2,d2,f2):
        m7 = False
    if notmill(a1,d1,g1):
        m8 = False
    if notmill(a7,a4,a1):
        m9 = False
    if notmill(b2,b4,b6):
        m10 = False
    if notmill(c3,c4,c5):
        m11 = False
    if notmill(d1,d2,d3):
        m12 = False
    if notmill(d7,d6,d5):
        m13 = False
    if notmill(e5,e4,e3):
        m14 = False
    if notmill(f2,f4,f6):
        m15 = False
    if notmill(g1,g4,g7):
        m16 = False
    if a7 == "O" and d7 == "O" and g7 == "O":
        if all(x in inmillP for x in ['a7', 'd7', 'g7']) == False:
            inmillP.extend(["a7","d7","g7"])
        if m1 != True:
            m1 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'd7', 'g7']):
        inmillP.remove("a7")
        inmillP.remove("d7")
        inmillP.remove("g7")
    if b6 == "O" and d6 == "O" and f6 == "O":
        if all(x in inmillP for x in ['b6', 'd6', 'f6']) == False:
            inmillP.extend(["b6","d6","f6"])
        if m2 != True and rest != "MILL":
            m2 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b6', 'd6', 'f6']):
        inmillP.remove("b6")
        inmillP.remove("d6")
        inmillP.remove("f6")
    if c5 == "O" and d5 == "O" and e5 == "O":
        if all(x in inmillP for x in ['c5', 'd5', 'e5']) == False:
            inmillP.extend(["c5","d5","e5"])
        if m3 != True and rest != "MILL":
            m3 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c5', 'd5', 'e5']):
        inmillP.remove("c5")
        inmillP.remove("d5")
        inmillP.remove("e5")
    if a4 == "O" and b4 == "O" and c4 == "O":
        if all(x in inmillP for x in ['a4', 'b4', 'c4']) == False:
            inmillP.extend(["a4","b4","c4"])
        if m4 != True and rest != "MILL":
            m4 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a4', 'b4', 'c4']):
        inmillP.remove("a4")
        inmillP.remove("b4")
        inmillP.remove("c4")
    if e4 == "O" and f4 == "O" and g4 == "O":
        if all(x in inmillP for x in ['e4', 'f4', 'g4']) == False:
            inmillP.extend(["e4","f4","g4"])
        if m5 != True and rest != "MILL":
            m5 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e4', 'f4', 'g4']):
        inmillP.remove("e4")
        inmillP.remove("f4")
        inmillP.remove("g4")
    if c3 == "O" and d3 == "O" and e3 == "O":
        if all(x in inmillP for x in ['c3', 'd3', 'e3']) == False:
            inmillP.extend(["c3","d3","e3"])
        if m6 != True and rest != "MILL":
            m6 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'd3', 'e3']):
        inmillP.remove("c3")
        inmillP.remove("d3")
        inmillP.remove("e3")
    if b2 == "O" and d2 == "O" and f2 == "O":
        if all(x in inmillP for x in ['b2', 'd2', 'f2']) == False:
            inmillP.extend(["b2","d2","f2"])
        if m7 != True and rest != "MILL":
            m7 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'd2', 'f2']):
        inmillP.remove("b2")
        inmillP.remove("d2")
        inmillP.remove("f2")
    if a1 == "O" and d1 == "O" and g1 == "O":
        if all(x in inmillP for x in ['a1', 'd1', 'g1']) == False:
            inmillP.extend(["a1","d1","g1"])
        if m8 != True and rest != "MILL":
            m8 = True
            mi4 = True # for strategy
            rest = "MILL"
    elif all(x in inmillP for x in ['a1', 'd1', 'g1']):
        inmillP.remove("a1")
        inmillP.remove("d1")
        inmillP.remove("g1")
    # VERTICALS
    if a7 == "O" and a4 == "O" and a1 == "O":
        if all(x in inmillP for x in ['a7', 'a4', 'a1']) == False:
            inmillP.extend(["a7","a4","a1"])
        if m9 != True and rest != "MILL":
            m9 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'a4', 'a1']):
        inmillP.remove("a7")
        inmillP.remove("a4")
        inmillP.remove("a1")
    if b2 == "O" and b4 == "O" and b6 == "O":
        if all(x in inmillP for x in ['b2', 'b4', 'b6']) == False:
            inmillP.extend(["b2","b4","b6"])
        if m10 != True and rest != "MILL":
            m10 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'b4', 'b6']):
        inmillP.remove("b2")
        inmillP.remove("b4")
        inmillP.remove("b6")
    if c3 == "O" and c4 == "O" and c5 == "O":
        if all(x in inmillP for x in ['c3', 'c4', 'c5']) == False:
            inmillP.extend(["c3","c4","c5"])
        if m11 != True and rest != "MILL":
            m11 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'c4', 'c5']):
        inmillP.remove("c3")
        inmillP.remove("c4")
        inmillP.remove("c5")
    if d1 == "O" and d2 == "O" and d3 == "O":
        if all(x in inmillP for x in ['d1', 'd2', 'd3']) == False:
            inmillP.extend(["d1","d2","d3"])
        if m12 != True and rest != "MILL":
            m12 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d1', 'd2', 'd3']):
        inmillP.remove("d1")
        inmillP.remove("d2")
        inmillP.remove("d3")
    if d7 == "O" and d6 == "O" and d5 == "O":
        if all(x in inmillP for x in ['d7', 'd6', 'd5']) == False:
            inmillP.extend(["d7","d6","d5"])
        if m13 != True and rest != "MILL":
            m13 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d7', 'd6', 'd5']):
        inmillP.remove("d7")
        inmillP.remove("d6")
        inmillP.remove("d5")
    if e5 == "O" and e4 == "O" and e3 == "O":
        if all(x in inmillP for x in ['e5', 'e4', 'e3']) == False:
            inmillP.extend(["e5","e4","e3"])
        if m14 != True and rest != "MILL":
            m14 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e5', 'e4', 'e3']):
        inmillP.remove("e5")
        inmillP.remove("e4")
        inmillP.remove("e3")
    if f2 == "O" and f4 == "O" and f6 == "O":
        if all(x in inmillP for x in ['f2', 'f4', 'f6']) == False:
            inmillP.extend(["f2","f4","f6"])
        if m15 != True and rest != "MILL":
            m15 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['f2', 'f4', 'f6']):
        inmillP.remove("f2")
        inmillP.remove("f4")
        inmillP.remove("f6")
    if g1 == "O" and g4 == "O" and g7 == "O":
        if all(x in inmillP for x in ['g1', 'g4', 'g7']) == False:
            inmillP.extend(["g1","g4","g7"])
        if m16 != True and rest != "MILL":
            m16 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['g1', 'g4', 'g7']):
        inmillP.remove("g1")
        inmillP.remove("g4")
        inmillP.remove("g7")
    """
    if a7 == "O" and d7 == "O" and g7 == "O" and m1 != True:
        m1 = True
        rest = "MILL"
    elif b6 == "O" and d6 == "O" and f6 == "O" and m2 != True:
        m2 = True
        rest = "MILL"
    elif c5 == "O" and d5 == "O" and e5 == "O" and m3 != True:
        m3 = True
        rest = "MILL"
    elif a4 == "O" and b4 == "O" and c4 == "O" and m4 != True:
        m4 = True
        rest = "MILL"
    elif e4 == "O" and f4 == "O" and g4 == "O" and m5 != True:
        m5 = True
        rest = "MILL"
    elif c3 == "O" and d3 == "O" and e3 == "O" and m6 != True:
        m6 = True
        rest = "MILL"
    elif b2 == "O" and d2 == "O" and f2 == "O" and m7 != True:
        m7 = True
        rest = "MILL"
    elif a1 == "O" and d1 == "O" and g1 == "O" and m8 != True:
        m8 = True
        rest = "MILL"
    # VERTICALS
    elif a7 == "O" and a4 == "O" and a1 == "O" and m9 != True:
        m9 = True
        rest = "MILL"
    elif b2 == "O" and b4 == "O" and b6 == "O" and m10 != True:
        m10 = True
        rest = "MILL"
    elif c3 == "O" and c4 == "O" and c5 == "O" and m11 != True:
        m11 = True
        rest = "MILL"
    elif d1 == "O" and d2 == "O" and d3 == "O" and m12 != True:
        m12 = True
        rest = "MILL"
    elif d7 == "O" and d6 == "O" and d5 == "O" and m13 != True:
        m13 = True
        rest = "MILL"
    elif e5 == "O" and e4 == "O" and e3 == "O" and m14 != True:
        m14 = True
        rest = "MILL"
    elif f2 == "O" and f4 == "O" and f6 == "O" and m15 != True:
        m15 = True
        rest = "MILL"
    elif g1 == "O" and g4 == "O" and g7 == "O" and m16 != True:
        m16 = True
        rest = "MILL"
    """
while phase == "fly":
    inmill = list(set(inmill))
    inmillP = list(set(inmillP))
    clear()
    if opcs == 3 and pcs == 3:
        phase = "bfly"
        break
    if pcs < 3:
        phase = "plose"
        break
    print "                                      a    b    c    d    e    f    g"
    print "                                 7    %s--------------%s--------------%s    7" % (a7, d7, g7) # 7
    print "                                      |              |              |"
    print "                                 6    |    %s---------%s---------%s    |    6" % (b6, d6, f6)  # 6
    print "                                      |    |         |         |    |"
    print "                                 5    |    |    %s----%s----%s    |    |    5" % (c5, d5, e5)  # 5
    print "                                      |    |    |         |    |    |"
    print "                                 4    %s----%s----%s         %s----%s----%s    4" % (a4, b4, c4, e4, f4, g4)  # 4
    print "                                      |    |    |         |    |    |"
    print "                                 3    |    |    %s----%s----%s    |    |    3"  % (c3, d3, e3) # 3
    print "                                      |    |         |         |    |"
    print "                                 2    |    %s---------%s---------%s    |    2" % (b2, d2, f2) # 2
    print "                                      |              |              |"
    print "                                 1    %s--------------%s--------------%s    1" % (a1, d1, g1)  # 1
    print "                                      a    b    c    d    e    f    g"
    print "Current phase: Flying (player)\n"
    if rest == True:
        print "Please fly with one of your pieces. E.g.: a1,g7 / d3,d5"
    if rest == "MILL":
        print "You have formed a mill!"
        print "Enter one of your opponent's pieces location to remove it!"
    elif rest == "OMILL":
        print "Your opponent have formed a mill and removed %r" % rmvd
    if rest == "MFNVA" and rest2 == "MTNVA":
        rest = True
        print "Neither %s nor %s is a valid location. Please try again." % (movef, movet)
    elif rest == "MFNVA":
        rest = True
        print "%s is not a valid location. Please try again." % movef
    elif rest2 == "MTNVA":
        rest2 = 0
        print "%s is not a valid location. Please try again." % movet
    if rest == "ERROR IE":
        print "You've entered %s. This is invalid." % movef
        print "Please enter a movement like the following: 'a1,d1' or 'g1,g4'"
    if rest == "ERROR BPL":
        print "You have entered an incorrect movement."
        print "You've tried to move from %s to %s" % (movef,movet)
        print "Please try again."
    if rest == "ERROR NVM":
        print "You have entered an incorrect movement."
        print "If you still experience this problem, please learn the rules."
        print "Please try again."
    if rest == "ERROR BS":
        rest = 'MILL'
        print "The entered location is not valid. Please try again."
    if rest == "ERROR INMILL":
        rest = 'MILL'
        print "The piece that you are trying to remove is in mill."
        print "If the problem still occurs, please learn the rules of this game."
        print "Thereafter, if the problem still occurs, contact Us."
    print "Your pieces: %d" % pcs
    print "Opponent's pieces: %d" % opcs
    print "Last movement: %s" % last
    print "Opponent's level: %s" % ailvl
    if debug == True:
        print "Player InMill: %r    Opponent InMill: %r" % (inmillP, inmill) # debug only
        print "Result: %r       Put: %r" % (rest,put) # debug only
        print "'strategy' var: %r       'cs' - current strategy: %r" % (strategy, cs) # debug only
    # PLAYER TURN
    move = raw_input(">> ")
    if rest == "MILL":
        if move not in locations:
            rest = "ERROR BS"
        exec("i = " + move)
        if move in inmill:
            rest = "ERROR INMILL"
            continue
        if i == "X":
            exec(move + " = '*'")
            opcs-=1
            rest = True
        else:
            rest = "ERROR BS"
    else:
        move = move.replace("'","")
        try:
            move = move.split(',')
            movef = move[0]
            movet = move[1]
        except IndexError:
            rest = "ERROR IE"
            continue
        if movef not in locations:
            rest = "MFNVA"
        if movet not in locations:
            rest2 = "MTNVA"
        if rest == "MFNVA" or rest2 == "MTNVA":
            rest = "ERRORback"
            continue
        exec("a = " + movef)
        exec("b = " + movet)
        if a == "O" and b == "*":
            exec(movef + " = '*'")
            exec(movet + " = 'O'")
        else:
            rest = "ERROR BPL"
            continue
    # MILLS
    if True: # notmill() tech
        if notmill(a7,d7,g7):
            m1 = False
        if notmill(b6,d6,f6):
            m2 = False
        if notmill(c5,d5,e5):
            m3 = False
        if notmill(a4,b4,c4):
            m4 = False
        if notmill(e4,f4,g4):
            m5 = False
        if notmill(c3,d3,e3):
            m6 = False
        if notmill(b2,d2,f2):
            m7 = False
        if notmill(a1,d1,g1):
            m8 = False
        if notmill(a7,a4,a1):
            m9 = False
        if notmill(b2,b4,b6):
            m10 = False
        if notmill(c3,c4,c5):
            m11 = False
        if notmill(d1,d2,d3):
            m12 = False
        if notmill(d7,d6,d5):
            m13 = False
        if notmill(e5,e4,e3):
            m14 = False
        if notmill(f2,f4,f6):
            m15 = False
        if notmill(g1,g4,g7):
            m16 = False
    if a7 == "O" and d7 == "O" and g7 == "O":
        if all(x in inmillP for x in ['a7', 'd7', 'g7']) == False:
            inmillP.extend(["a7","d7","g7"])
        if m1 != True:
            m1 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'd7', 'g7']):
        inmillP.remove("a7")
        inmillP.remove("d7")
        inmillP.remove("g7")
    if b6 == "O" and d6 == "O" and f6 == "O":
        if all(x in inmillP for x in ['b6', 'd6', 'f6']) == False:
            inmillP.extend(["b6","d6","f6"])
        if m2 != True and rest != "MILL":
            m2 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b6', 'd6', 'f6']):
        inmillP.remove("b6")
        inmillP.remove("d6")
        inmillP.remove("f6")
    if c5 == "O" and d5 == "O" and e5 == "O":
        if all(x in inmillP for x in ['c5', 'd5', 'e5']) == False:
            inmillP.extend(["c5","d5","e5"])
        if m3 != True and rest != "MILL":
            m3 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c5', 'd5', 'e5']):
        inmillP.remove("c5")
        inmillP.remove("d5")
        inmillP.remove("e5")
    if a4 == "O" and b4 == "O" and c4 == "O":
        if all(x in inmillP for x in ['a4', 'b4', 'c4']) == False:
            inmillP.extend(["a4","b4","c4"])
        if m4 != True and rest != "MILL":
            m4 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a4', 'b4', 'c4']):
        inmillP.remove("a4")
        inmillP.remove("b4")
        inmillP.remove("c4")
    if e4 == "O" and f4 == "O" and g4 == "O":
        if all(x in inmillP for x in ['e4', 'f4', 'g4']) == False:
            inmillP.extend(["e4","f4","g4"])
        if m5 != True and rest != "MILL":
            m5 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e4', 'f4', 'g4']):
        inmillP.remove("e4")
        inmillP.remove("f4")
        inmillP.remove("g4")
    if c3 == "O" and d3 == "O" and e3 == "O":
        if all(x in inmillP for x in ['c3', 'd3', 'e3']) == False:
            inmillP.extend(["c3","d3","e3"])
        if m6 != True and rest != "MILL":
            m6 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'd3', 'e3']):
        inmillP.remove("c3")
        inmillP.remove("d3")
        inmillP.remove("e3")
    if b2 == "O" and d2 == "O" and f2 == "O":
        if all(x in inmillP for x in ['b2', 'd2', 'f2']) == False:
            inmillP.extend(["b2","d2","f2"])
        if m7 != True and rest != "MILL":
            m7 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'd2', 'f2']):
        inmillP.remove("b2")
        inmillP.remove("d2")
        inmillP.remove("f2")
    if a1 == "O" and d1 == "O" and g1 == "O":
        if all(x in inmillP for x in ['a1', 'd1', 'g1']) == False:
            inmillP.extend(["a1","d1","g1"])
        if m8 != True and rest != "MILL":
            m8 = True
            mi4 = True # for strategy
            rest = "MILL"
    elif all(x in inmillP for x in ['a1', 'd1', 'g1']):
        inmillP.remove("a1")
        inmillP.remove("d1")
        inmillP.remove("g1")
    # VERTICALS
    if a7 == "O" and a4 == "O" and a1 == "O":
        if all(x in inmillP for x in ['a7', 'a4', 'a1']) == False:
            inmillP.extend(["a7","a4","a1"])
        if m9 != True and rest != "MILL":
            m9 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'a4', 'a1']):
        inmillP.remove("a7")
        inmillP.remove("a4")
        inmillP.remove("a1")
    if b2 == "O" and b4 == "O" and b6 == "O":
        if all(x in inmillP for x in ['b2', 'b4', 'b6']) == False:
            inmillP.extend(["b2","b4","b6"])
        if m10 != True and rest != "MILL":
            m10 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'b4', 'b6']):
        inmillP.remove("b2")
        inmillP.remove("b4")
        inmillP.remove("b6")
    if c3 == "O" and c4 == "O" and c5 == "O":
        if all(x in inmillP for x in ['c3', 'c4', 'c5']) == False:
            inmillP.extend(["c3","c4","c5"])
        if m11 != True and rest != "MILL":
            m11 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'c4', 'c5']):
        inmillP.remove("c3")
        inmillP.remove("c4")
        inmillP.remove("c5")
    if d1 == "O" and d2 == "O" and d3 == "O":
        if all(x in inmillP for x in ['d1', 'd2', 'd3']) == False:
            inmillP.extend(["d1","d2","d3"])
        if m12 != True and rest != "MILL":
            m12 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d1', 'd2', 'd3']):
        inmillP.remove("d1")
        inmillP.remove("d2")
        inmillP.remove("d3")
    if d7 == "O" and d6 == "O" and d5 == "O":
        if all(x in inmillP for x in ['d7', 'd6', 'd5']) == False:
            inmillP.extend(["d7","d6","d5"])
        if m13 != True and rest != "MILL":
            m13 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d7', 'd6', 'd5']):
        inmillP.remove("d7")
        inmillP.remove("d6")
        inmillP.remove("d5")
    if e5 == "O" and e4 == "O" and e3 == "O":
        if all(x in inmillP for x in ['e5', 'e4', 'e3']) == False:
            inmillP.extend(["e5","e4","e3"])
        if m14 != True and rest != "MILL":
            m14 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e5', 'e4', 'e3']):
        inmillP.remove("e5")
        inmillP.remove("e4")
        inmillP.remove("e3")
    if f2 == "O" and f4 == "O" and f6 == "O":
        if all(x in inmillP for x in ['f2', 'f4', 'f6']) == False:
            inmillP.extend(["f2","f4","f6"])
        if m15 != True and rest != "MILL":
            m15 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['f2', 'f4', 'f6']):
        inmillP.remove("f2")
        inmillP.remove("f4")
        inmillP.remove("f6")
    if g1 == "O" and g4 == "O" and g7 == "O":
        if all(x in inmillP for x in ['g1', 'g4', 'g7']) == False:
            inmillP.extend(["g1","g4","g7"])
        if m16 != True and rest != "MILL":
            m16 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['g1', 'g4', 'g7']):
        inmillP.remove("g1")
        inmillP.remove("g4")
        inmillP.remove("g7")
    # OPPONENT'S TURN
    if (
        rest != "MILL" and rest != "ERROR NVM" and
        rest != "ERROR BPL" and rest != "MFNVA" and 
        rest != "MTNVA" and rest != "ERROR BS" and
        rest != "ERROR IE" and rest != "ERRORback" and
        rest != "ERROR INMILL" and phase == "fly"
        ):
        sx = ("*","X")
        sat = 0
        qr = 0
        while sat != 1:
            qr+=1
            # # # E M E R G E N C Y # # #
            #  Shall remove at release  #
            if qr == 15:
                print "Entered emergency"
                raw_input()
                strategy = 999
                use_strategy()
                sat = 1
                break
            #  Shall remove at release  #
            # # # E M E R G E N C Y # # #
            if sat == 0:
                choose_strategy(thebad)
            use_strategy()
        # STRATEGY END
        if notmillO(a7,d7,g7):
            m21 = False
        if notmillO(b6,d6,f6):
            m22 = False
        if notmillO(c5,d5,e5):
            m23 = False
        if notmillO(a4,b4,c4):
            m24 = False
        if notmillO(e4,f4,g4):
            m25 = False
        if notmillO(c3,d3,e3):
            m26 = False
        if notmillO(b2,d2,f2):
            m27 = False
        if notmillO(a1,d1,g1):
            m28 = False
        if notmillO(a7,a4,a1):
            m29 = False
        if notmillO(b2,b4,b6):
            m210 = False
        if notmillO(c3,c4,c5):
            m211 = False
        if notmillO(d1,d2,d3):
            m212 = False
        if notmillO(d7,d6,d5):
            m213 = False
        if notmillO(e5,e4,e3):
            m214 = False
        if notmillO(f2,f4,f6):
            m215 = False
        if notmillO(g1,g4,g7):
            m216 = False
        if a7 == "X" and d7 == "X" and g7 == "X":
            if all(x in inmill for x in ['a7', 'd7', 'g7']) == False:
                inmill.extend(["a7","d7","g7"])
            if m21 != True:
                m21 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'd7', 'g7']):
            inmill.remove("a7")
            inmill.remove("d7")
            inmill.remove("g7")
        if b6 == "X" and d6 == "X" and f6 == "X":
            if all(x in inmill for x in ['b6', 'd6', 'f6']) == False:
                inmill.extend(["b6","d6","f6"])
            if m22 != True and rest != "OMILL":
                m22 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b6', 'd6', 'f6']):
            inmill.remove("b6")
            inmill.remove("d6")
            inmill.remove("f6")
        if c5 == "X" and d5 == "X" and e5 == "X":
            if all(x in inmill for x in ['c5', 'd5', 'e5']) == False:
                inmill.extend(["c5","d5","e5"])
            if m23 != True and rest != "OMILL":
                m23 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c5', 'd5', 'e5']):
            inmill.remove("c5")
            inmill.remove("d5")
            inmill.remove("e5")
        if a4 == "X" and b4 == "X" and c4 == "X":
            if all(x in inmill for x in ['a4', 'b4', 'c4']) == False:
                inmill.extend(["a4","b4","c4"])
            if m24 != True and rest != "OMILL":
                m24 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a4', 'b4', 'c4']):
            inmill.remove("a4")
            inmill.remove("b4")
            inmill.remove("c4")
        if e4 == "X" and f4 == "X" and g4 == "X":
            if all(x in inmill for x in ['e4', 'f4', 'g4']) == False:
                inmill.extend(["e4","f4","g4"])
            if m25 != True and rest != "OMILL":
                m25 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e4', 'f4', 'g4']):
            inmill.remove("e4")
            inmill.remove("f4")
            inmill.remove("g4")
        if c3 == "X" and d3 == "X" and e3 == "X":
            if all(x in inmill for x in ['c3', 'd3', 'e3']) == False:
                inmill.extend(["c3","d3","e3"])
            if m26 != True and rest != "OMILL":
                m26 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'd3', 'e3']):
            inmill.remove("c3")
            inmill.remove("d3")
            inmill.remove("e3")
        if b2 == "X" and d2 == "X" and f2 == "X":
            if all(x in inmill for x in ['b2', 'd2', 'f2']) == False:
                inmill.extend(["b2","d2","f2"])
            if m27 != True and rest != "OMILL":
                m27 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'd2', 'f2']):
            inmill.remove("b2")
            inmill.remove("d2")
            inmill.remove("f2")
        if a1 == "X" and d1 == "X" and g1 == "X":
            if all(x in inmill for x in ['a1', 'd1', 'g1']) == False:
                inmill.extend(["a1","d1","g1"])
            if m28 != True and rest != "OMILL":
                m28 = True
                mi4 = True # for strategy
                rest = "OMILL"
        elif all(x in inmill for x in ['a1', 'd1', 'g1']):
            inmill.remove("a1")
            inmill.remove("d1")
            inmill.remove("g1")
        # VERTICALS
        if a7 == "X" and a4 == "X" and a1 == "X":
            if all(x in inmill for x in ['a7', 'a4', 'a1']) == False:
                inmill.extend(["a7","a4","a1"])
            if m29 != True and rest != "OMILL":
                m29 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'a4', 'a1']):
            inmill.remove("a7")
            inmill.remove("a4")
            inmill.remove("a1")
        if b2 == "X" and b4 == "X" and b6 == "X":
            if all(x in inmill for x in ['b2', 'b4', 'b6']) == False:
                inmill.extend(["b2","b4","b6"])
            if m210 != True and rest != "OMILL":
                m210 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'b4', 'b6']):
            inmill.remove("b2")
            inmill.remove("b4")
            inmill.remove("b6")
        if c3 == "X" and c4 == "X" and c5 == "X":
            if all(x in inmill for x in ['c3', 'c4', 'c5']) == False:
                inmill.extend(["c3","c4","c5"])
            if m211 != True and rest != "OMILL":
                m211 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'c4', 'c5']):
            inmill.remove("c3")
            inmill.remove("c4")
            inmill.remove("c5")
        if d1 == "X" and d2 == "X" and d3 == "X":
            if all(x in inmill for x in ['d1', 'd2', 'd3']) == False:
                inmill.extend(["d1","d2","d3"])
            if m212 != True and rest != "OMILL":
                m212 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d1', 'd2', 'd3']):
            inmill.remove("d1")
            inmill.remove("d2")
            inmill.remove("d3")
        if d7 == "X" and d6 == "X" and d5 == "X":
            if all(x in inmill for x in ['d7', 'd6', 'd5']) == False:
                inmill.extend(["d7","d6","d5"])
            if m213 != True and rest != "OMILL":
                m213 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d7', 'd6', 'd5']):
            inmill.remove("d7")
            inmill.remove("d6")
            inmill.remove("d5")
        if e5 == "X" and e4 == "X" and e3 == "X":
            if all(x in inmill for x in ['e5', 'e4', 'e3']) == False:
                inmill.extend(["e5","e4","e3"])
            if m214 != True and rest != "OMILL":
                m214 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e5', 'e4', 'e3']):
            inmill.remove("e5")
            inmill.remove("e4")
            inmill.remove("e3")
        if f2 == "X" and f4 == "X" and f6 == "X":
            if all(x in inmill for x in ['f2', 'f4', 'f6']) == False:
                inmill.extend(["f2","f4","f6"])
            if m215 != True and rest != "OMILL":
                m215 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['f2', 'f4', 'f6']):
            inmill.remove("f2")
            inmill.remove("f4")
            inmill.remove("f6")
        if g1 == "X" and g4 == "X" and g7 == "X":
            if all(x in inmill for x in ['g1', 'g4', 'g7']) == False:
                inmill.extend(["g1","g4","g7"])
            if m216 != True and rest != "OMILL":
                m216 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['g1', 'g4', 'g7']):
            inmill.remove("g1")
            inmill.remove("g4")
            inmill.remove("g7")
        if rest == "OMILL":
            ## SHALL MAKE IT BETTER!!
            pcs-=1
            go = False
            for i in possible_mills:
                if go == True:
                    break
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill(a,b,c,"player"):
                    for y in [i[0],i[1],i[2]]:
                        if go2 == True:
                            continue
                        exec("x = " + y)
                        if x == "O":
                            for q in [i[0],i[1],i[2]]:
                                exec("q = " + q)
                                if q == "X":
                                    go2 = True
                                    break
                            if y not in inmillP:
                                exec(y + " = '*'")
                                rmvd = y
                                go = True
                                break
                            else:
                                continue
                        else:
                            continue
            go2 = 0
            for i in possible_mills:
                if go == True:
                    break
                i = i.split(',')
                exec("a = " + i[0])
                exec("b = " + i[1])
                exec("c = " + i[2])
                if pmill2(a,b,c,"opp"):
                    for y in [i[0],i[1],i[2]]:
                        if go2 == True:
                            continue
                        exec("x = " + y)
                        if x == "O":
                            if y not in inmillP:
                                exec(y + " = '*'")
                                rmvd = y
                                go = True
                                break
                            else:
                                continue
                        else:
                            continue
            # random choosing
            while go != True:
                choice = random.choice(locations)
                while choice in inmillP:
                    choice = random.choice(locations)
                exec("i = " + choice)
                if i == "O":
                    exec(choice + " = '*'")
                    rmvd = choice
                    go = True
                else:
                    continue
while phase == "bfly":
    print "                                      a    b    c    d    e    f    g"
    print "                                 7    %s--------------%s--------------%s    7" % (a7, d7, g7) # 7
    print "                                      |              |              |"
    print "                                 6    |    %s---------%s---------%s    |    6" % (b6, d6, f6)  # 6
    print "                                      |    |         |         |    |"
    print "                                 5    |    |    %s----%s----%s    |    |    5" % (c5, d5, e5)  # 5
    print "                                      |    |    |         |    |    |"
    print "                                 4    %s----%s----%s         %s----%s----%s    4" % (a4, b4, c4, e4, f4, g4)  # 4
    print "                                      |    |    |         |    |    |"
    print "                                 3    |    |    %s----%s----%s    |    |    3"  % (c3, d3, e3) # 3
    print "                                      |    |         |         |    |"
    print "                                 2    |    %s---------%s---------%s    |    2" % (b2, d2, f2) # 2
    print "                                      |              |              |"
    print "                                 1    %s--------------%s--------------%s    1" % (a1, d1, g1)  # 1
    print "                                      a    b    c    d    e    f    g" 
    print "Current Phase: Flying\n"
    # DO NOT MAKE ERROR CATCH
    # ERRORback is the catcher below
    if rest == True:
        print "Please fly with one of your pieces. E.g.: a1,g7 / d3,d5"
    if rest == "MILL":
        print "You have formed a mill."
        print "Enter one of your opponent's pieces location to remove it!"
    elif rest == "OMILL":
        print "Your opponent have formed a mill and removed %r" % rmvd
    if rest == "ERROR BS":
        rest = 'MILL'
        print "The entered location is not valid. Please try again."
    if rest == "ERROR INMILL":
        rest = 'MILL'
        print "The piece that you are trying to remove is in mill."
        print "If the problem still occurs, please learn the rules of this game."
        print "Thereafter, if the problem still occurs, contact Us."
    if rest == "ERROR IE":
        print "You've entered %s. This is invalid." % movef
        print "Please enter a movement like the following: 'a1,g4' or 'g7,d1'"
    if rest == "MFNVA" and rest2 == "MTNVA":
        rest = True
        print "Neither %s nor %s is a valid location. Please try again." % (movef, movet)
    elif rest == "MFNVA":
        rest = True
        print "%s is not a valid location. Please try again." % movef
    elif rest2 == "MTNVA":
        rest2 = 0
        print "%s is not a valid location. Please try again" % movet
    if rest == "ERROR BPL":
        print "You have entered an incorrect movement."
        print "You've tried to move from %s to %s" % (movef,movet)
        print "Please try again."
    print "Your pieces: %d" % pcs
    print "Opponent's pieces: %d" % opcs
    print "Opponent's level: %s" % ailvl
    print "Last movement: %s" % last # possible purpose - debug
    if debug == True:
        print "Player InMill: %r    Opponent InMill: %r" % (inmillP, inmill) # debug only
        print "Result: %r       Put: %r" % (rest,put) # debug only
        print "'strategy' var: %r       'cs' - current strategy: %r" % (strategy, cs) # debug only
    # PLAYER'S TURN
    move =  raw_input(">> ")
    if rest == "MILL":
        if move not in locations:
            rest = "ERROR BS"
        exec("i = " + move)
        if move in inmill:
            rest = "ERROR INMILL"
            continue
        if i == "X":
            exec(move + " = '*'")
            opcs-=1
            rest = True
        else:
            rest = "ERROR BS"
    else:
        move = move.replace("'","")
        try:
            move = move.split(',')
            movef = move[0]
            movet = move[1]
        except IndexError:
            rest = "ERROR IE"
            continue
        if movef not in locations:
            rest = "MFNVA"
        if movet not in locations:
            rest2 = "MTNVA"
        if rest == "MFNVA" or rest2 == "MTNVA":
            rest = "ERRORback"
            continue
        exec("a = " + movef)
        exec("b = " + movet)
        if a == "O" and b == "*":
            exec(movef + " = '*'")
            exec(movet + " = 'O'")
        else:
            rest = "ERROR BPL"
            continue
    # MILLS
    if notmill(a7,d7,g7):
        m1 = False
    if notmill(b6,d6,f6):
        m2 = False
    if notmill(c5,d5,e5):
        m3 = False
    if notmill(a4,b4,c4):
        m4 = False
    if notmill(e4,f4,g4):
        m5 = False
    if notmill(c3,d3,e3):
        m6 = False
    if notmill(b2,d2,f2):
        m7 = False
    if notmill(a1,d1,g1):
        m8 = False
    if notmill(a7,a4,a1):
        m9 = False
    if notmill(b2,b4,b6):
        m10 = False
    if notmill(c3,c4,c5):
        m11 = False
    if notmill(d1,d2,d3):
        m12 = False
    if notmill(d7,d6,d5):
        m13 = False
    if notmill(e5,e4,e3):
        m14 = False
    if notmill(f2,f4,f6):
        m15 = False
    if notmill(g1,g4,g7):
        m16 = False
    if a7 == "O" and d7 == "O" and g7 == "O":
        if all(x in inmillP for x in ['a7', 'd7', 'g7']) == False:
            inmillP.extend(["a7","d7","g7"])
        if m1 != True:
            m1 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'd7', 'g7']):
        inmillP.remove("a7")
        inmillP.remove("d7")
        inmillP.remove("g7")
    if b6 == "O" and d6 == "O" and f6 == "O":
        if all(x in inmillP for x in ['b6', 'd6', 'f6']) == False:
            inmillP.extend(["b6","d6","f6"])
        if m2 != True and rest != "MILL":
            m2 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b6', 'd6', 'f6']):
        inmillP.remove("b6")
        inmillP.remove("d6")
        inmillP.remove("f6")
    if c5 == "O" and d5 == "O" and e5 == "O":
        if all(x in inmillP for x in ['c5', 'd5', 'e5']) == False:
            inmillP.extend(["c5","d5","e5"])
        if m3 != True and rest != "MILL":
            m3 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c5', 'd5', 'e5']):
        inmillP.remove("c5")
        inmillP.remove("d5")
        inmillP.remove("e5")
    if a4 == "O" and b4 == "O" and c4 == "O":
        if all(x in inmillP for x in ['a4', 'b4', 'c4']) == False:
            inmillP.extend(["a4","b4","c4"])
        if m4 != True and rest != "MILL":
            m4 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a4', 'b4', 'c4']):
        inmillP.remove("a4")
        inmillP.remove("b4")
        inmillP.remove("c4")
    if e4 == "O" and f4 == "O" and g4 == "O":
        if all(x in inmillP for x in ['e4', 'f4', 'g4']) == False:
            inmillP.extend(["e4","f4","g4"])
        if m5 != True and rest != "MILL":
            m5 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e4', 'f4', 'g4']):
        inmillP.remove("e4")
        inmillP.remove("f4")
        inmillP.remove("g4")
    if c3 == "O" and d3 == "O" and e3 == "O":
        if all(x in inmillP for x in ['c3', 'd3', 'e3']) == False:
            inmillP.extend(["c3","d3","e3"])
        if m6 != True and rest != "MILL":
            m6 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'd3', 'e3']):
        inmillP.remove("c3")
        inmillP.remove("d3")
        inmillP.remove("e3")
    if b2 == "O" and d2 == "O" and f2 == "O":
        if all(x in inmillP for x in ['b2', 'd2', 'f2']) == False:
            inmillP.extend(["b2","d2","f2"])
        if m7 != True and rest != "MILL":
            m7 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'd2', 'f2']):
        inmillP.remove("b2")
        inmillP.remove("d2")
        inmillP.remove("f2")
    if a1 == "O" and d1 == "O" and g1 == "O":
        if all(x in inmillP for x in ['a1', 'd1', 'g1']) == False:
            inmillP.extend(["a1","d1","g1"])
        if m8 != True and rest != "MILL":
            m8 = True
            mi4 = True # for strategy
            rest = "MILL"
    elif all(x in inmillP for x in ['a1', 'd1', 'g1']):
        inmillP.remove("a1")
        inmillP.remove("d1")
        inmillP.remove("g1")
    # VERTICALS
    if a7 == "O" and a4 == "O" and a1 == "O":
        if all(x in inmillP for x in ['a7', 'a4', 'a1']) == False:
            inmillP.extend(["a7","a4","a1"])
        if m9 != True and rest != "MILL":
            m9 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['a7', 'a4', 'a1']):
        inmillP.remove("a7")
        inmillP.remove("a4")
        inmillP.remove("a1")
    if b2 == "O" and b4 == "O" and b6 == "O":
        if all(x in inmillP for x in ['b2', 'b4', 'b6']) == False:
            inmillP.extend(["b2","b4","b6"])
        if m10 != True and rest != "MILL":
            m10 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['b2', 'b4', 'b6']):
        inmillP.remove("b2")
        inmillP.remove("b4")
        inmillP.remove("b6")
    if c3 == "O" and c4 == "O" and c5 == "O":
        if all(x in inmillP for x in ['c3', 'c4', 'c5']) == False:
            inmillP.extend(["c3","c4","c5"])
        if m11 != True and rest != "MILL":
            m11 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['c3', 'c4', 'c5']):
        inmillP.remove("c3")
        inmillP.remove("c4")
        inmillP.remove("c5")
    if d1 == "O" and d2 == "O" and d3 == "O":
        if all(x in inmillP for x in ['d1', 'd2', 'd3']) == False:
            inmillP.extend(["d1","d2","d3"])
        if m12 != True and rest != "MILL":
            m12 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d1', 'd2', 'd3']):
        inmillP.remove("d1")
        inmillP.remove("d2")
        inmillP.remove("d3")
    if d7 == "O" and d6 == "O" and d5 == "O":
        if all(x in inmillP for x in ['d7', 'd6', 'd5']) == False:
            inmillP.extend(["d7","d6","d5"])
        if m13 != True and rest != "MILL":
            m13 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['d7', 'd6', 'd5']):
        inmillP.remove("d7")
        inmillP.remove("d6")
        inmillP.remove("d5")
    if e5 == "O" and e4 == "O" and e3 == "O":
        if all(x in inmillP for x in ['e5', 'e4', 'e3']) == False:
            inmillP.extend(["e5","e4","e3"])
        if m14 != True and rest != "MILL":
            m14 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['e5', 'e4', 'e3']):
        inmillP.remove("e5")
        inmillP.remove("e4")
        inmillP.remove("e3")
    if f2 == "O" and f4 == "O" and f6 == "O":
        if all(x in inmillP for x in ['f2', 'f4', 'f6']) == False:
            inmillP.extend(["f2","f4","f6"])
        if m15 != True and rest != "MILL":
            m15 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['f2', 'f4', 'f6']):
        inmillP.remove("f2")
        inmillP.remove("f4")
        inmillP.remove("f6")
    if g1 == "O" and g4 == "O" and g7 == "O":
        if all(x in inmillP for x in ['g1', 'g4', 'g7']) == False:
            inmillP.extend(["g1","g4","g7"])
        if m16 != True and rest != "MILL":
            m16 = True
            rest = "MILL"
    elif all(x in inmillP for x in ['g1', 'g4', 'g7']):
        inmillP.remove("g1")
        inmillP.remove("g4")
        inmillP.remove("g7")
    # OPPONENT'S TURN
    if (
        rest != "MILL" and rest != "ERROR NVM" and
        rest != "ERROR BPL" and rest != "MFNVA" and 
        rest != "MTNVA" and rest != "ERROR BS" and
        rest != "ERROR IE" and rest != "ERRORback" and
        rest != "ERROR INMILL" and phase == "bfly"
        ):
        sx = ("*","X")
        sat = 0
        while sat != 1:
            if sat == 0:
                choose_strategy(thebad)
            use_strategy()
        # STRATEGY END
        # The following code is the
        ## INMILL list handling
        # # It handles the list, so the AI will pay attention to
        # # pieces that are in mill.
        if a7 == "X" and d7 == "X" and g7 == "X":
            if all(x in inmill for x in ['a7', 'd7', 'g7']) == False:
                inmill.extend(["a7","d7","g7"])
            if m21 != True:
                m21 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'd7', 'g7']):
            inmill.remove("a7")
            inmill.remove("d7")
            inmill.remove("g7")
        if b6 == "X" and d6 == "X" and f6 == "X":
            if all(x in inmill for x in ['b6', 'd6', 'f6']) == False:
                inmill.extend(["b6","d6","f6"])
            if m22 != True and rest != "OMILL":
                m22 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b6', 'd6', 'f6']):
            inmill.remove("b6")
            inmill.remove("d6")
            inmill.remove("f6")
        if c5 == "X" and d5 == "X" and e5 == "X":
            if all(x in inmill for x in ['c5', 'd5', 'e5']) == False:
                inmill.extend(["c5","d5","e5"])
            if m23 != True and rest != "OMILL":
                m23 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c5', 'd5', 'e5']):
            inmill.remove("c5")
            inmill.remove("d5")
            inmill.remove("e5")
        if a4 == "X" and b4 == "X" and c4 == "X":
            if all(x in inmill for x in ['a4', 'b4', 'c4']) == False:
                inmill.extend(["a4","b4","c4"])
            if m24 != True and rest != "OMILL":
                m24 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a4', 'b4', 'c4']):
            inmill.remove("a4")
            inmill.remove("b4")
            inmill.remove("c4")
        if e4 == "X" and f4 == "X" and g4 == "X":
            if all(x in inmill for x in ['e4', 'f4', 'g4']) == False:
                inmill.extend(["e4","f4","g4"])
            if m25 != True and rest != "OMILL":
                m25 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e4', 'f4', 'g4']):
            inmill.remove("e4")
            inmill.remove("f4")
            inmill.remove("g4")
        if c3 == "X" and d3 == "X" and e3 == "X":
            if all(x in inmill for x in ['c3', 'd3', 'e3']) == False:
                inmill.extend(["c3","d3","e3"])
            if m26 != True and rest != "OMILL":
                m26 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'd3', 'e3']):
            inmill.remove("c3")
            inmill.remove("d3")
            inmill.remove("e3")
        if b2 == "X" and d2 == "X" and f2 == "X":
            if all(x in inmill for x in ['b2', 'd2', 'f2']) == False:
                inmill.extend(["b2","d2","f2"])
            if m27 != True and rest != "OMILL":
                m27 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'd2', 'f2']):
            inmill.remove("b2")
            inmill.remove("d2")
            inmill.remove("f2")
        if a1 == "X" and d1 == "X" and g1 == "X":
            if all(x in inmill for x in ['a1', 'd1', 'g1']) == False:
                inmill.extend(["a1","d1","g1"])
            if m28 != True and rest != "OMILL":
                m28 = True
                mi4 = True # for strategy
                rest = "OMILL"
        elif all(x in inmill for x in ['a1', 'd1', 'g1']):
            inmill.remove("a1")
            inmill.remove("d1")
            inmill.remove("g1")
        # VERTICALS
        if a7 == "X" and a4 == "X" and a1 == "X":
            if all(x in inmill for x in ['a7', 'a4', 'a1']) == False:
                inmill.extend(["a7","a4","a1"])
            if m29 != True and rest != "OMILL":
                m29 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['a7', 'a4', 'a1']):
            inmill.remove("a7")
            inmill.remove("a4")
            inmill.remove("a1")
        if b2 == "X" and b4 == "X" and b6 == "X":
            if all(x in inmill for x in ['b2', 'b4', 'b6']) == False:
                inmill.extend(["b2","b4","b6"])
            if m210 != True and rest != "OMILL":
                m210 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['b2', 'b4', 'b6']):
            inmill.remove("b2")
            inmill.remove("b4")
            inmill.remove("b6")
        if c3 == "X" and c4 == "X" and c5 == "X":
            if all(x in inmill for x in ['c3', 'c4', 'c5']) == False:
                inmill.extend(["c3","c4","c5"])
            if m211 != True and rest != "OMILL":
                m211 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['c3', 'c4', 'c5']):
            inmill.remove("c3")
            inmill.remove("c4")
            inmill.remove("c5")
        if d1 == "X" and d2 == "X" and d3 == "X":
            if all(x in inmill for x in ['d1', 'd2', 'd3']) == False:
                inmill.extend(["d1","d2","d3"])
            if m212 != True and rest != "OMILL":
                m212 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d1', 'd2', 'd3']):
            inmill.remove("d1")
            inmill.remove("d2")
            inmill.remove("d3")
        if d7 == "X" and d6 == "X" and d5 == "X":
            if all(x in inmill for x in ['d7', 'd6', 'd5']) == False:
                inmill.extend(["d7","d6","d5"])
            if m213 != True and rest != "OMILL":
                m213 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['d7', 'd6', 'd5']):
            inmill.remove("d7")
            inmill.remove("d6")
            inmill.remove("d5")
        if e5 == "X" and e4 == "X" and e3 == "X":
            if all(x in inmill for x in ['e5', 'e4', 'e3']) == False:
                inmill.extend(["e5","e4","e3"])
            if m214 != True and rest != "OMILL":
                m214 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['e5', 'e4', 'e3']):
            inmill.remove("e5")
            inmill.remove("e4")
            inmill.remove("e3")
        if f2 == "X" and f4 == "X" and f6 == "X":
            if all(x in inmill for x in ['f2', 'f4', 'f6']) == False:
                inmill.extend(["f2","f4","f6"])
            if m215 != True and rest != "OMILL":
                m215 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['f2', 'f4', 'f6']):
            inmill.remove("f2")
            inmill.remove("f4")
            inmill.remove("f6")
        if g1 == "X" and g4 == "X" and g7 == "X":
            if all(x in inmill for x in ['g1', 'g4', 'g7']) == False:
                inmill.extend(["g1","g4","g7"])
            if m216 != True and rest != "OMILL":
                m216 = True
                rest = "OMILL"
        elif all(x in inmill for x in ['g1', 'g4', 'g7']):
            inmill.remove("g1")
            inmill.remove("g4")
            inmill.remove("g7")
        if rest == "OMILL":
            pcs-=1
            go = False
            while go != True:
                choice = random.choice(locations)
                while choice in inmillP:
                    choice = random.choice(locations)
                exec("i = " + choice)
                if i == "O":
                    exec(choice + " = '*'")
                    rmvd = choice
                    go = True
                else:
                    continue
        if rest == "OMILL":
            pcs-=1
            go = False
            while go != True: # IMO - better way: 'while i != "O"'
                choice = random.choice(locations)
                while choice in inmillP:
                    choice = random.choice(locations)
                exec("i = " + choice)
                if i == "O":
                    exec(choice + " = '*'")
                    rmvd = choice
                    go = True
                else:
                    continue
while phase == "pwin":
    clear()
    print "                                      a    b    c    d    e    f    g"
    print "                                 7    %s--------------%s--------------%s    7" % (a7, d7, g7) # 7
    print "                                      |              |              |"
    print "                                 6    |    %s---------%s---------%s    |    6" % (b6, d6, f6)  # 6
    print "                                      |    |         |         |    |"
    print "                                 5    |    |    %s----%s----%s    |    |    5" % (c5, d5, e5)  # 5
    print "                                      |    |    |         |    |    |"
    print "                                 4    %s----%s----%s         %s----%s----%s    4" % (a4, b4, c4, e4, f4, g4)  # 4
    print "                                      |    |    |         |    |    |"
    print "                                 3    |    |    %s----%s----%s    |    |    3"  % (c3, d3, e3) # 3
    print "                                      |    |         |         |    |"
    print "                                 2    |    %s---------%s---------%s    |    2" % (b2, d2, f2) # 2
    print "                                      |              |              |"
    print "                                 1    %s--------------%s--------------%s    1" % (a1, d1, g1)  # 1
    print "                                      a    b    c    d    e    f    g"
    print " __    __  __                      __ "
    print "|  \\  |  \\|  \\                    |  \\"
    print "| $$\ | $$ \$$  _______   ______  | $$"
    print "| $$$\| $$|  \ /       \ /      \ | $$"
    print "| $$$$\ $$| $$|  $$$$$$$|  $$$$$$\| $$"
    print "| $$\$$ $$| $$| $$      | $$    $$ \$$"
    print "| $$ \$$$$| $$| $$_____ | $$$$$$$$ __ "
    print "| $$  \$$$| $$ \$$     \ \$$     \|  \\"
    print " \$$   \$$ \$$  \$$$$$$$  \$$$$$$$ \$$"
    print "\nCongratulations! You've beated our AI!"
    print "If you've enjoyed this match, don't forget to play another!"
    print "Choose another difficulty or try the hardest!"
    print "The AI will certainly play another role, with another strategy." 
    print "Thanks for playing!"
    print "\nPress Enter <Return> to exit the game."
    raw_input()
    import sys # if no menu
    sys.exit() # if no menu
while phase == "plose":
    clear()
    print "                                      a    b    c    d    e    f    g"
    print "                                 7    %s--------------%s--------------%s    7" % (a7, d7, g7) # 7
    print "                                      |              |              |"
    print "                                 6    |    %s---------%s---------%s    |    6" % (b6, d6, f6)  # 6
    print "                                      |    |         |         |    |"
    print "                                 5    |    |    %s----%s----%s    |    |    5" % (c5, d5, e5)  # 5
    print "                                      |    |    |         |    |    |"
    print "                                 4    %s----%s----%s         %s----%s----%s    4" % (a4, b4, c4, e4, f4, g4)  # 4
    print "                                      |    |    |         |    |    |"
    print "                                 3    |    |    %s----%s----%s    |    |    3"  % (c3, d3, e3) # 3
    print "                                      |    |         |         |    |"
    print "                                 2    |    %s---------%s---------%s    |    2" % (b2, d2, f2) # 2
    print "                                      |              |              |"
    print "                                 1    %s--------------%s--------------%s    1" % (a1, d1, g1)  # 1
    print "                                      a    b    c    d    e    f    g"
    print "  ______"                                                  
    print " /      \\"                                                
    print "|  $$$$$$\  ______    ______    ______   __    __"            
    print "| $$___\$$ /      \  /      \  /      \ |  \  |  \\"            
    print " \$$    \ |  $$$$$$\|  $$$$$$\|  $$$$$$\| $$  | $$"            
    print " _\$$$$$$\| $$  | $$| $$   \$$| $$   \$$| $$  | $$"            
    print "|  \__| $$| $$__/ $$| $$      | $$      | $$__/ $$"
    print " \$$    $$ \$$    $$| $$      | $$       \$$    $$"
    print "  \$$$$$$   \$$$$$$  \$$       \$$       _\$$$$$$$"
    print "                                        |  \__| $$"      
    print "                                         \$$    $$"           
    print "                                          \$$$$$$"    
    print "\nBut you've lost this match."
    print "Don't worry. That's not an easy AI. This game has been made"
    print "to confirm that there are unbeatable AI's in Mills, too."
    print "Just try it again, with another strategy and try to do the impossible!"
    print "Beat this AI!"
    print "Good luck! ;) And thanks for playing!"
    print "\nPress Enter <Return> to exit the game."
    raw_input()
    import sys # if no menu
    sys.exit() # if no menu    