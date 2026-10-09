from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Arc, Ellipse
out=Path(__file__).parent/'figures';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans','font.weight':'normal','axes.titleweight':'normal'})
blue='#196d9b';ink='#242c35'
def finish(fig,name):
 fig.savefig(out/name,dpi=180,bbox_inches='tight',facecolor='white');plt.close(fig)
def arrow(ax,a,b,label,pos):
 ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='<->',color=ink,lw=1.3));ax.text(*pos,label,ha='center',va='center')
fig,ax=plt.subplots(figsize=(7,4));ax.set_aspect('equal');ax.axis('off');ax.plot([-4,46],[0,0],color=ink);ax.plot([0,0,40],[0,30,0],color=ink);ax.plot([0,2,2],[2,2,0],color=ink)
ax.scatter([0,40],[30,0],color=blue,s=55);ax.text(-1,32,'Fixed radar',ha='left');ax.text(40,3,'Car',ha='center');ax.text(45,-1,'Road',ha='left');ax.text(-2,15,'30 ft',ha='right');ax.text(24,18,'D(t)',ha='center');arrow(ax,(0,-5),(40,-5),'x(t)',(20,-8));ax.annotate('',xy=(28,1),xytext=(39,1),arrowprops=dict(arrowstyle='->',color=blue,lw=1.5));ax.text(24,4,'Approach',ha='center',color=blue);ax.set_xlim(-9,56);ax.set_ylim(-12,37);finish(fig,'radar-v2.png')
