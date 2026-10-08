from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Arc

out=Path(__file__).resolve().parents[1]/'figures'
out.mkdir(exist_ok=True)
theta=0.64  # illustration choice; no numerical angle is asserted in the lesson
O=np.array([0.,0.]); A=np.array([1.,0.]); B=np.array([np.cos(theta),np.sin(theta)])
C=np.array([B[0],0.]); T=np.array([1.,np.tan(theta)])
fig,ax=plt.subplots(figsize=(8.8,5.1),layout='constrained')
ax.add_patch(Polygon([O,A,T],facecolor='#fff0c2',edgecolor='none'))
q=np.linspace(0,theta,200)
ax.fill(np.r_[0,np.cos(q),0],np.r_[0,np.sin(q),0],color='#cddfeb')
ax.add_patch(Polygon([O,A,B],facecolor='#aac7b7',edgecolor='none',alpha=.95))
ax.plot([0,1,1,0],[0,0,T[1],0],color='#3c4652',lw=1.5)
ax.plot(np.cos(q),np.sin(q),color='#245c90',lw=2.6)
ax.plot([0,B[0],1],[0,B[1],0],color='#263b33',lw=1.6)
ax.plot([B[0],B[0]],[0,B[1]],'--',color='#425561',lw=1.3)
ax.add_patch(Arc((0,0),.4,.4,theta1=0,theta2=np.degrees(theta),color='#3c4652'))
ax.text(.24,.07,r'$\theta$',fontsize=15)
for p,s,offset in [(O,'O',(-.04,-.08)),(A,'A',(.025,-.08)),(B,'B',(-.04,.045)),(C,'C',(-.03,-.08)),(T,'T',(.03,.005))]:
    ax.plot(*p,'o',color='#263b33',ms=4);ax.text(p[0]+offset[0],p[1]+offset[1],s,fontsize=14)
ax.text(.37,-.16,r'$OC=\cos\theta$',fontsize=14)
ax.text(.83,-.23,r'$CA=1-\cos\theta$',fontsize=13)
ax.text(.57,.33,r'$OB=1$',rotation=np.degrees(theta),fontsize=14)
ax.text(B[0]-.035,.25,r'$BC=\sin\theta$',ha='right',fontsize=14)
ax.text(1.08,.38,r'$AT=\tan\theta$',fontsize=14)
ax.annotate(r'arc $AB=\theta$',xy=(np.cos(theta*.56),np.sin(theta*.56)),xytext=(1.17,.62),arrowprops=dict(arrowstyle='-',color='#245c90'),color='#245c90',fontsize=14)
ax.text(.02,.97,'Inner triangle OAB ⊂ sector OAB ⊂ outer triangle OAT',fontsize=14)
ax.text(.02,.89,r'$OA=1,\quad 0<\theta<\pi/2$ (radians)',fontsize=13)
ax.set(xlim=(-.09,1.69),ylim=(-.29,1.02),aspect='equal');ax.axis('off')
fig.savefig(out/'unit-circle-proof-v1.png',dpi=170,facecolor='white')
