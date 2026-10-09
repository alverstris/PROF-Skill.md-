from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np
out=Path(__file__).parent/'figures';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':12,'font.weight':'normal','axes.titleweight':'normal','axes.labelweight':'normal','figure.dpi':160})
blue='#235789';green='#18845d';orange='#b65d16'
def tidy(ax):
 ax.spines[['top','right']].set_visible(False); ax.set_xlabel('x');ax.set_ylabel('height',rotation=90);ax.grid(alpha=.12)
def save(fig,name):
 fig.tight_layout();fig.savefig(out/name,bbox_inches='tight',facecolor='white');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,4))
x=np.linspace(0,2,301)
for ax,right,title in zip(axs,[False,True],['Left heights: lower rectangles','Right heights: upper rectangles']):
 for k in range(4):
  h=((k+int(right))*.5)**2;ax.add_patch(Rectangle((k*.5,0),.5,h,facecolor=green if not right else orange,alpha=.25,edgecolor='black'))
 ax.plot(x,x*x,color=blue,lw=2);ax.set_xlim(0,2.12);ax.set_ylim(0,4.4);ax.set_xticks(np.arange(0,2.1,.5));ax.set_title(title);tidy(ax)
save(fig,'rectangles.png')
fig,axs=plt.subplots(1,2,figsize=(10,4.5));a,b=axs
for s in [4,3,2,1]:a.add_patch(Rectangle((-s/2,-s/2),s,s,fill=False,color='black'))
a.set_aspect('equal');a.set_xlim(-2.65,2.65);a.set_ylim(-2.65,2.65);a.set_title('Top view: square slabs');a.set_xlabel('horizontal coordinate');a.set_ylabel('horizontal coordinate')
for k,s in enumerate([4,3,2,1]): b.add_patch(Rectangle((-s/2,k),s,1,facecolor='#cccccc',edgecolor='black',alpha=.65))
b.plot([-2,0,2],[0,4,0],color=green,lw=2,label='Inner: side 4, height 4')
b.plot([-2.5,0,2.5],[0,5,0],color=orange,lw=2,label='Outer: side 5, height 5')
b.set_xlim(-2.8,2.8);b.set_ylim(-.1,5.5);b.set_yticks(range(6));b.set_xlabel('horizontal coordinate');b.set_ylabel('height z');b.set_title('Central side view, n = 4');b.legend(fontsize=9,loc='upper center',bbox_to_anchor=(.5,-.21));b.set_aspect('equal');b.grid(alpha=.12)
save(fig,'pyramids.png')
fig,axs=plt.subplots(1,2,figsize=(10,4));a,b=axs
x=np.linspace(0,2,201);a.fill_between(x,0,x,color=blue,alpha=.2);a.plot(x,x,color=blue,lw=2);a.plot([2,2],[0,2],color=blue);a.set_xlim(0,2.4);a.set_ylim(0,2.4);a.set_xticks([0,2],['0','b']);a.set_yticks([0,2],['0','b']);a.set_title('Line: triangle area = b²/2');tidy(a)
x=np.linspace(0,2.4,301);b.plot(x,x*x/2+.5,color=blue,lw=2)
xx=np.linspace(1.5,2,100);b.fill_between(xx,0,xx*xx/2+.5,color=orange,alpha=.3)
b.add_patch(Rectangle((1.5,0),.5,1.625,fill=False,color=green,lw=1.6));b.add_patch(Rectangle((1.5,0),.5,2.5,fill=False,color=orange,lw=1.6))
b.set_xticks([0,1.5,2],['0','b','b + h']);b.set_yticks([1.625,2.5],['f(b)','f(b + h)']);b.set_xlim(0,2.4);b.set_ylim(0,3.6);b.set_title('Added strip: h > 0');tidy(b)
save(fig,'endpoint.png')
fig,ax=plt.subplots(figsize=(7,4));x=np.linspace(0,4,400);f=lambda x:1+np.sqrt(x+.2);ax.plot(x,f(x),color=blue,lw=2)
l,r,c=1.3,2.5,1.7;ax.add_patch(Rectangle((l,0),r-l,f(c),facecolor=orange,edgecolor=orange,alpha=.3));ax.plot([c,c],[0,f(c)],ls='--',color='black');ax.scatter([c],[f(c)],color='black',s=25);ax.set_xticks([0,l,c,r,4],['a','xᵢ₋₁','cᵢ','xᵢ','b']);ax.set_yticks([0,f(c)],['0','f(cᵢ)']);ax.annotate('',xy=(l,.35),xytext=(r,.35),arrowprops={'arrowstyle':'<->'});ax.text((l+r)/2,.47,'Δx',ha='center');ax.set_ylim(0,3.7);ax.set_xlim(-.1,4.1);ax.set_title('One tagged rectangle');tidy(ax)
save(fig,'tag.png')
