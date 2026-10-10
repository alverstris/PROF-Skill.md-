from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json, hashlib

p=Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25/repair/probe-input')
p.mkdir()
for name,margins in [('motion-a',(0.12,0.97,0.22,0.80)),('motion-b',(0.12,0.97,0.015,0.99))]:
    fig,ax=plt.subplots(figsize=(7.2,3.6),dpi=160)
    fig.subplots_adjust(left=margins[0],right=margins[1],bottom=margins[2],top=margins[3])
    t=np.linspace(0,2,100)
    ax.plot(t,2*t,color='#196ca3',lw=2)
    ax.set(xlim=(0,2),ylim=(0,4),xlabel='Time t (seconds)',ylabel='Displacement (metres)',title='Uniform motion: displacement increases with time')
    ax.grid(alpha=.25)
    fig.savefig(p/(name+'.png'))
    plt.close(fig)
(p/'notes.md').write_text('''A short reference for interpreting totals

This is a reference excerpt, with no learner-response tasks. Prior knowledge includes ordinary definite integrals, average value and multiplication of units. Here q(u) is energy measured in joules and u is a dimensionless fraction from zero to one. The integral adds q(u) times the dimensionless width du. Its average on that interval is the integral divided by the dimensionless width one. Integrals and averages always have different units.

For comparison, integrating a power p(t) in watts over a duration t measured in seconds gives joules, and its time average is measured in watts.

The following two figures both represent displacement 2t metres at numerical time t seconds, for 0 to 2 seconds.

![First motion diagram.](motion-a.png)

![Second motion diagram.](motion-b.png)
''')
records=[{'path':f.name,'bytes':len(f.read_bytes()),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(p.iterdir())]
(p.parent/'probe-input-identities.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records))
