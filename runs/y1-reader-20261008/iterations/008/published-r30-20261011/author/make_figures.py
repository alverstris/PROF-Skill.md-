from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
out=Path('teaching/figures');out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':13,'axes.titlesize':15,'axes.labelsize':13,'font.weight':'normal','axes.titleweight':'normal','figure.facecolor':'white','savefig.facecolor':'white'})
def style(ax):
 ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.18);ax.set_xlabel('x');ax.set_ylabel('y',rotation=0,labelpad=12)
fig,ax=plt.subplots(figsize=(8.3,4.9),layout='constrained');x=np.linspace(.35,1.9,400)
ax.plot(x,np.log(x),color='#16745a',lw=2.8,label='f(x) = ln(x)');ax.plot(x,x-1,'--',color='#b24828',lw=2.3,label='L(x) = x - 1');ax.scatter([1],[0],c='black',zorder=4);ax.annotate('basepoint (1, 0)',(1,0),xytext=(1.18,-.62),arrowprops={'arrowstyle':'->'});ax.set_title('Same value and slope at the basepoint');style(ax);ax.legend(loc='upper left',frameon=False);fig.savefig(out/'tangent.png',dpi=170);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(11.4,4.8),layout='constrained');x=np.linspace(-1.8,1.8,500)
axs[0].plot(x,np.sin(x),lw=2.8,color='#16745a',label='sin(x)');axs[0].plot(x,x,'--',lw=2.2,color='#b24828',label='L(x) = Q(x) = x');axs[0].set_title('Sine: zero quadratic coefficient');axs[0].set_ylim(-1.85,1.85)
axs[1].plot(x,np.cos(x),lw=2.8,color='#16745a',label='cos(x)');axs[1].plot(x,np.ones_like(x),'--',lw=2.2,color='#b24828',label='L(x) = 1');axs[1].plot(x,1-x*x/2,':',lw=3,color='#314da5',label='Q(x) = 1 - x²/2');axs[1].set_title('Cosine: curvature changes the model');axs[1].set_ylim(-.85,1.25)
for ax in axs:style(ax);ax.scatter([0],[0 if ax is axs[0] else 1],c='black',zorder=4);ax.legend(loc='lower center',frameon=False)
fig.savefig(out/'sine-cosine.png',dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(10.5,4.3),layout='constrained');ax.set_xlim(0,10);ax.set_ylim(0,4);ax.axis('off')
ax.plot([.5,9.5],[.9,.9],color='#606060');ax.text(5,.45,'Stationary reference frame: coordinate interval T′',ha='center')
for x,lab in [(1.8,'Event A: first tick'),(7.6,'Event B: later tick')]:
 ax.add_patch(Circle((x,2.15),.22,fc='#cee4ef',ec='#154560',lw=2));ax.text(x,1.55,lab,ha='center')
ax.annotate('',xy=(7.3,2.15),xytext=(2.15,2.15),arrowprops={'arrowstyle':'->','lw':2,'color':'#154560'});ax.text(4.7,2.52,'Same moving clock; constant speed v',ha='center');ax.text(5,3.38,'Clock carries elapsed time T from event A to event B',ha='center');fig.savefig(out/'clock-model.png',dpi=170);plt.close(fig)
print('Three PNG figures generated.')
