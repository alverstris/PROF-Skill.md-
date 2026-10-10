from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np
out=Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25/output/figures')
plt.rcParams.update({'font.size':12,'font.weight':'normal','axes.titleweight':'normal','axes.labelweight':'normal','font.family':'DejaVu Sans','savefig.facecolor':'white'})
blue='#2563a6'; orange='#ce7027'; green='#1c7a57'; red='#b84444'; dark='#243442'
def clean(ax):
    ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=11); ax.grid(False)
fig,axs=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
ax=axs[0]; x=np.linspace(0,2,401)
for i in range(1,5):
    ax.add_patch(Rectangle(((i-1)/2,0),.5,(i/2)**2,facecolor=blue,edgecolor=blue,alpha=.18,lw=1.5))
    ax.plot([i/2],[ (i/2)**2 ],'o',color=blue,ms=5)
ax.plot(x,x*x,color=dark,lw=2.3)
ax.set(xlim=(-.08,2.2),ylim=(-.15,4.65),xlabel='$x$',ylabel='$y$',title='Right endpoints: four rectangles')
ax.set_xticks([0,.5,1,1.5,2]);ax.set_yticks([0,1,2,3,4])
ax.text(1.13,3.6,'$y=x^2$',color=dark)
ax.annotate('',xy=(0,.22),xytext=(.5,.22),arrowprops=dict(arrowstyle='<->',color=dark,lw=1))
ax.text(.25,.4,'$\\Delta x$',ha='center')
clean(ax)
ax=axs[1];f=lambda x:1.2+.45*x+.15*np.sin(x);x=np.linspace(0,4,401);ci=2.4
ax.plot(x,f(x),color=dark,lw=2.3)
ax.add_patch(Rectangle((2,0),1,f(ci),facecolor=orange,edgecolor=orange,alpha=.22,lw=2))
ax.plot([ci,ci],[0,f(ci)],'--',color=orange,lw=1.4)
ax.plot([ci],[f(ci)],'o',color=orange,ms=6)
ax.annotate('',xy=(2,.35),xytext=(3,.35),arrowprops=dict(arrowstyle='<->',color=dark,lw=1))
ax.text(2.5,.51,'$\\Delta x$',ha='center')
ax.annotate('$f(c_i)$',xy=(ci,f(ci)),xytext=(.65,2.6),arrowprops=dict(arrowstyle='->',lw=1,color=dark))
ax.text(3.1,3.05,'$y=f(x)$')
ax.set(xlim=(-.12,4.2),ylim=(-.15,3.5),xlabel='$x$',ylabel='$y$',title='Any sample inside its own interval')
ax.set_xticks([0,2,ci,3,4]);ax.set_xticklabels(['$a$','$x_{i-1}$','$c_i$','$x_i$','$b$']);ax.set_yticks([0])
clean(ax)
fig.savefig(out/'rectangle-sums.png',dpi=180);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(11,5.4),layout='constrained')
ax=axs[0]
for side in [4,3,2,1]:
    ax.add_patch(Rectangle((-side/2,-side/2),side,side,fill=False,edgecolor=dark,lw=1.8))
ax.annotate('',xy=(-2,-2.32),xytext=(2,-2.32),arrowprops=dict(arrowstyle='<->',color=dark))
ax.text(0,-2.65,'base side = 4',ha='center')
ax.text(0,0,'top',ha='center',va='center',fontsize=10)
ax.set(xlim=(-2.8,2.8),ylim=(-2.9,2.6),title='Top view: centred square slabs')
ax.set_aspect('equal');ax.axis('off')
ax=axs[1]
for j in range(4):
    side=4-j
    ax.add_patch(Rectangle((-side/2,j),side,1,facecolor='#e8edf2',edgecolor=dark,lw=1.6))
ax.plot([-2,0,2],[0,4,0],color=green,lw=2.5,label='Inner pyramid')
ax.plot([-2.5,0,2.5],[0,5,0],color=red,lw=2.5,label='Outer pyramid')
ax.set(xlim=(-2.9,2.9),ylim=(-.1,5.55),ylabel='height $z$',title='Central vertical section')
ax.set_xticks([-2.5,-2,0,2,2.5]);ax.set_yticks(range(6))
ax.legend(loc='upper right',frameon=False,fontsize=10)
ax.set_aspect('equal');clean(ax)
fig.savefig(out/'staircase-pyramids.png',dpi=180);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(11,4.3),layout='constrained')
ax=axs[0]; x=np.linspace(0,2,301)
ax.fill_between(x,0,x,color=blue,alpha=.17);ax.plot(x,x,color=dark,lw=2.3);ax.plot([2,2],[0,2],color=dark,lw=1.8)
ax.text(1.27,.37,'area = 2',ha='center');ax.text(.7,1.55,'$y=x$')
ax.set(xlim=(-.1,2.2),ylim=(-.1,2.25),xlabel='$x$',ylabel='$y$',title='Triangle: base 2, height 2')
ax.set_xticks([0,1,2]);ax.set_yticks([0,1,2]);clean(ax)
ax=axs[1];y=x-1
ax.fill_between(x,0,y,where=y>=0,color=blue,alpha=.2)
ax.fill_between(x,0,y,where=y<=0,color=orange,alpha=.25)
ax.plot(x,y,color=dark,lw=2.3);ax.axhline(0,color=dark,lw=1)
ax.text(.38,-.64,'−1/2',color=orange);ax.text(1.6,.26,'+1/2',color=blue)
ax.text(.25,.7,'$y=x-1$')
ax.set(xlim=(-.1,2.2),ylim=(-1.15,1.2),xlabel='$x$',ylabel='$y$',title='Signed contributions cancel')
ax.set_xticks([0,1,2]);ax.set_yticks([-1,0,1]);clean(ax)
fig.savefig(out/'areas-and-signs.png',dpi=180);plt.close(fig)
print('Created three complete figure PNGs.')
