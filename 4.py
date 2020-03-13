def is_pal(x):
    if x == int(str(x)[::-1]):
        return True
    return False

def solve():
    a = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if is_pal(i*j):
                a.append(i*j)
    print(max(a))
    

solve()
        
    
