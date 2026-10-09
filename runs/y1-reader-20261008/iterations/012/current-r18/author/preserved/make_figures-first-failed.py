from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
out=Path(__file__).parent/'figures';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','font.weight':'normal','axes.titleweight':'normal','axes.labelweight':'normal'})
blue='#245ca6';red='#bd3a35';gray='#687483';green='#29775c'
def axes(ax):
 ax.axhline(0,color=gray,lw=.8);ax.axvline(0,color=gray,lw=.8);ax.spines[['top','right']].set_visible(False);ax.set_xlabel('x');ax.set_ylabel('y',rotation=0);ax.grid(alpha=.12)
fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained')
for ax,sgn in zip(axs,[1,-1]):
 z=np.linspace(-2.55,2.55,600);ax.plot(z,z*z-3,color='black',label=r'$y=x^2-3$')
 for k,(cur,col) in enumerate([(sgn,red),(sgn*2,blue)]):
  nex=(cur+3/cur)/2; yy=cur*cur-3
  xx=np.linspace(min(cur,nex)-.15,max(cur,nex)+.15,60);ax.plot(xx,yy+2*cur*(xx-cur),color=col,lw=1.8)
  ax.plot([cur,cur],[0,yy],':',color=col);ax.scatter([cur,nex],[yy,0],color=col,s=25,zorder=5)
 ax.set_xlim((.6,2.3) if sgn==1 else (-2.3,-.6));ax.set_ylim(-2.6,2.5);axes(ax)
 ax.set_title('Start at 1' if sgn==1 else 'Start at −1')
 ax.annotate(r'$x_0$',(sgn,0),xytext=(-6,8),textcoords='offset points')
 ax.annotate(r'$x_1$',(sgn*2,0),xytext=(3,-19),textcoords='offset points')
 ax.annotate(r'$x_2$',(sgn*1.75,0),xytext=(-16,8),textcoords='offset points')
 ax.annotate(f'({sgn}, −2)',(sgn,-2),xytext=(8,-14),textcoords='offset points',color=red)
 ax.annotate(f'({sgn*2}, 1)',(sgn*2,1),xytext=(-58,12) if sgn==1 else (8,12),textcoords='offset points',color=blue)
 ax.legend(loc='upper center',frameon=False)
fig.savefig(out/'newton-steps.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(7,4.8),layout='constrained');z=np.linspace(-1.25,1.25,800);ax.plot(z,-z**3+z,color='black',label=r'$h(x)=-x^3+x$');a=-1/np.sqrt(5);b=-a
for cur,col in [(a,red),(b,blue)]:
 nex=-cur;yy=-cur**3+cur;xx=np.linspace(-.75,.75,200);ax.plot(xx,yy+.4*(xx-cur),color=col,lw=1.7);ax.plot([cur,cur],[0,yy],':',color=col);ax.scatter([cur,nex],[yy,0],color=col,s=28,zorder=5)
 ax.annotate('',xy=(nex,0),xytext=(cur,yy),arrowprops={'arrowstyle':'->','color':col,'lw':1.8})
ax.text(a-.03,.04,r'$a=-1/\sqrt5$',ha='right');ax.text(b+.03,-.1,r'$b=1/\sqrt5$',ha='left');axes(ax);ax.set_xlim(-1.25,1.25);ax.set_ylim(-.75,.75);ax.legend(loc='upper right',frameon=False);fig.savefig(out/'newton-cycle.png',dpi=180);plt.close(fig)
def ellipse(a,b,L):
 c=np.array([a,b])/2;dist=np.hypot(a,b);e=np.array([a,b])/dist;perp=np.array([-e[1],e[0]]);theta=np.linspace(0,2*np.pi,700)
 return c[:,None]+L/2*e[:,None]*np.cos(theta)+np.sqrt(L*L-dist*dist)/2*perp[:,None]*np.sin(theta)
a,b,L=8,3,10;D=np.sqrt(L*L-a*a);P=np.array([a/2*(1-b/D),(b-D)/2]);A=np.array([0.,0.]);B=np.array([a,b]);ell=ellipse(a,b,L)
fig,ax=plt.subplots(figsize=(8.4,6),layout='constrained');ax.plot(*ell,color=blue,lw=1.4,label='allowed positions');ax.plot([0,P[0],a],[0,P[1],b],color='black',lw=2);ax.scatter([0,a,P[0]],[0,b,P[1]],color=red,zorder=5)
ax.plot([0,P[0],P[0],a],[0,0,b,b],':',color=gray);ax.plot([P[0],P[0]],[P[1],b+.6],':',color=gray);ax.plot([P[0]-2.4,P[0]+2.4],[P[1],P[1]],'--',color=blue,lw=1)
ax.text(-.4,.25,r'$A=(0,0)$');ax.text(a+.1,b,r'$B=(a,b)$');ax.text(P[0]-.5,P[1]-.45,r'$P=(x,y)$');ax.text(.9,.2,r'$x$');ax.text(4.8,b+.2,r'$a-x$');ax.text(.35,-.95,r'$r_1$');ax.text(5.6,.7,r'$r_2$');
ang=np.degrees(np.arctan(a/D));ax.add_patch(Arc(P,1.2,1.2,theta1=90,theta2=90+ang,color=green));ax.add_patch(Arc(P,1.6,1.6,theta1=90-ang,theta2=90,color=green));ax.text(P[0]-.35,P[1]+.65,r'$\alpha$',color=green);ax.text(P[0]+.28,P[1]+.8,r'$\beta$',color=green)
ax.set_aspect('equal');ax.set_xlabel('horizontal position');ax.set_ylabel('height');ax.set_xlim(-2,10.4);ax.set_ylim(-2.4,6);ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.12);ax.legend(loc='upper left',frameon=False);fig.savefig(out/'ring-geometry.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(8,5.7),layout='constrained');a,b,L=6,2,10;A=np.array([0.,0.]);B=np.array([a,b]);ell=ellipse(a,b,L);P=ell[:,115];u1=(P-A)/np.linalg.norm(P-A);u2=(P-B)/np.linalg.norm(P-B);n=(u1+u2)/np.linalg.norm(u1+u2);t=np.array([-n[1],n[0]])
ax.plot(*ell,color=blue,lw=1.4);ax.plot([*A[:1],P[0],B[0]],[A[1],P[1],B[1]],color=gray,alpha=.5)
for Q,R in [(A,P),(P,B)]:ax.annotate('',xy=R,xytext=Q,arrowprops={'arrowstyle':'->','color':red,'lw':2})
ax.plot([P[0]-2*n[0],P[0]+2*n[0]],[P[1]-2*n[1],P[1]+2*n[1]],'--',color=green,label='local normal');ax.plot([P[0]-2.6*t[0],P[0]+2.6*t[0]],[P[1]-2.6*t[1],P[1]+2.6*t[1]],':',color='black',label='local tangent')
ax.scatter([A[0],B[0],P[0]],[A[1],B[1],P[1]],s=28,color='black',zorder=5);ax.text(-.45,-.1,'A');ax.text(B[0]+.2,B[1]-.2,'B');ax.text(P[0]-.3,P[1]+.28,'P')
ax.set_aspect('equal');ax.set_xlabel('horizontal position');ax.set_ylabel('height');ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.12);ax.legend(loc='lower right',frameon=False);fig.savefig(out/'ellipse-reflection.png',dpi=180);plt.close(fig)
