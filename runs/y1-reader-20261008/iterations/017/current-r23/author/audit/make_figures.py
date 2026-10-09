from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parents[1]/'learner/figures'
plt.rcParams.update({'font.size':12,'font.weight':'normal','axes.labelweight':'normal','axes.titleweight':'normal','figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(8.8,3.8),layout='constrained')
x=np.linspace(0,2*np.pi,801);y=np.sin(x)
ax.plot(x,y,color='#182b42',lw=2)
ax.fill_between(x,0,y,where=x<=np.pi,color='#afd3e8')
ax.fill_between(x,0,y,where=x>=np.pi,color='#f1c29a')
ax.axhline(0,color='#3c444e',lw=.9)
ax.set(xticks=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],xticklabels=['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$'],yticks=[-1,0,1],xlabel='x (radians)',ylabel='y = sin x',xlim=(-.15,2*np.pi+.15),ylim=(-1.3,1.3))
ax.text(np.pi/2,.42,'+2',ha='center',va='center',fontsize=14)
ax.text(3*np.pi/2,-.42,'−2',ha='center',va='center',fontsize=14)
fig.savefig(out/'sine.png',dpi=160);plt.close(fig)
fig,ax=plt.subplots(figsize=(8.8,3.8),layout='constrained')
x=np.linspace(0,2,501);y=1+x*x
ax.plot(x,y,color='#182b42',lw=2)
ax.fill_between(x,0,y,where=x<=1,color='#afd3e8')
ax.fill_between(x,0,y,where=x>=1,color='#f1c29a')
for a in [0,1,2]:ax.plot([a,a],[0,1+a*a],color='#3c444e',lw=1)
ax.axhline(0,color='#3c444e',lw=.9)
ax.set(xticks=[0,1,2],xticklabels=['a = 0','b = 1','c = 2'],yticks=[0,1,2,3,4,5],xlabel='x',ylabel='f(x) = 1 + x²',xlim=(-.15,2.15),ylim=(0,5.6))
ax.text(.5,.55,'first interval',ha='center')
ax.text(1.5,1.4,'second interval',ha='center')
fig.savefig(out/'additivity.png',dpi=160);plt.close(fig)
print('Created two exact function plots; source formulas used, no fitted source sketch.')
