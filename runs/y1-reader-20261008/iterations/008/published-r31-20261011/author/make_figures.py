from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'font.weight':'normal','axes.titleweight':'normal','axes.labelweight':'normal','mathtext.default':'regular','figure.facecolor':'white','savefig.facecolor':'white'})
out=Path('teaching/figures');out.mkdir(exist_ok=True,parents=True)
blue='#145da0';orange='#c45111';green='#16826b'
def style(ax):
 ax.grid(alpha=.22);ax.spines[['top','right']].set_visible(False);ax.set_xlabel('x');ax.set_ylabel('y',rotation=0,labelpad=14)
x=np.linspace(.4,1.8,500);fig,ax=plt.subplots(figsize=(8,4.5),layout='constrained');ax.plot(x,np.log(x),color=blue,label='ln x',lw=2.3);ax.plot(x,x-1,color=orange,ls='--',label='tangent: x − 1',lw=2);ax.scatter([1],[0],color='black',zorder=5);ax.annotate('base point (1, 0)',(1,0),(.57,.26),arrowprops={'arrowstyle':'->'},fontsize=12);style(ax);ax.set_xlim(.4,1.8);ax.set_ylim(-1,.8);ax.legend(loc='lower right',frameon=False);fig.savefig(out/'tangent.png',dpi=160);plt.close(fig)
x=np.linspace(-2,2,500);fig,axs=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
for ax,y,l,title in [(axs[0],np.sin(x),x,'Sine at zero'),(axs[1],np.cos(x),np.ones_like(x),'Cosine at zero')]:
 ax.plot(x,y,color=blue,lw=2.3,label='curve');ax.plot(x,l,color=orange,ls='--',lw=2,label='tangent');style(ax);ax.set_title(title);ax.axhline(0,color='black',lw=.7);ax.axvline(0,color='black',lw=.7);ax.set_xlim(-2,2)
axs[0].set_ylim(-2.2,2.2);axs[0].legend(frameon=False);axs[1].set_ylim(-.65,1.2);axs[1].legend(frameon=True,facecolor='white',edgecolor='white',framealpha=1,loc='lower center');fig.savefig(out/'basic-tangents.png',dpi=160);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,3.9),layout='constrained');ax.set_xlim(0,10);ax.set_ylim(0,4);ax.axis('off');ax.hlines(1,0.5,9.5,color='#59646f',lw=2);ax.text(5,.58,'Reference-frame clocks are synchronized and at rest.',ha='center');ax.scatter([2,8],[2.35,2.35],s=160,color=blue);ax.annotate('',(7.65,2.35),(2.35,2.35),arrowprops={'arrowstyle':'->','lw':2,'color':blue});ax.text(5,2.65,'constant speed v',ha='center',color=blue);ax.text(2,3.5,'First tick',ha='center');ax.text(8,3.5,'Second tick',ha='center');ax.text(5,3.12,'Same moving clock; elapsed onboard time T',ha='center');ax.vlines([2,8],1,2.1,color='gray',linestyle='dotted');ax.text(2.2,1.3,'t₁',ha='left');ax.text(8.2,1.3,'t₂',ha='left');ax.text(5,.12,'Reference elapsed time: T′ = t₂ − t₁',ha='center');fig.savefig(out/'clock-model.png',dpi=160);plt.close(fig)
x=np.linspace(-2.4,2.4,600);fig,ax=plt.subplots(figsize=(8,4.7),layout='constrained');ax.plot(x,np.cos(x),color=blue,lw=2.5,label='cos x');ax.plot(x,np.ones_like(x),color='#797979',ls=':',lw=2,label='linear: 1');ax.plot(x,1-x*x/2,color=orange,ls='--',lw=2,label='quadratic: 1 − x²/2');style(ax);ax.set_xlim(-2.4,2.4);ax.set_ylim(-2,1.45);ax.axhline(0,color='black',lw=.7);ax.scatter([0],[1],color='black',zorder=5);ax.legend(frameon=False,loc='lower center');fig.savefig(out/'cosine-quadratic.png',dpi=160);plt.close(fig)
