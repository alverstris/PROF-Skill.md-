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
ax.scatter([0,40],[30,0],color=blue,s=55);ax.text(-1,32,'Fixed radar',ha='left');ax.text(40,3,'Car',ha='center');ax.text(45,-1,'Road',ha='left');ax.text(-2,15,'30 ft',ha='right');ax.text(24,18,'D(t)',ha='center');arrow(ax,(0,-5),(40,-5),'x(t)',(20,-8));ax.annotate('Approach',xy=(29,1),xytext=(41,12),arrowprops=dict(arrowstyle='->',color=blue),color=blue);ax.set_xlim(-9,56);ax.set_ylim(-12,37);finish(fig,'radar.png')
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,5));
for q in (ax,bx):q.set_aspect('equal');q.axis('off')
ax.plot([-4,0,4],[10,0,10],color=ink);ax.add_patch(Ellipse((0,10),8,1.4,fill=False,edgecolor=ink));ax.add_patch(Polygon([(-2,5),(0,0),(2,5)],facecolor='#b3dbe9',edgecolor='none'));ax.add_patch(Ellipse((0,5),4,.7,facecolor='#b3dbe9',edgecolor=blue));ax.plot([0,0],[0,10],ls=':',color=ink);arrow(ax,(0,10),(4,10),'4 ft',(2,11));arrow(ax,(-5,0),(-5,10),'10 ft',(-6,5));arrow(ax,(0,5),(2,5),'r',(1,5.7));arrow(ax,(3,0),(3,5),'h',(3.6,2.5));ax.text(0,-1.3,'Water occupies the smaller cone',ha='center');ax.set_xlim(-7,5);ax.set_ylim(-2,12)
bx.add_patch(Polygon([(0,0),(0,5),(2,5)],facecolor='#b3dbe9',edgecolor='none'));bx.plot([0,0,4,0],[0,10,10,0],color=ink);bx.plot([0,2],[5,5],color=blue,lw=2);bx.plot([0,.35,.35],[9.65,9.65,10],color=ink);arrow(bx,(0,11),(4,11),'4 ft',(2,11.7));arrow(bx,(-1,0),(-1,10),'10 ft',(-2,5));arrow(bx,(0,5.5),(2,5.5),'r',(1,6.2));arrow(bx,(-.3,0),(-.3,5),'h',(-.58,2.5));bx.text(1,-1.3,'Half of the central vertical section',ha='center');bx.set_xlim(-3,6);bx.set_ylim(-2,12);finish(fig,'cone.png')
fig,ax=plt.subplots(figsize=(7,4.3));ax.set_aspect('equal');ax.axis('off');ax.plot([0,0,4,0],[0,3,0,0],color=ink);ax.plot([0,.2,.2],[.2,.2,0],color=ink);ax.scatter([0],[3],s=70,color=blue);ax.text(.15,3.15,'Satellite',va='bottom');ax.text(-.2,1.5,'c',ha='right');ax.text(2,-.3,'L',ha='center');ax.text(2.2,1.7,'h',ha='center');ax.text(2,-.85,'h is slant distance; c is vertical separation',ha='center');ax.set_xlim(-.8,5);ax.set_ylim(-1.1,3.8);finish(fig,'satellite.png')
fig,ax=plt.subplots(figsize=(6,5));ax.set_aspect('equal');ax.axis('off');x=np.linspace(-1.5,1.5,400);ax.plot(x,x*x,color=ink,lw=1.6);F=np.array([0,.25]);pts=[np.array([.6,.36]),np.array([.95,.9025])]
for p in pts:ax.plot([F[0],p[0]],[F[1],p[1]],color=blue);ax.plot([p[0],p[0]],[p[1],2.2],color=blue)
ax.scatter(*F,s=25,color=ink);angles=[np.degrees(np.arctan2(*(p-F)[::-1])) for p in pts];ax.add_patch(Arc(F,.6,.6,theta1=angles[0],theta2=angles[1],color=ink));ax.text(.32,.4,r'$\Delta\theta$',ha='left');arrow(ax,(.6,2.08),(.95,2.08),r'$\Delta a$',(.775,2.45));ax.text(-.1,-.45,'Schematic: two ray directions and positions',ha='center');ax.set_xlim(-1.8,1.8);ax.set_ylim(-.65,2.75);finish(fig,'mirror.png')
