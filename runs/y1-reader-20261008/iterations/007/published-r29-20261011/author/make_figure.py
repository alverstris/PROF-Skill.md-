from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titleweight':'normal','axes.labelweight':'normal','font.weight':'normal'})
fig,ax=plt.subplots(1,2,figsize=(10.8,4.8),layout='constrained')
t=np.linspace(-np.pi,np.pi,500)
a=ax[0];a.plot(np.cos(t),np.sin(t),color='#174E78',lw=2.5);a.scatter([1,0],[0,1],color='#174E78',zorder=3)
a.annotate('x = 0: (1, 0)',(1,0),xytext=(0.1,-1.3),arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=11)
a.annotate('x = π/2: (0, 1)',(0,1),xytext=(-1.5,1.4),arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=11)
a.set_title('u = cos x, v = sin x',pad=10);a.set_xlim(-1.7,1.7);a.set_ylim(-1.6,1.7);a.set_xticks([-1,0,1]);a.set_yticks([-1,0,1])
a=ax[1];t=np.linspace(-1.55,1.55,500);a.plot(np.cosh(t),np.sinh(t),color='#B34913',lw=2.5);a.plot(-np.cosh(t),np.sinh(t),color='#777777',lw=1.6,ls='--')
a.scatter([1,1.25,1.25],[0,.75,-.75],color='#B34913',zorder=3)
a.annotate('x = 0: (1, 0)',(1,0),xytext=(-.5,-.45),arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=10)
a.annotate('x = ln 2: (1.25, 0.75)',(1.25,.75),xytext=(-1.9,1.6),arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=10)
a.annotate('x = −ln 2: (1.25, −0.75)',(1.25,-.75),xytext=(-2.4,-1.85),arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=10)
a.text(-2.45,.2,'Untraced\nleft branch',color='#555555',fontsize=10)
a.set_title('u = cosh x, v = sinh x',pad=10);a.set_xlim(-2.65,2.65);a.set_ylim(-2.2,2.2);a.set_xticks([-2,-1,0,1,2]);a.set_yticks([-2,-1,0,1,2])
for a in ax:
 a.axhline(0,lw=.7,color='#777777',zorder=0);a.axvline(0,lw=.7,color='#777777',zorder=0);a.set_xlabel('u');a.set_ylabel('v',rotation=0,labelpad=10);a.set_aspect('equal');a.spines[['top','right']].set_visible(False);a.grid(alpha=.15)
p=Path('teaching/figures/circle-hyperbola.png');fig.savefig(p,dpi=160,facecolor='white');print(p)
