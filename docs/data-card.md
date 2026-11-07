
# Data Card: Synthetic Healthcare Metadata Inventory

## Dataset Overview

**Dataset name:** Synthetic Healthcare Metadata Inventory

**File:** `data/metadata_inventory.csv`

**Purpose:** Support an educational Data Governance project that measures metadata completeness, ownership coverage, stewardship coverage, and documentation gaps.

**Dataset size:** 60 fictional data assets across five healthcare-related departments.

## Data Source and Provenance

This dataset was created specifically for the Continuous Intelligence Project 03: Signal Design assignment.

The records are entirely synthetic and represent a fictional healthcare organization. Dataset names and metadata statuses were constructed for educational analysis rather than extracted from an operational system.

No real patient, employee, organizational, or protected health information (PHI) is included.

No external dataset was downloaded or incorporated. The data was generated for this project with AI assistance and reviewed as part of the project workflow.

## Departments Represented

Each department contains 12 fictional data assets:

- Clinical Analytics
- Revenue Cycle
- Quality Improvement
- Health Information Management
- Human Resources

## Data Dictionary

| Column | Description |
|---|---|
| `asset_id` | Unique identifier for each fictional data asset |
| `dataset_name` | Descriptive name of the fictional dataset |
| `department` | Department responsible for the data asset |
| `data_owner` | Indicates whether a data owner is assigned |
| `data_steward` | Indicates whether a data steward is assigned |
| `description` | Indicates whether a dataset description is complete |
| `business_definition` | Indicates whether a business definition is complete |
| `data_classification` | Indicates whether a classification is documented |

## Metadata Status Values

The inventory uses simplified status indicators rather than actual metadata content.

- `Assigned`: An owner or steward is documented.
- `Complete`: A description or business definition is documented.
- `Missing`: Required metadata is not documented.
- `Confidential` or `Internal`: A data classification is documented.

## Intended Uses

This dataset supports:

- Calculating metadata completeness for individual data assets.
- Measuring data ownership and stewardship coverage.
- Identifying missing documentation.
- Comparing governance readiness across departments.
- Demonstrating a reproducible Python data pipeline.

## Licensing and Usage

The dataset was created for this educational project using synthetic records and AI assistance. No external dataset or third-party data license was used.

No separate reuse license has been assigned to this dataset. Reuse permissions should not be inferred from the absence of an external license.

## Limitations

1. The dataset is synthetic and does not represent actual healthcare organizational performance.
2. Each department contains exactly 12 assets, which may not reflect real organizational distributions.
3. Metadata statuses are simplified and do not measure the accuracy or quality of documented information.
4. Ownership and stewardship signals indicate assignment status, not whether responsibilities are actively performed.
5. The dataset represents a single snapshot and cannot yet demonstrate changes over time.

## Ethical and Privacy Considerations

The dataset contains no real patient records, employee records, or PHI.

The analysis is intended for educational demonstration and should not be interpreted as an assessment of any actual healthcare department or organization.
