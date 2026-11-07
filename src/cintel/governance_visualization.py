"""Create a heatmap of departmental Data Governance readiness."""

from pathlib import Path

import matplotlib.pyplot as plt
import polars as pl


def main() -> None:
    """Visualize governance readiness across departments."""
    # Locate the input and output files
    project_root = Path(__file__).resolve().parents[2]
    input_path = project_root / "artifacts" / "governance_department_summary.csv"
    output_path = project_root / "artifacts" / "governance_readiness_heatmap.png"

    # Load the departmental summary
    df = pl.read_csv(input_path)

    # Convert documentation gaps into documentation completeness
    df = df.with_columns(
        (100 - pl.col("documentation_gap_pct")).alias("documentation_pct")
    )

    # Define the measurements to display
    columns = [
        "completeness_pct",
        "ownership_pct",
        "stewardship_pct",
        "documentation_pct",
    ]

    labels = [
        "Metadata\nCompleteness",
        "Ownership\nCoverage",
        "Stewardship\nCoverage",
        "Documentation\nCompleteness",
    ]

    # Prepare the heatmap values
    values = df.select(columns).to_numpy()
    departments = df["department"].to_list()

    # Create the heatmap
    fig, ax = plt.subplots(figsize=(11, 5))
    heatmap = ax.imshow(values, cmap="RdYlGn", vmin=0, vmax=100, aspect="auto")

    # Add labels
    ax.set_xticks(range(len(labels)), labels=labels)
    ax.set_yticks(range(len(departments)), labels=departments)

    # Display percentages inside each cell
    for row in range(len(departments)):
        for col in range(len(labels)):
            ax.text(
                col,
                row,
                f"{values[row, col]:.1f}%",
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold",
            )

    ax.set_title(
        "Data Governance Readiness by Department",
        fontsize=15,
        fontweight="bold",
        pad=20,
    )

    fig.colorbar(heatmap, ax=ax, label="Readiness (%)")
    fig.tight_layout()

    # Save the visualization
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved governance heatmap to {output_path}")


if __name__ == "__main__":
    main()
