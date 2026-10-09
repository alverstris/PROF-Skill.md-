from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
A=Path(__file__).parent/'assets'
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','font.weight':'normal','axes.titleweight':'normal','svg.fonttype':'none'})
def save(fig,name):
 fig.tight_layout();fig.savefig(A/(name+'.svg'));fig.savefig(A/(name+'.png'),dpi=160);plt.close(fig)
f,ax=plt.subplots(figsize=(7,3.8)); x=np.linspace(-6,6,1001);ax.plot(x,np.exp(-x*x/2),c='#145f9c',lw=2)
ax.set(xlim=(-6,6),ylim=(0,1.08),xlabel='x',ylabel='y');ax.grid(alpha=.25);ax.set_xticks([-6,-4,-2,0,2,4,6]);save(f,'figure-1-gaussian')
f,ax=plt.subplots(figsize=(6,5));x=np.linspace(0,1.55,501);ax.plot(x,x*x,c='#25364a',lw=2,label='Curve: y = x²');x=np.linspace(0,1.55,20);ax.plot(x,x,'--',c='#64748b',label='Ray: y = x');x=np.linspace(.4,1.6,20);ax.plot(x,2*x-1,c='#ba3434',lw=2,label='Tangent: y = 2x − 1');ax.scatter([1],[1],c='black',zorder=4);ax.annotate('(1, 1)',(1,1),xytext=(.55,1.25));ax.axhline(0,c='black',lw=.7);ax.axvline(0,c='black',lw=.7);ax.set(xlim=(-.12,1.75),ylim=(-.15,2.5),xlabel='x',ylabel='y');ax.set_aspect('equal');ax.legend(loc='upper left',fontsize=10);save(f,'figure-2-slopes')
f,ax=plt.subplots(figsize=(7,5.2)); x=np.linspace(-2.7,2.7,1301)
for a in [-1,-.4,.4,1]:ax.plot(x,a*x*x,c='#25364a',lw=1.5,label='Parabolas: y = ax²' if a==-1 else None)
t=np.linspace(0,2*np.pi,1001)
for c in [.4,1.2]: ax.plot(2*np.sqrt(c)*np.cos(t),np.sqrt(2*c)*np.sin(t),c='#078394',lw=2,label='Ellipses: x²/4 + y²/2 = c' if c==.4 else None)
ax.axhline(0,c='black',lw=.7);ax.axvline(0,c='black',lw=.7);ax.set(xlim=(-2.6,2.6),ylim=(-1.9,1.9),xlabel='x',ylabel='y');ax.set_aspect('equal');ax.legend(loc='upper right',fontsize=10);save(f,'figure-3-orthogonal')
