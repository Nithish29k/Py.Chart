from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np
import io
from matplotlib import lines, patches
from matplotlib.patheffects import withStroke

app = Flask(__name__)

@app.route('/designCh')
def generate_chart():
    counts = [6, 7, 7, 9, 11, 15, 17, 18, 54]
    names = [
        "Hantavirus", "Tularemia", "Dengue", "Ebola", "E. coli", 
        "Tuberculosis", "Salmonella", "Vaccinia", "Brucella"
    ]

    y = [i * 0.9 for i in range(len(names))]

    # Colors
    BLUE = "#076fa2"
    RED = "#E3120B"
    BLACK = "#202020"
    GREY = "#a2a2a2"

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.barh(y, counts, height=0.55, align="edge", color=BLUE)

    ax.xaxis.set_ticks([i * 5 for i in range(0, 12)])
    ax.xaxis.set_ticklabels([i * 5 for i in range(0, 12)], size=16, fontfamily="sans-serif")
    ax.xaxis.set_tick_params(labelbottom=False, labeltop=True, length=0)

    ax.set_xlim((0, 55.5))
    ax.set_ylim((0, len(names) * 0.9 - 0.2))

    ax.set_axisbelow(True)
    ax.grid(axis="x", color="#A8BAC4", lw=1.2)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_lw(1.5)
    ax.spines["left"].set_capstyle("butt")

    ax.yaxis.set_visible(False)

    PAD = 0.3
    for name, count, y_pos in zip(names, counts, y):
        x = 0
        color = "white"
        path_effects = None
        if count < 8:
            x = count
            color = BLUE
            path_effects = [withStroke(linewidth=6, foreground="white")]

        ax.text(
            x + PAD, y_pos + 0.5 / 2, name,
            color=color, fontfamily="sans-serif", fontsize=18, va="center",
            path_effects=path_effects
        )

    fig.subplots_adjust(left=0.005, right=1, top=0.8, bottom=0.1)

    # Title, Subtitle, and Caption
    fig.text(0, 0.925, "Escape artists", fontsize=22, fontweight="bold")
    fig.text(0, 0.875, "Number of laboratory-acquired infections, 1970-2021", fontsize=20)
    fig.text(0, 0.06, "Source: American Biological Safety Association", color=GREY, fontsize=14)
    fig.text(0, 0.005, "The Economist", color=GREY, fontsize=16)

    fig.add_artist(lines.Line2D([0, 1], [1, 1], lw=3, color=RED, solid_capstyle="butt"))
    fig.add_artist(patches.Rectangle((0, 0.975), 0.05, 0.025, color=RED))

    fig.set_facecolor("white")

    # Send the plot as an image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
