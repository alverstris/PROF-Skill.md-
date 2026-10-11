from pathlib import Path
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import erf
out=Path('output/figures');out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','font.weight':'normal','axes.labelweight':'normal'})
f=lambda t:1+.55*t-.045*t*t
fig,ax=plt.subplots(figsize=(8.4,4.6),layout='constrained')
t=np.linspace(0,3.3,300);ax.plot(t,f(t),color='#193e60',lw=2)
a=.3;x=2.05;h=.6
for l,r,c in [(a,x,'#bad5e5'),(x,x+h,'#eaa35b')]:
 z=np.linspace(l,r,150);ax.fill_between(z,0,f(z),color=c,alpha=.75);ax.vlines([l,r],0,[f(l),f(r)],color='#555555',lw=.8)
ax.hlines(f(x),x,x+h,colors='#884611',linestyles='dashed');ax.text(1.02,.62,'F(x)',ha='center');ax.text(x+h/2,.62,'ΔF',ha='center');ax.text(2.84,2.07,'f(t)',ha='left');ax.annotate('rectangle height f(x)',xy=(2.35,f(x)),xytext=(1.3,2.55),arrowprops={'arrowstyle':'->','color':'#555555'},ha='center')
ax.set_xticks([a,x,x+h],['a','x','x + h']);ax.set_yticks([0]);ax.set_xlim(-.1,3.4);ax.set_ylim(0,2.9);ax.set_xlabel('t');ax.set_ylabel('height');ax.spines[['top','right']].set_visible(False);fig.savefig(out/'accumulation-strip.png',dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(8.4,4.6),layout='constrained')
x=np.linspace(-3,3,500);ax.plot(x,[erf(v) for v in x],color='#193e60',lw=2);ax.axhline(0,color='#777',lw=.7);ax.axvline(0,color='#777',lw=.7)
for y in [-1,1]:ax.axhline(y,color='#a66a24',lw=1,linestyle='--')
ax.set_xticks([-3,-2,-1,0,1,2,3]);ax.set_yticks([-1,0,1]);ax.set_xlim(-3.2,3.2);ax.set_ylim(-1.2,1.2);ax.set_xlabel('x');ax.set_ylabel('erf(x)');ax.spines[['top','right']].set_visible(False);ax.text(1.75,.78,'approaches 1',ha='center');ax.text(-1.75,-.78,'approaches −1',ha='center');fig.savefig(out/'error-function.png',dpi=170);plt.close(fig)
print('Saved both exact lesson figures')
