import matplotlib.pyplot as plt
import seaborn as sns
from flight_analysis.plot_utils import save_plot, add_table

def plot_coach_price_distribution(flight, benchmark=500, output_path="images/task1_coach_price.png"):
    """Plot distribution of coach ticket prices with summary statistics and benchmark."""

    # --- Summary statistics ---
    mean_price = flight["coach_price"].mean()
    median_price = flight["coach_price"].median()
    min_price = flight["coach_price"].min()
    max_price = flight["coach_price"].max()
    q1 = flight["coach_price"].quantile(0.25)
    q3 = flight["coach_price"].quantile(0.75)
    iqr = q3 - q1

    # --- Histogram ---
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(flight["coach_price"], bins=30, kde=True, color="skyblue", ax=ax)

    # Highlight IQR
    ax.axvspan(q1, q3, color="yellow", alpha=0.2, label="Typical Range (Q1-Q3)")

    # Add vertical lines
    ax.axvline(mean_price, color="red", linestyle="--", linewidth=2, label=f"Mean: ${mean_price:.0f}")
    ax.axvline(median_price, color="green", linestyle="--", linewidth=2, label=f"Median: ${median_price:.0f}")
    ax.axvline(benchmark, color="purple", linestyle="-", linewidth=2, label=f"${benchmark} Benchmark")

    # Titles
    ax.set_title("Distribution of Coach Ticket Prices", fontsize=14, weight="bold")
    ax.set_xlabel("Coach Price ($)")
    ax.set_ylabel("Number of Flights")
    ax.legend()

    # --- Table below plot ---
    cell_text = [[
        f"${min_price:.0f}", f"${q1:.0f}", f"${median_price:.0f}",
        f"${mean_price:.0f}", f"${q3:.0f}", f"${max_price:.0f}",
        f"${iqr:.0f}", f"${benchmark}"
    ]]
    columns = ["Min", "Q1", "Median", "Mean", "Q3", "Max", "IQR", "Benchmark"]
    cell_colors = [[
        (1,1,1,0.3), (1,1,0,0.3), (0,1,0,0.3), (1,0,0,0.3),
        (1,1,0,0.3), (1,1,1,0.3), (1,1,0,0.3), (0.5,0,0.5,0.3)
    ]]
    add_table(ax, cell_text, columns, row_labels=None, cell_colors=cell_colors)

    # --- Verdict text ---
    if benchmark < q1:
        verdict = "a really good deal (below typical prices)"
    elif benchmark > q3:
        verdict = "on the expensive side (above typical prices)"
    else:
        verdict = "pretty average (within the typical middle range)"

    ax.text(0.5, -0.55, f"A ${benchmark:.0f} ticket is {verdict}.",
            ha="center", va="top", fontsize=12, transform=ax.transAxes)

    plt.subplots_adjust(bottom=0.4)

    # Save image
    save_plot(fig, output_path)