from pathlib import Path
import hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
A=Path(__file__).resolve().parent
archive=A.parents[1]/'runtime-recovery/teaching-pending-write-recovery.md'
raw=archive.read_bytes(); text=raw.decode()
figs=A/'figures';figs.mkdir(exist_ok=True)
for name in ['cubic','reciprocal','stationary-inflection','logarithmic']:
 text=text.replace(f'figures/{name}.png',f'figures/{name}-replacement.png')
text=text.replace('The four worked functions follow that lecture; the explanations, plots and Tasks A–C here are newly constructed.','The four worked functions follow that lecture. This recovery revision preserves the earlier draft’s explanations and Tasks A–C, with four newly constructed replacement plots; these are not recovered original images.')
(A/'teaching-r15-recovery-v1.md').write_text(text)
text=text.replace('at least one approach to that line sends the function values without bound.', 'at least one one-sided limit as the input tends to that line is $`+\\infty`$ or $`-\\infty`$. This means all sufficiently nearby inputs on that side have arbitrarily large positive, or arbitrarily large negative, values; isolated unbounded values alone do not establish the asymptote.')
(A/'teaching-r15-recovery-v2.md').write_text(text)
plt.rcParams.update({'font.size':12,'font.weight':'normal','axes.titleweight':'normal','axes.labelweight':'normal','mathtext.default':'regular','figure.dpi':160})
def axes(xlim,ylim):
 fig,ax=plt.subplots(figsize=(8,4.8),layout='constrained')
 ax.set(xlim=xlim,ylim=ylim,xlabel='x',ylabel='y')
 ax.axhline(0,color='#555555',lw=.9);ax.axvline(0,color='#555555',lw=.9)
 ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
 return fig,ax
def save(fig,name):
 fig.savefig(figs/(name+'-replacement.png'));plt.close(fig)
def point(ax,x,y,label,offset):
 ax.plot(x,y,'o',color='black',ms=4)
 ax.annotate(label,(x,y),xytext=offset,textcoords='offset points',fontsize=11,
             bbox={'facecolor':'white','edgecolor':'none','alpha':.85,'pad':1.5})
fig,ax=axes((-2.4,2.4),(-5,5));x=np.linspace(-2.4,2.4,1800)
ax.plot(x,3*x-x**3,color='#006e89',lw=2)
ax.plot([-.0,0],[0,0]);ax.hlines([-2,2],[-1.42,.58],[-.58,1.42],color='#aa6200',linestyle='dashed',lw=1.2)
for xx,yy,label,off in [(-np.sqrt(3),0,r'$(-\sqrt{3},0)$',(-65,12)),(0,0,'(0,0)',(7,-22)),(np.sqrt(3),0,r'$(\sqrt{3},0)$',(6,12)),(-1,-2,'(-1,-2)',(-68,-21)),(1,2,'(1,2)',(5,15))]:point(ax,xx,yy,label,off)
ax.set_title(r'$y=3x-x^3$');save(fig,'cubic')
fig,ax=axes((-4,4),(-4,4))
for x in [np.linspace(-4,-.08,1600),np.linspace(.08,4,1600)]:ax.plot(x,1/x,color='#006e89',lw=2)
ax.text(-3.8,3.35,'Excluded input: x = 0',fontsize=11);ax.set_title(r'$y=1/x$');save(fig,'reciprocal')
fig,ax=axes((-.7,2.7),(-3.5,5.5));x=np.linspace(-.7,2.7,1400)
ax.plot(x,(x-1)**3+1,color='#006e89',lw=2);ax.hlines(1,.25,1.75,color='#aa6200',linestyle='dashed',lw=1.2)
point(ax,1,1,'(1,1): horizontal tangent',(10,-27));point(ax,0,0,'(0,0)',(-55,12));ax.set_title(r'$y=x^3-3x^2+3x$');save(fig,'stationary-inflection')
fig,ax=axes((0,13),(-1.25,.65));x=np.linspace(.05,13,2400)
ax.plot(x,np.log(x)/x,color='#006e89',lw=2)
point(ax,1,0,'(1,0)',(8,-24));point(ax,np.e,1/np.e,r'$(e,1/e)$: maximum',(-35,35));p=np.exp(1.5);point(ax,p,1.5/p,r'$(e^{3/2},3/(2e^{3/2}))$: inflection',(20,10))
ax.text(8,.07,'approaches y = 0 from above',fontsize=10);ax.set_title(r'$y=(\ln x)/x,\quad x>0$');save(fig,'logarithmic')
record={'revision':'r15-recovery-v2','basis_archive':str(archive),'archive_sha256_before':hashlib.sha256(raw).hexdigest(),'archive_sha256_after':hashlib.sha256(archive.read_bytes()).hexdigest(),'historical_pending_write_outcome':'unknown; old workspace absent','original_four_figures':'unavailable; none recovered','original_33_numerical_checks':'not inspected; unavailable','new_figures':[p.name for p in sorted(figs.glob('*.png'))],'changes':['Four figure references point to explicitly named newly plotted replacements.','P045 discloses recovery basis and new replacement-figure provenance.','P018 now requires a one-sided infinite limit; initial recovery-v1 is preserved.'],'no_skill_change':True}
(A/'recovery-provenance.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
