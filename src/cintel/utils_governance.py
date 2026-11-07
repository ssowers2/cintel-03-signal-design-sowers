"""Reusable Data Governance signal calculations."""

import polars as pl


def calculate_metadata_completeness(df: pl.DataFrame) -> pl.DataFrame:
    """Calculate metadata completeness for each data asset."""
    required_fields = [
        "data_owner",
        "data_steward",
        "description",
        "business_definition",
        "data_classification",
    ]

    completed_fields = [
        (
            pl.col(field).is_not_null()
            & (pl.col(field) != "Missing")
            & (pl.col(field) != "")
        ).cast(pl.Int64)
        for field in required_fields
    ]

    return df.with_columns(
        (pl.sum_horizontal(completed_fields) / len(required_fields)).alias(
            "metadata_completeness"
        )
    )


def calculate_ownership_signal(df: pl.DataFrame) -> pl.DataFrame:
    """Identify whether each data asset has an assigned owner."""
    return df.with_columns(
        (
            pl.col("data_owner").is_not_null()
            & (pl.col("data_owner") != "Missing")
            & (pl.col("data_owner") != "")
        )
        .cast(pl.Int64)
        .alias("owner_assigned")
    )


def calculate_stewardship_signal(df: pl.DataFrame) -> pl.DataFrame:
    """Identify whether each data asset has an assigned steward."""
    return df.with_columns(
        (
            pl.col("data_steward").is_not_null()
            & (pl.col("data_steward") != "Missing")
            & (pl.col("data_steward") != "")
        )
        .cast(pl.Int64)
        .alias("steward_assigned")
    )


def calculate_documentation_gap(df: pl.DataFrame) -> pl.DataFrame:
    """Flag assets missing a description or business definition."""
    return df.with_columns(
        (
            (pl.col("description") == "Missing")
            | (pl.col("business_definition") == "Missing")
        )
        .cast(pl.Int64)
        .alias("documentation_gap")
    )
