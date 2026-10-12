"""Render the three requested mathematical diagrams from exact functions."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "teaching" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#263442"
BLUE = "#2069ae"
RED = "#c43d3d"
GRAY = "#74808a"
GRID = "#e8ecef"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 14,
    "font.weight": "normal",
    "font.style": "normal",
    "axes.labelweight": "normal",
    "axes.titleweight": "normal",
    "axes.titlesize": 19,
    "axes.labelsize": 15,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "text.color": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "mathtext.fontset": "dejavusans",
    "savefig.facecolor": "white",
})


def frame(title, xlim, ylim, xticks, yticks):
    fig, ax = plt.subplots(figsize=(8, 5.4), dpi=200)
    fig.subplots_adjust(left=0.10, right=0.965, bottom=0.12, top=0.88)
    ax.set_title(title, pad=18)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_xlabel("$t$", labelpad=9)
    ax.set_ylabel("$y$", rotation=0, labelpad=17)
    ax.grid(color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#a6afb7")
        ax.spines[side].set_linewidth(0.9)
    ax.tick_params(length=4, width=0.8)
    return fig, ax


def export(fig, filename):
    # Fixed canvas, rather than tight cropping, preserves all margins exactly.
    fig.savefig(OUT / filename, dpi=200)
    plt.close(fig)


def mvt_parallel():
    fig, ax = frame(
        "Parallel secant and tangent", (-0.10, 2.20), (-1.85, 4.85),
        [0, 0.5, 1, 1.5, 2], [-1, 0, 1, 2, 3, 4],
    )
    t = np.linspace(0, 2, 801)
    ax.plot(t, t**2, color=INK, lw=2.8, label="$f(t)=t^2$", zorder=3)
    ax.plot(t, 2*t, color=BLUE, lw=2.3, label="Secant $L(t)=2t$", zorder=2)
    ax.plot(t, 2*t-1, color=RED, lw=2.3,
            label="Tangent $T(t)=2t-1$", zorder=4)
    d = np.linspace(0, 0.75, 201)
    ax.plot(d, 2*d-1.65, color=GRAY, lw=1.7, ls=(0, (5, 4)), zorder=1)
    ax.scatter([0, 2], [0, 4], s=37, color=BLUE, zorder=6)
    ax.scatter([1], [1], s=47, facecolor="white", edgecolor=RED,
               linewidth=2, zorder=7)
    ax.text(0.08, -0.14, "$(0,0)$", va="top", fontsize=13)
    ax.text(2.04, 4.10, "$(2,4)$", ha="right", va="bottom", fontsize=13)
    ax.annotate("$c=1$", xy=(1, 1), xytext=(0.79, 0.20),
                color=RED, fontsize=14,
                arrowprops={"arrowstyle": "-", "color": RED, "lw": 1.0},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.annotate("slope $2$", xy=(1.66, 2.32), xytext=(1.57, 1.32),
                color=RED, fontsize=14,
                arrowprops={"arrowstyle": "-", "color": RED, "lw": 1.0},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    # The dashed line has the same slope and a smaller intercept.
    ax.annotate("", xy=(0.32, 2*0.32-1), xytext=(0.32, 2*0.32-1.65),
                arrowprops={"arrowstyle": "-|>", "color": GRAY, "lw": 1.9})
    ax.text(0.48, -1.39, "Translate upward", color=GRAY, fontsize=13)
    ax.legend(loc="upper left", bbox_to_anchor=(0.015, 0.98),
              frameon=False, fontsize=13, handlelength=2.0,
              borderaxespad=0.2, labelspacing=0.55)
    export(fig, "mvt-parallel.png")


def corner():
    fig, ax = frame(
        "A corner at $t=0$", (-1.25, 1.25), (-0.40, 1.58),
        [-1, -0.5, 0, 0.5, 1], [0, 0.5, 1],
    )
    t = np.linspace(-1, 1, 801)
    ax.plot(t, np.abs(t), color=INK, lw=3, zorder=3)
    ax.plot([-1, 1], [1, 1], color=BLUE, lw=2.3, zorder=2)
    ax.plot([-1, 1], [0, 0], color=RED, lw=2.3, zorder=2)
    ax.scatter([-1, 1], [1, 1], s=38, color=BLUE, zorder=6)
    ax.scatter([0], [0], s=47, facecolor="white", edgecolor=RED,
               linewidth=2, zorder=7)
    ax.text(0, 1.35, "$f(t)=|t|$", ha="center", fontsize=17)
    ax.text(0, 1.06, "Secant $y=1$", ha="center", color=BLUE, fontsize=14)
    ax.text(-0.72, 0.23, "left slope $-1$", ha="center", fontsize=14)
    ax.text(0.73, 0.23, "right slope $+1$", ha="center", fontsize=14)
    ax.text(-1.08, -0.085, "$y=0$", ha="left", va="top", color=RED, fontsize=14)
    ax.text(0.13, -0.25, "Derivative at $0$ undefined", ha="center", fontsize=14)
    export(fig, "corner.png")


def approximation():
    fig, ax = frame(
        "Linear estimate and exact value", (0.95, 1.90), (0.84, 3.12),
        [1, 1.25, 1.5, 1.65], [1, 1.5, 2, 2.5, 3],
    )
    t = np.linspace(1, 1.65, 801)
    ax.plot(t, t**2, color=INK, lw=2.8, label="$f(t)=t^2$", zorder=3)
    ax.plot(t, 1+2*(t-1), color=RED, lw=2.3,
            label="Tangent $L(t)=1+2(t-1)$", zorder=4)
    ax.scatter([1], [1], s=43, color=RED, zorder=7)
    ax.axvline(1.5, ymin=0, ymax=(2.25-0.84)/(3.12-0.84),
               color="#bdc5cc", lw=1.2, ls=(0, (4, 4)), zorder=1)
    ax.scatter([1.5], [2.25], s=43, color=INK, zorder=7)
    ax.scatter([1.5], [2], s=43, color=RED, zorder=7)
    ax.annotate("Exact $2.25$", xy=(1.5, 2.25), xytext=(1.27, 2.49),
                color=INK, fontsize=14,
                arrowprops={"arrowstyle": "-", "color": INK, "lw": 1.0},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.annotate("Estimate $2$", xy=(1.5, 2), xytext=(1.58, 1.67),
                color=RED, fontsize=14, ha="center",
                arrowprops={"arrowstyle": "-", "color": RED, "lw": 1.0},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.annotate("", xy=(1.5, 2.25), xytext=(1.5, 2),
                arrowprops={"arrowstyle": "<->", "color": BLUE,
                            "lw": 1.8, "shrinkA": 3, "shrinkB": 3}, zorder=8)
    ax.text(1.70, 2.125, "Error $0.25$", color=BLUE, fontsize=14,
            va="center", bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.text(1.06, 0.98, "$a=1$", color=RED, fontsize=14, va="center")
    ax.text(1.5, 1.02, "$x=1.5$", ha="center", fontsize=13,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.legend(loc="upper left", bbox_to_anchor=(0.015, 0.98),
              frameon=False, fontsize=13, handlelength=2.0,
              borderaxespad=0.2, labelspacing=0.55)
    export(fig, "approximation.png")


if __name__ == "__main__":
    mvt_parallel()
    corner()
    approximation()
    for p in sorted(OUT.glob("*.png")):
        print(p)
