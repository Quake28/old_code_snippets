def perfect_Three(d):
    x=100
    for a in range(1,x):
        for b in range(a+1,x):
            for c in range(b+1,x):
                if a!=b and a!=c:
                    if d**3==(a**3 + b**3 + c**3):
                        return True
    return False
    
num=int(input())
print(perfect_Three(num))

def perfectFinder(z):
    x=z
    for a in range(1,x):
        for b in range(a+1,x):
            for c in range(b+1,x):
                if a!=b and a!=c:
                    for d in range(1,x):
                        if d**3==(a**3 + b**3 + c**3):
                            print(a,b,c,d)
perfectFinder(100)
"""
1 6 8 9
2 12 16 18
2 17 40 41
3 4 5 6
3 10 18 19
3 18 24 27
3 36 37 46
4 17 22 25
4 24 32 36
4 34 80 82
5 30 40 45
6 8 10 12
6 20 36 38
6 32 33 41
6 36 48 54
6 72 74 92
7 14 17 20
7 42 56 63
7 54 57 70
8 34 44 50
8 48 64 72
9 12 15 18
9 30 54 57
9 54 72 81
10 60 80 90
11 15 27 29
11 66 88 99
12 16 20 24
12 19 53 54
12 40 72 76
12 51 66 75
12 64 66 82
14 23 70 71
14 28 34 40
15 20 25 30
15 42 49 58
15 50 90 95
16 23 41 44
17 40 86 89
18 19 21 28
18 24 30 36
19 53 90 96
19 60 69 82
20 54 79 87
21 28 35 42
21 42 51 60
21 43 84 88
22 30 54 58
22 51 54 67
24 32 40 48
"""
