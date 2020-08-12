import numpy as np
import cv2 as cv
import pandas as pd
np.set_printoptions(threshold=np.inf)
def Q_learning():
    nsp=np.arange(0,2500)
    def total_no_action(R,sp):
        R=np.array(R)
        total_action_id=np.where(R[sp,]>=0)
        oneaction=np.random.choice(total_action_id[0])
        return oneaction,total_action_id[0]
    action,_=total_no_action(R,sp)
    def n_state(sp):
        if action==0:
            p=sp-1
            new_state=p
        elif action==1:
            p=sp+1
            new_state=p
        elif action==2:
            p=sp-50
            new_state=p
        elif action==3:
            p=sp+50
            new_state=p
        return new_state
    nw_state=n_state(sp)
    _,nw_actions=total_no_action(R,nw_state)
    def Q_update(R,sp,action,nw_state,nw_actions):
        R=np.array(R)
        max_q=[]
        for i in range(len(nw_actions)):
            get_all_Q=Q[nw_state,nw_actions[i]]
            max_q.append(get_all_Q)
        Q[sp,action]=R[sp,action]+0.8*max(max_q)
    Q_update(R,sp,action,nw_state,nw_actions)
    for i in range(1000):
        #nsp=np.arange(0,2500)
        #nsp=np.delete(nsp,np.where(nsp==49))
        #nsp=np.delete(nsp,np.where(nsp==2499))
        #nsp=np.delete(nsp,np.where(nsp==2490))
        #nsp=np.delete(nsp,np.where(nsp==0))
        #n_sp=np.random.choice(nsp)
        a12=np.arange(0,2500)
        a12=a12.reshape(50,50)
        rs,cs=np.where(a12==sp)
        rf,cf=np.where(a12==fp)
        if rs==rf or cs==cf:
            rs,cs=np.where(a12==53)
            rf,cf=np.where(a12==2447)
        r=[rs,rf]
        c=[cs,cf]
        f=a12[min(r)[0]:(max(r)+1)[0],min(c)[0]:(max(c)+1)[0]]
        nsp=f.ravel()
        n_sp=np.random.choice(nsp)
        action,_=total_no_action(R,n_sp)
        nw_state=n_state(n_sp)
        _,nw_actions=total_no_action(R,nw_state)
        Q_update(R,n_sp,action,nw_state,nw_actions)
        #print(i)
img=np.zeros((500,500,3))
i=0
step_dict={}
action_dict={0:'l',1:'r',2:'u',3:'d'}
for r in range(0,500,10):
    for c in range(0,500,10):
        step_dict.update({i:img[r:r+10,c:c+10,:]})
        i=i+1
env=np.arange(0,2500).reshape((50,50))
R=pd.read_csv('reward1.csv')
Q=np.zeros((2500,4))
'''for i in range(1,49):
    R[i][0]=-10
    R[i][1]=-10
    R[i][2]=-10
    R[i][3]=0
for i in range(2401,2499):
    R[i][0]=-10
    R[i][1]=-10
    R[i][2]=0
    R[i][3]=-10'''
f_pos=np.arange(0,2500)
for i  in range(0,2500,50):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
for i  in range(0,50):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
for i  in range(49,2500,50):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
for i  in range(2450,2500):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
for i  in range(266,666,50):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
for i  in range(240,640,50):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
for i  in range(975,1275,50):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
for i  in range(2116,2140):
    f_pos=np.delete(f_pos,np.where(f_pos==i))
sp=np.random.choice(f_pos)
step_dict[sp][:,:,1]=255
fp=np.random.choice(f_pos)
while True:
    for i in range(0,2500,50):
        step_dict[i][:,:,0]=255
    for i in range(0,50):
        step_dict[i][:,:,0]=255
    for i in range(49,2500,50):
        step_dict[i][:,:,0]=255
    for i in range(2450,2500):
        step_dict[i][:,:,0]=255
    for i in range(266,666,50):
        step_dict[i][:,:,0]=255
    for i in range(240,640,50):
        step_dict[i][:,:,0]=255
    for i in range(975,1275,50):
        step_dict[i][:,:,0]=255
    for i in range(2116,2140):
        step_dict[i][:,:,0]=255
    cv.imshow('img',img)
    key=cv.waitKey(1)
    step_dict[fp][:,:,2]=255
    a,b,c=step_dict[sp][0,0,:]
    lf=fp-1
    rf=fp+1
    uf=fp-50
    df=fp+50
    afl,bfl,cfl=step_dict[lf][0,0,:]
    afr,bfr,cfr=step_dict[rf][0,0,:]
    afu,bfu,cfu=step_dict[uf][0,0,:]
    afd,bfd,cfd=step_dict[df][0,0,:]
    if afl==255:
        pass
    elif afl==0 or bfl==255:
        R.loc[lf,'1']=10
    if afr==255:
        pass
    elif afr==0 or bfr==255:
        R.loc[rf,'0']=10
    if afu==255:
        pass
    elif afu==0 or bfu==255:
        R.loc[uf,'3']=10
    if afd==255:
        pass
    elif afd==0 or bfd==255:
        R.loc[df,'2']=10
    Q_learning()
    '''l=sp-1
    r=sp+1
    u=sp-50
    d=sp+50
    al,bl,cl=step_dict[l][0,0,:]
    ar,br,cr=step_dict[r][0,0,:]
    au,bu,cu=step_dict[u][0,0,:]
    ad,bd,cd=step_dict[d][0,0,:]
    if al==255:
        R[sp][0]=-10
    elif al==0:
        print('l0')
    if ar==255:
        R[sp][1]=-10
    elif ar==0:
        print('r0')
    if au==255:
        R[sp][2]=-10
    elif au==0:
        print('u0')
    if ad==255:
        R[sp][3]=-10
    elif ad==0:
        print('d0')'''
    #
    #testing
    #
    def test():
        #Q=pd.read_csv('Qvalue.csv')
        #Q=np.array(Q)
        act_can_do=np.where(Q[sp,]==np.max(Q[sp,]))
        act=act_can_do[0]
        if len(act_can_do[0])>1:
            act=np.random.choice(act_can_do[0])
        return act
    act=test()
    if a==b:
        print('loss')
    if sp==fp:
        step_dict[fp][:,:,2]=0
        fp=np.random.choice(f_pos)
        R=pd.read_csv('reward1.csv')
        Q=np.zeros((2500,4))
        print('good')
    if act==2:#key==ord('w'):
        step_dict[sp][:,:,:]=0
        step_dict[sp-50][:,:,1]=255
        sp=sp-50
    elif act==3:#key==ord('s'):
        step_dict[sp][:,:,:]=0
        step_dict[sp+50][:,:,1]=255
        sp=sp+50
    elif act==0:#key==ord('a'):
        step_dict[sp][:,:,:]=0
        step_dict[sp-1][:,:,1]=255
        sp=sp-1
    elif act==1:#key==ord('d'):
        step_dict[sp][:,:,:]=0
        step_dict[sp+1][:,:,1]=255
        sp=sp+1
    if key==27:
        break
cv.destroyAllWindows()
