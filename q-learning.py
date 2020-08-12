import cv2 as cv
import numpy as np
import random
img=np.ones((300,300,3))*255
cv.putText(img,'start',(20,250),cv.FONT_HERSHEY_SIMPLEX,.5,(255, 0, 0))
cv.putText(img,'goal',(250,20),cv.FONT_HERSHEY_SIMPLEX,.5,(255, 0, 0))
steps={0:img[0:100,0:100,:],1:img[0:100,100:200,:],2:img[0:100,200:300,:],
       3:img[100:200,0:100,:],4:img[100:200,100:200,:],5:img[100:200,200:300,:],
       6:img[200:300,0:100,:],7:img[200:300,100:200,:],8:img[200:300,200:300,:]}
action={0:'l',1:'r',2:'u',3:'d'}
img[100:200,100:200,:]=0
R=np.array([[-1,0,-1,0],
             [0,10,-1,-10],
             [0,-1,-1,0],
             [-1,-10,0,0],
             [0,0,0,0],
             [-10,-1,10,0],
             [-1,0,0,-1],
             [0,0,-10,-1],
             [0,-1,0,-1]])
env=np.array([[0,1,2],
              [3,4,5],
              [6,7,8]])
Q=np.zeros((9,4))
initial_state=6
gamma=0.8
def can_take_action(state):
    total_act=np.where(R[state,]>=0)
    return total_act
total_act_can_take=can_take_action(initial_state)
def choose_one_act(take):
    act=np.random.choice(take[0])
    return act
act=choose_one_act(total_act_can_take)

def next_state(initial_state):
    state_pos=np.where(env==initial_state)
    row,col=state_pos[0][0],state_pos[1][0]
    if action[act]=='u':
        row=row-1
        n_state=env[row][col]
    elif action[act]=='d':
        row=row+1
        n_state=env[row][col]
    elif action[act]=='l':
        col=col-1
        n_state=env[row][col]
    elif action[act]=='r':
        col=col+1
        n_state=env[row][col]
    return n_state
n_state=next_state(initial_state)
def n_acti(n_state):
    total_nact_can_take=can_take_action(n_state)
    return total_nact_can_take
total_nact_can_take=n_acti(n_state)
def update(state,n_state,total_nact_can_take,action,gamma):
    max_q=[]
    for i in range(len(total_nact_can_take[0])):
        get_all_Q=Q[n_state,total_nact_can_take[0][i]]
        max_q.append(get_all_Q)
    Q[state,action]=R[state,action]+gamma*max(max_q)
for i in range(10000):
    a=[0,1,3,5,7,8,6,2]
    initial_state=random.choice(a)
    total_act_can_take=can_take_action(initial_state)
    act=choose_one_act(total_act_can_take)
    n_state=next_state(initial_state)
    total_nact_can_take=n_acti(n_state)
    update(initial_state,n_state,total_nact_can_take,act,gamma)
#
#testing
#
initial_state=5
steps[initial_state][:,:,0]=0
cv.imshow('img',img)
while(1):
    if initial_state==2:
        break
    elif initial_state==4:
        print('hole')
        break
    q_maxim=np.where(Q[initial_state,]==np.max(Q[initial_state,]))[0]
    do=np.random.choice(q_maxim)
    state_pos1=np.where(env==initial_state)
    row1,col1=state_pos1[0][0],state_pos1[1][0]
    if action[do]=='u':
        steps[initial_state][:,:,0]=255
        row1=row1-1
        initial_state=env[row1][col1]
        steps[initial_state][:,:,0]=0
    elif action[do]=='d':
        steps[initial_state][:,:,0]=255
        row1=row1+1
        initial_state=env[row1][col1]
        steps[initial_state][:,:,0]=0
    elif action[do]=='l':
        steps[initial_state][:,:,0]=255
        col1=col1-1
        initial_state=env[row1][col1]
        steps[initial_state][:,:,0]=0
    elif action[do]=='r':
        steps[initial_state][:,:,0]=255
        col1=col1+1
        initial_state=env[row1][col1]
        steps[initial_state][:,:,0]=0
    cv.waitKey(70)
    cv.imshow('img',img)
