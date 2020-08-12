import numpy as np
#import time#####
'''
env=np.array([[np.zeros((3,3)),np.zeros((3,3)),np.zeros((3,3))],
              [np.zeros((3,3)),np.zeros((3,3)),np.zeros((3,3))],
              [np.zeros((3,3)),np.zeros((3,3)),np.zeros((3,3))]])
'''
env=np.random.randn(9,9)-10#np.zeros((9,9))
values=[1,2,3,4,5,6,7,8,9]
rs=[(0,3),(3,6),(6,9)]
cs=[(0,3),(3,6),(6,9)]
def befor_consistent(env,row,col):
    rr=[]
    cc=[]
    for r in rs:
        if row in range(r[0],r[1]):
            rr.append(r)
    for c in cs:
        if col in range(c[0],c[1]):
            cc.append(c)
    return len(set(env[rr[0][0]:rr[0][1],cc[0][0]:cc[0][1]].ravel()))==9
def consistent(env,row,col):
    return len(set(env[row,:9]))==9 and len(set(env[:9,col]))==9 and befor_consistent(env,row,col)
def select_unassigned_variable(env):
    global check
    check=[]
    for i in range(9):
        for j in range(9):
            if env[i,j]<1:
                check.append((i,j))
    if check:
        return check[0]
    return None
select_unassigned_variable(env)
def backtrack(env):
    """Runs backtracking search to find an assignment."""

    # Check if assignment is complete
    if len(check)==1:
        return env
    # Try a new variable
    #time.sleep(5)#####
    #print(env)#####
    var = select_unassigned_variable(env)
    for value in values:
        new_env = env.copy()
        new_env[var] = value
        if consistent(new_env,var[0],var[1]):
            result = backtrack(new_env)
            if result is not None:
                return result
    return None
solution = backtrack(env)
print(solution)
