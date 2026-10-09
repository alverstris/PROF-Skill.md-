from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Polygon
P=Path(__file__).resolve().parents[1]/'learner'/'figures'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titleweight':'normal','font.weight':'normal'})
blue='#1f5a9c'; orange='#bc5b10'; green='#188263'
fig,axs=plt.subplots(1,2,figsize=(11,4.2),layout='constrained')
x=np.linspace(0,1,300)
for ax in axs:
 ax.plot(x,x*x,color=blue,lw=2.5); ax.set(xlim=(-.03,1.05),ylim=(0,1.12),xlabel='x',ylabel='height'); ax.spines[['top','right']].set_visible(False);ax.set_xticks([0,.25,.5,.75,1]);ax.set_yticks([0,.25,.5,.75,1])
axs[0].fill_between(x,0,x*x,color=blue,alpha=.16);axs[0].set_title('Actual region: y = x² on [0, 1]')
for k in range(1,5):axs[1].add_patch(Rectangle(((k-1)/4,0),.25,(k/4)**2,facecolor=orange,alpha=.18,edgecolor=orange,lw=2));axs[1].plot(k/4,(k/4)**2,'o',color=orange)
axs[1].set_title('Four right-endpoint rectangles')
fig.savefig(P/'rectangles.png',dpi=170);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(11,5.1),layout='constrained')
for k in range(4,0,-1): axs[0].add_patch(Rectangle((-k/2,-k/2),k,k,fill=False,edgecolor='black',lw=1.4))
axs[0].set(xlim=(-2.7,2.7),ylim=(-2.7,2.7),aspect='equal');axs[0].axis('off');axs[0].set_title('Top view: nested square layers (n = 4)');axs[0].text(0,-2.5,'Bottom side 4; each next side is one shorter',ha='center',fontsize=11)
ax=axs[1]
for j in range(4):ax.add_patch(Rectangle((-(4-j)/2,j),4-j,1,facecolor='.9',edgecolor='black',lw=1.2))
ax.plot([-2,0,2],[0,4,0],color=green,lw=2,label='Inner pyramid')
ax.plot([-2.5,0,2.5],[0,5,0],color=orange,lw=2,label='Outer pyramid')
ax.axhline(1.5,color=blue,ls='--',lw=1);ax.text(2.1,1.55,'z = 1.5',color=blue,fontsize=10)
ax.set(xlim=(-2.8,3),ylim=(-.15,5.8),xlabel='horizontal position',ylabel='height z',title='Central side section: thickness 1')
ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False);ax.set_yticks(range(6));ax.legend(loc='upper right',fontsize=9,frameon=False)
fig.savefig(P/'staircase.png',dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(8.5,4.4),layout='constrained')
x=np.linspace(1,3,400);f=lambda x:1+.4*x+.15*x*x
ax.plot(x,f(x),color=blue,lw=2.5);ax.fill_between(x,0,f(x),color=blue,alpha=.07)
a,b=1.8,2.2;c=1.95
ax.add_patch(Rectangle((a,0),b-a,f(c),facecolor=orange,alpha=.25,edgecolor=orange,lw=2));ax.vlines(c,0,f(c),color=orange,ls='--');ax.plot(c,f(c),'o',color=orange)
ax.annotate('',xy=(a,.3),xytext=(b,.3),arrowprops={'arrowstyle':'<->','color':orange});ax.text(2,.4,'Δx',ha='center',color=orange)
ax.text(2.28,f(c)/2,'height f(cᵢ)',color=orange);ax.text(2.55,3.72,'y = f(x)',color=blue)
ax.set_xticks([1,a,c,b,3],['a','xᵢ₋₁','cᵢ','xᵢ','b']);ax.set_yticks([0]);ax.set(xlim=(.9,3.1),ylim=(0,4.1),xlabel='x',ylabel='height');ax.spines[['top','right']].set_visible(False)
fig.savefig(P/'sample-rectangle.png',dpi=170);plt.close(fig)
