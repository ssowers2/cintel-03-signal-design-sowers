"""Run the custom metadata governance signal pipeline."""

from pathlib import Path

import polars as pl

from cintel.utils_governance import (
    calculate_documentation_gap,
    calculate_metadata_completeness,
    calculate_ownership_signal,
    calculate_stewardship_signal,
)


def main() -> None:
    """Load metadata, calculate completeness, and save results."""
    # Locate project folders
    project_root = Path(__file__).resolve().parents[2]
    input_path = project_root / "data" / "metadata_inventory.csv"
    output_path = project_root / "artifacts" / "governance_signals.csv"
    summary_path = project_root / "artifacts" / "governance_department_summary.csv"

    # Load the synthetic metadata inventory
    df = pl.read_csv(input_path)
    print(f"Loaded {df.height} metadata records.")

    # Calculate the metadata completeness signal
    results = calculate_metadata_completeness(df)
    print("Calculated metadata completeness.")

    # Calculate the data ownership signal
    results = calculate_ownership_signal(results)
    print("Calculated data ownership signal.")

    # Calculate the data stewardship signal
    results = calculate_stewardship_signal(results)
    print("Calculated data stewardship signal.")

    # Calculate the documentation gap signal
    results = calculate_documentation_gap(results)
    print("Calculated documentation gap signal.")

    # Save results to a new CSV file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results.write_csv(output_path)
    print(f"Saved results to {output_path}")

    # Summarize governance signals by department
    department_summary = (
        results.group_by("department")
        .agg(
            pl.len().alias("assets"),
            (pl.col("metadata_completeness").mean() * 100)
            .round(2)
            .alias("completeness_pct"),
            (pl.col("owner_assigned").mean() * 100).round(2).alias("ownership_pct"),
            (pl.col("steward_assigned").mean() * 100).round(2).alias("stewardship_pct"),
            (pl.col("documentation_gap").mean() * 100)
            .round(2)
            .alias("documentation_gap_pct"),
        )
        .sort("completeness_pct")
    )

    # Save the departmental summary
    department_summary.write_csv(summary_path)
    print(f"Saved departmental summary to {summary_path}")


if __name__ == "__main__":
    main()
