import matplotlib.pyplot as plt

def save_plot(fig, filename: str, dpi: int = 300):
    """Save a matplotlib figure and close it."""
    fig.savefig(filename, bbox_inches='tight', dpi=dpi)
    plt.close(fig)

def add_table(ax, cell_text, col_labels, row_labels, cell_colors=None, bbox=[0, -0.45, 1, 0.25]):
    """A a table below a matplotlib plot."""
    table = ax.table(
        cellText=cell_text,
        colLabels=col_labels,
        rowLabels=row_labels,
        cellLoc='center',
        rowLoc='center',
        loc='bottom',
        cellColours=cell_colors,
        bbox=bbox
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for key, cell in table.get_celld().items():
        cell.set_height(0.15)
    return table