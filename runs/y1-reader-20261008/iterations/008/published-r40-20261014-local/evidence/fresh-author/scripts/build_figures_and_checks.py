from pathlib import Path
import os, sys, json, hashlib, math
from decimal import Decimal, localcontext

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'cache'
CACHE.mkdir(exist_ok=True)
os.environ['MPLCONFIGDIR'] = str(CACHE / 'matplotlib')
os.environ['TEMP'] = str(CACHE)
os.environ['TMP'] = str(CACHE)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import PIL
from PIL import Image
from pypdf import PdfReader

FIG = ROOT / 'teaching' / 'figures'
FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':13, 'axes.titlesize':15,
                     'axes.titleweight':'normal', 'axes.labelsize':13, 'legend.fontsize':12})
blue, orange, green = '#215c9e', '#ba5125', '#36825d'

def axes_common(ax):
    ax.axhline(0, color='#777777', linewidth=.8)
    ax.axvline(0, color='#777777', linewidth=.8)
    ax.grid(alpha=.2)
    ax.set_xlabel('x')
    ax.set_ylabel('y', rotation=0, labelpad=12)

fig, ax = plt.subplots(figsize=(9,5.4), dpi=150, layout='constrained')
x = np.linspace(.35,1.9,500)
ax.plot(x,np.log(x),color=blue,label=r'$y=\ln x$',linewidth=2.2)
ax.plot(x,x-1,color=orange,linestyle='--',label=r'$y=x-1$',linewidth=2)
ax.scatter([1],[0],color='#222222',zorder=5)
ax.annotate('Shared point (1, 0) and slope 1',xy=(1,0),xytext=(.55,.55),
            arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=12)
ax.set_title('A tangent supplies a local line')
axes_common(ax)
ax.set_xlim(.3,1.95); ax.set_ylim(-1.2,.9)
ax.legend(loc='lower right')
fig.savefig(FIG/'log-tangent.png'); plt.close(fig)

fig, axs = plt.subplots(1,2,figsize=(10.4,4.6),dpi=150,layout='constrained')
x = np.linspace(-2.5,2.5,500)
for ax, y, model, lab, modellab, title in zip(axs,[np.sin(x),np.cos(x)],[x,np.ones_like(x)],
        [r'$y=\sin x$',r'$y=\cos x$'],[r'$y=x$',r'$y=1$'],['Sine at zero','Cosine at zero']):
    ax.plot(x,y,color=blue,label=lab,linewidth=2.2)
    ax.plot(x,model,color=orange,label=modellab,linestyle='--',linewidth=2)
    ax.scatter([0],[float(y[len(y)//2]) if title.startswith('Sine') else 1],s=0)
    ax.scatter([0],[0 if title.startswith('Sine') else 1],color='#222222',zorder=4)
    ax.set_title(title); axes_common(ax); ax.set_xlim(-2.5,2.5); ax.set_ylim(-1.35,1.45)
    ax.legend(loc='lower left')
fig.savefig(FIG/'trig-linear.png'); plt.close(fig)

fig, ax = plt.subplots(figsize=(9,5.4),dpi=150,layout='constrained')
x = np.linspace(-2.1,2.1,500)
ax.plot(x,np.cos(x),color=blue,linewidth=2.2,label=r'$y=\cos x$')
ax.plot(x,np.ones_like(x),color=orange,linestyle='--',linewidth=1.7,label=r'$L(x)=1$')
ax.plot(x,1-x*x/2,color=green,linestyle='-.',linewidth=2,label=r'$Q(x)=1-x^2/2$')
ax.scatter([0],[1],color='#222222',zorder=4)
axes_common(ax); ax.set_xlim(-2.1,2.1); ax.set_ylim(-1.3,1.35)
ax.set_title('Matching curvature improves the local cosine model')
ax.legend(loc='lower center')
fig.savefig(FIG/'cos-quadratic.png'); plt.close(fig)

checks = {'origins': {'python':sys.executable,'numpy':np.__file__,
                     'matplotlib':matplotlib.__file__,'PIL':PIL.__file__},
          'write_destinations': {'MPLCONFIGDIR':os.environ['MPLCONFIGDIR'],
                                'TEMP':os.environ['TEMP'],'TMP':os.environ['TMP']}}
pdf = ROOT.parent/'original-inputs'/'mit-18.01-fall-2006-lec9.pdf'
reader = PdfReader(pdf)
checks['original_pdf']={'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
                        'pages':len(reader.pages), 'page_sizes':[list(map(float,p.mediabox)) for p in reader.pages]}
with localcontext() as ctx:
    ctx.prec=65
    D=Decimal
    q=(D(4)/D(300000))**2
    gamma=1/(1-q).sqrt()
    checks['timing']={'v_km_s':'4','c_km_s':'300000','q':str(q),'q_over_2':str(q/2),
                     'three_q_squared_over_8':str(3*q*q/8),'gamma':str(gamma),
                     'gamma_minus_1':str(gamma-1),'fractional_change_in_day_seconds':str((q/2)*D(86400))}
    q=D('.36'); exact=1/(1-q).sqrt(); lin=1+q/2; quad=lin+3*q*q/8
    checks['task_a3']={'q':str(q),'exact':str(exact),'linear':str(lin),'quadratic':str(quad),
                       'linear_absolute_error':str(abs(exact-lin)),
                       'quadratic_absolute_error':str(abs(exact-quad))}
checks['worked_checks']={'ln_1_02':math.log(1.02),'ln_1_02_L':.02,'ln_1_02_Q':.02-.02**2/2,
                         'f_0_02':math.exp(-.04)/math.sqrt(1.02),'f_0_02_L':1-2.5*.02,
                         'f_0_02_Q':1-2.5*.02+(27/8)*.02**2}
checks['task_a1']={'estimate':math.log(2)+.5*.04,'exact':math.log(2.04),'given_ln_2':.69314718056}
checks['task_a2']={'constant':0,'linear':3,'quadratic':-1.5,'limit':3,
                   'numerical_ratio_x_1e_4':math.sin(3e-4)/(1e-4*math.sqrt(1.0001))}
checks['task_a4']={'a':2.5,'quadratic_coefficient':27/8-25/4,'g_second_derivative_at_0':-23/4}
v=math.cos(.2)
checks['task_r1']={'cos_0_2':v,'linear':1,'quadratic':.98,
                   'linear_absolute_error':abs(1-v),'quadratic_absolute_error':abs(.98-v)}
checks['figures']=[{'file':p.name,'width':Image.open(p).width,'height':Image.open(p).height,
                    'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(FIG.glob('*.png'))]
(ROOT/'evidence'/'author-recomputations.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,indent=2))
