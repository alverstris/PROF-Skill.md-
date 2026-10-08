from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
out=Path(__file__).resolve().parents[1]
fig,ax=plt.subplots(figsize=(8.4,5.5),dpi=180)
u,v,du,dv=3.5,2.3,1.35,0.85
for x,y,w,h,c,label in [(0,0,u,v,'#f3a15c',r'$uv$'),(0,v,u,dv,'#f3b3a2',r'$u\,\Delta v$'),(u,0,du,v,'#f2e998',r'$v\,\Delta u$'),(u,v,du,dv,'#ffffff',r'$\Delta u\,\Delta v$')]:
 ax.add_patch(Rectangle((x,y),w,h,facecolor=c,edgecolor='#222222',linewidth=1.5));ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=17)
for a,b,y,label in [(0,u,-.28,r'$u$'),(u,u+du,-.28,r'$\Delta u$')]:
 ax.annotate('',xy=(a,y),xytext=(b,y),arrowprops={'arrowstyle':'<->','lw':1.2});ax.text((a+b)/2,y-.12,label,ha='center',va='top',fontsize=16)
for a,b,x,label in [(0,v,-.28,r'$v$'),(v,v+dv,-.28,r'$\Delta v$')]:
 ax.annotate('',xy=(x,a),xytext=(x,b),arrowprops={'arrowstyle':'<->','lw':1.2});ax.text(x-.12,(a+b)/2,label,ha='right',va='center',fontsize=16)
ax.set_aspect('equal');ax.set_xlim(-.85,u+du+.18);ax.set_ylim(-.7,v+dv+.2);ax.axis('off');fig.tight_layout(pad=.5);fig.savefig(out/'product-increment-v1.png',bbox_inches='tight',facecolor='white');plt.close(fig)
