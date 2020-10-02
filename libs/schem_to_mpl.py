import matplotlib.pyplot as plt

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["font.family"] = "Yu Gothic"
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.edgecolor"] = "black"
plt.rcParams["legend.framealpha"] = 1


def to_mpl(d, size=None):
    schem_fig = d.draw(show=False)
    fig, ax = schem_fig.fig, schem_fig.ax

    ax.axis("equal")
    ax.axis("off")
    fig.patch.set_visible(False)

    if size != None:
        fig.set_size_inches(size)

    return fig, ax
