from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse,Rectangle,Arc
from scipy.interpolate import CubicHermiteSpline
out=Path(__file__).parent/'figures'; out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'normal'})
blue='#1769aa'; orange='#c45716'; green='#16805a'
def save(fig,name):
 fig.savefig(out/name,dpi=150,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(8,4.6));x=np.linspace(.18,10,1200);ax.plot(x,np.log(x)/x,color=blue,lw=2)
ax.axhline(0,color='.5',lw=.8);ax.axvline(0,color='.5',lw=.8);ax.plot([np.e,np.e],[0,1/np.e],'--',color=orange);ax.plot([0,np.e],[1/np.e]*2,'--',color=orange);ax.scatter([np.e],[1/np.e],color=orange,zorder=3);ax.set(xlim=(0,10),ylim=(-1.2,.6),xlabel='x',ylabel='f(x) = ln(x) / x');ax.set_xticks([1,np.e,5,10],['1','e','5','10']);ax.set_yticks([-1,0,1/np.e],['−1','0','1/e']);save(fig,'log-over-x.png')
fig,ax=plt.subplots(figsize=(8,4));xs=np.array([0,1,2,3,4,5.5,7]);ys=np.array([1,3,1.1,4.2,.7,3.5,0]);curve=CubicHermiteSpline(xs,ys,[.3,0,0,0,0,0,-.5]);xx=np.linspace(0,7,1000);ax.plot(xx,curve(xx),color=blue,lw=2);ax.scatter(xs,ys,color='.2');ax.scatter([3,7],[4.2,0],color=orange,zorder=3);ax.annotate('absolute maximum',(3,4.2),xytext=(3.6,4.3),arrowprops={'arrowstyle':'-'});ax.annotate('absolute minimum',(7,0),xytext=(4.7,-.35),arrowprops={'arrowstyle':'-'});ax.set(xlabel='input on a closed interval',ylabel='function value',ylim=(-.7,4.8));ax.set_xticks([0,7],['a','b']);ax.set_yticks([]);save(fig,'candidates.png')
fig,ax=plt.subplots(figsize=(10,4));ax.set_aspect('equal');ax.set_xlim(-.5,10.5);ax.set_ylim(-.4,3.5);ax.axis('off')
ax.plot([0,0],[.5,2.8],color=blue);ax.plot([2,2],[.5,2.8],color=blue);ax.add_patch(Ellipse((1,2.8),2,.42,fill=False,color=blue));ax.add_patch(Arc((1,.5),2,.42,theta1=180,theta2=360,color=blue));ax.add_patch(Arc((1,.5),2,.42,theta1=0,theta2=180,color=blue,ls='--'));ax.plot([1,2],[.5,.5],color=orange);ax.text(1.45,.22,'r',color=orange);ax.annotate('',(-.22,.5),(-.22,2.8),arrowprops={'arrowstyle':'<->'});ax.text(-.45,1.6,'h');ax.text(.5,3.16,'open top');ax.text(.15,-.22,'cylindrical can')
ax.add_patch(Ellipse((4,.8),1.7,1.7,fill=False,color=orange));ax.plot([4,4.85],[.8,.8],color=orange);ax.text(4.25,.95,'r');ax.text(3.25,2.1,'base disk');ax.text(3.5,-.25,r'$\pi r^2$')
ax.add_patch(Rectangle((6,.1),4,2.3,fill=False,color=green));ax.text(6.8,2.9,'wall laid flat');ax.annotate('',(6,2.6),(10,2.6),arrowprops={'arrowstyle':'<->'});ax.text(7.5,2.65,r'$2\pi r$');ax.text(10.15,1.1,'h');ax.text(7.4,1.15,r'$2\pi rh$');ax.text(5.15,1,'+');save(fig,'can-geometry.png')
fig,ax=plt.subplots(figsize=(8,4.5));rr=np.linspace(.2,3.1,1000);ss=np.pi*rr**2+2*np.pi/rr;ax.plot(rr,ss,color=blue,lw=2);ax.scatter([1],[3*np.pi],color=orange,zorder=3);ax.plot([1,1],[0,3*np.pi],'--',color=orange);ax.set(xlim=(0,3.2),ylim=(0,36),xlabel='radius r (length units)',ylabel='surface area S (square units)');ax.set_yticks([0,3*np.pi,6*np.pi,9*np.pi],['0','3π','6π','9π']);ax.set_xticks([0,1,2,3]);ax.text(1.25,5.5,'minimum at r = 1; V = π');ax.annotate('r → 0⁺: S → ∞',(.21,30),xytext=(.6,31),arrowprops={'arrowstyle':'->'});ax.annotate('r → ∞: S → ∞',(3.08,32),xytext=(1.9,27),arrowprops={'arrowstyle':'->'});save(fig,'can-area.png')
fig,(a,b)=plt.subplots(1,2,figsize=(11,4.3),gridspec_kw={'width_ratios':[1,1.05]});a.axis('off');a.set_aspect('equal');a.set_xlim(-.15,1.15);a.set_ylim(-.5,.55);cut=.3;a.plot([0,cut],[.38,.38],color=blue,lw=3);a.plot([cut,1],[.38,.38],color=green,lw=3)
for v,t in [(0,'0'),(cut,'x'),(1,'1')]:a.plot([v,v],[.34,.42],color='.2');a.text(v-.015,.46,t)
a.text(.12,.25,'x',color=blue);a.text(.6,.25,'1 − x',color=green)
a.add_patch(Rectangle((.08,-.06),cut/4,cut/4,fill=False,color=blue,lw=2));a.add_patch(Rectangle((.65,-.06),(1-cut)/4,(1-cut)/4,fill=False,color=green,lw=2));a.text(.035,-.2,'side x/4',color=blue);a.text(.5,-.2,'side (1 − x)/4',color=green);a.text(.06,-.39,'schematic cut shown at x = 0.3')
x=np.linspace(0,1,500);b.plot(x,(x*x+(1-x)**2)/16,color=blue,lw=2);b.scatter([0,.5,1],[1/16,1/32,1/16],color=orange,zorder=3);b.set(xlim=(-.05,1.05),ylim=(0,.075),xlabel='cut x (length units)',ylabel='total area A (square units)');b.set_xticks([0,.5,1],['0','1/2','1']);b.set_yticks([0,1/32,1/16],['0','1/32','1/16']);b.text(.08,.068,'0 ≤ x ≤ 1: endpoints included');fig.tight_layout();save(fig,'wire-and-area.png')
print('Saved five figures')
