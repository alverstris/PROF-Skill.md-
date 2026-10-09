from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
out=Path(__file__).parent/'figures';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'font.weight':'normal','axes.titleweight':'normal','axes.labelweight':'normal','savefig.facecolor':'white'})
def frame():
 f,a=plt.subplots(figsize=(7.6,4.5),layout='constrained');a.spines[['top','right']].set_visible(False);a.set_xlabel('input x');a.set_ylabel('output y');return f,a
def save(f,n):
 f.savefig(out/(n+'.png'),dpi=170);f.savefig(out/(n+'.svg'));plt.close(f)
f,a=frame();x=np.linspace(.8,3.2,400);a.plot(x,x*x,color='#222222',label='curve: y = x²');a.plot(x,4*x-3,color='#295bb5',label='secant: y = 4x − 3');a.plot(x,4*x-4,color='#ad342b',label='tangent: y = 4x − 4');a.plot(x,4*x-4.7,'--',color='#888888',label='parallel line below contact');a.scatter([1,2,3],[1,4,9],color='#222222',zorder=4);a.annotate('a = 1',(1,1),xytext=(.87,1.6));a.annotate('c = 2',(2,4),xytext=(2.08,2.85));a.annotate('b = 3',(3,9),xytext=(2.6,9.7));a.annotate('',xy=(2,4),xytext=(2,3.3),arrowprops={'arrowstyle':'->','color':'#888888'});a.set_xlim(.8,3.2);a.set_ylim(-1,10.5);a.legend(loc='upper left',fontsize=10,frameon=False);save(f,'figure-1-parallel-lines')
f,a=frame();x=np.linspace(-1.25,2.25,400);a.plot(x,abs(x),color='#222222',label='curve: y = |x|');a.plot(x,x/3+4/3,color='#295bb5',label='secant slope = 1/3');a.plot(x,x/3,color='#ad342b',label='first contact from below');a.plot(x,x/3-.45,'--',color='#888888',label='parallel line below contact');a.scatter([-1,0,2],[1,0,2],color='#222222',zorder=4);a.annotate('corner: no derivative',(0,0),xytext=(.3,-.58),arrowprops={'arrowstyle':'->','color':'#222222'});a.annotate('',xy=(-.25,-.25/3),xytext=(-.25,-.25/3-.45),arrowprops={'arrowstyle':'->','color':'#888888'});a.set_xlim(-1.3,2.3);a.set_ylim(-.9,3.4);a.legend(loc='upper left',fontsize=10,frameon=False);save(f,'figure-2-corner')
f,a=frame();x=np.linspace(.7,2.2,400);a.plot(x,x*x,color='#222222',label='curve: y = x²');a.plot(x,2*x-1,color='#295bb5',label='tangent at a = 1: L(x) = 2x − 1');a.scatter([1,2,2],[1,4,3],color='#222222',zorder=4);a.vlines(2,3,4,color='#ad342b',linewidth=2);a.annotate('signed error = 1',(2,3.5),xytext=(1.28,4.5),arrowprops={'arrowstyle':'->','color':'#ad342b'});a.annotate('(1,1)',(1,1),xytext=(1.07,.7));a.annotate('(2,4)',(2,4),xytext=(2.03,3.98));a.annotate('(2,3)',(2,3),xytext=(2.03,2.9));a.set_xlim(.7,2.3);a.set_ylim(.3,5.9);a.legend(loc='upper left',fontsize=10,frameon=False);save(f,'figure-3-tangent-error')
