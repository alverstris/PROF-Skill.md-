from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

out = Path(__file__).resolve().parents[1] / "teaching" / "figures"
out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "font.weight": "normal", "axes.titleweight": "normal",
                     "axes.labelweight": "normal", "figure.facecolor": "white"})
blue, green, orange, ink = "#24679c", "#137b59", "#bb641d", "#263445"

fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), constrained_layout=True)
x = np.linspace(0, 2, 301)
for ax in axes:
    ax.plot(x, x*x, color=ink, lw=2)
    ax.set(xlim=(-.08, 2.12), ylim=(-.18, 4.5), xlabel="x", ylabel="y")
    ax.set_xticks([0, .5, 1, 1.5, 2])
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(1.17, 3.7, r"$y=x^2$", color=ink)
axes[0].fill_between(x, 0, x*x, color=blue, alpha=.22)
axes[0].set_title("Curved region on [0, 2]", pad=15)
for i in range(1, 5):
    axes[1].add_patch(Rectangle(((i-1)/2, 0), .5, (i/2)**2,
                               fc=blue, ec=blue, alpha=.25, lw=1.5))
    axes[1].plot(i/2, (i/2)**2, "o", color=blue, ms=4)
axes[1].set_title("Four right-endpoint rectangles", pad=15)
fig.savefig(out/"rectangles.png", dpi=170)
plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), constrained_layout=True,
                         gridspec_kw={"width_ratios":[1, 1.25]})
ax=axes[0]
for side in [4, 3, 2, 1]:
    ax.add_patch(Rectangle((-side/2,-side/2),side,side,fill=False,ec=ink,lw=1.8))
ax.set(xlim=(-2.6,2.6),ylim=(-2.6,2.6),aspect="equal",xlabel="horizontal position",ylabel="horizontal position")
ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2])
ax.set_title("Top view: four centred square layers",pad=16)
ax.text(0,-2.4,"Side lengths: 4, 3, 2, 1",ha="center",va="center",fontsize=10)
ax.spines[["top","right"]].set_visible(False)
ax=axes[1]
for j in range(4):
    side=4-j
    ax.add_patch(Rectangle((-side/2,j),side,1,facecolor="#dce3e9",edgecolor=ink,lw=1.4))
ax.plot([-2,0,2],[0,4,0],color=green,lw=2.3,label="Inner pyramid")
ax.plot([-2.5,0,2.5],[0,5,0],color=orange,lw=2.3,label="Outer pyramid")
ax.set(xlim=(-3,3),ylim=(-.18,5.45),xlabel="horizontal position",ylabel="height z")
ax.set_xticks([-2,0,2]);ax.set_yticks([0,1,2,3,4,5])
ax.set_title("Vertical section through the centre",pad=16)
ax.legend(loc="upper right",bbox_to_anchor=(1,1.0),fontsize=9,framealpha=1)
ax.spines[["top","right"]].set_visible(False)
fig.savefig(out/"pyramids.png",dpi=170)
plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(10,4.8),constrained_layout=True)
ax=axes[0]
ax.add_patch(Polygon([[0,0],[2,0],[2,2]],facecolor=blue,alpha=.2))
ax.plot([0,2],[0,2],color=ink,lw=2);ax.plot([2,2],[0,2],color=blue,lw=1.5)
ax.set(xlim=(-.12,2.3),ylim=(-.12,2.35),xlabel="x",ylabel="y")
ax.set_xticks([0,1,2]);ax.set_yticks([0,1,2])
ax.text(.55,1.2,r"$y=x$",color=ink);ax.set_title("Triangle: base b and height b",pad=15)
ax.text(1,-.03,"b = 2",ha="center",va="top",fontsize=10)
ax.spines[["top","right"]].set_visible(False)
ax=axes[1]
ax.plot(x,x*x,color=ink,lw=2)
ax.add_patch(Rectangle((1,0),.5,1.2**2,fc=blue,ec=blue,alpha=.25,lw=1.5))
ax.plot([1.2,1.2],[0,1.2**2],linestyle="--",color=green,lw=1.4)
ax.plot(1.2,1.2**2,"o",color=green)
ax.annotate(r"$c_3=1.2$",xy=(1.2,0),xytext=(.55,.47),arrowprops={"arrowstyle":"->","color":green},color=green)
ax.annotate(r"$f(c_3)=1.44$",xy=(1.5,1.44),xytext=(1.28,2.45),arrowprops={"arrowstyle":"->","color":blue},color=blue)
ax.annotate("",xy=(1,-.24),xytext=(1.5,-.24),arrowprops={"arrowstyle":"<->","color":ink})
ax.text(1.25,-.35,r"$\Delta x=0.5$",ha="center",va="top",color=ink,fontsize=10)
ax.set(xlim=(-.06,2.2),ylim=(-.72,4.55),xlabel="x",ylabel="y")
ax.set_xticks([0,.5,1,1.5,2]);ax.set_yticks([0,1,2,3,4])
ax.set_title("One sample in its own subinterval",pad=15)
ax.spines[["top","right"]].set_visible(False)
fig.savefig(out/"triangle-and-tag.png",dpi=170)
plt.close(fig)
